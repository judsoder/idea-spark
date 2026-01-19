#!/usr/bin/env python3
"""idea_spark - Generate creative angles and next steps for any topic."""

import argparse
import random
import hashlib
from typing import List, Optional


def get_seed(topic: str, audience: Optional[str]) -> int:
    """Generate deterministic seed from inputs for reproducible results."""
    seed_str = topic + (audience or "")
    return int(hashlib.md5(seed_str.encode()).hexdigest()[:8], 16)


ANGLE_TEMPLATES = {
    "punchy": [
        "The contrarian take: why {topic} is misunderstood",
        "What everyone gets wrong about {topic}",
        "{topic} explained in one powerful metaphor",
        "The hidden cost of ignoring {topic}",
        "Why {topic} matters more than ever",
        "The {topic} mistake smart people make",
        "{topic}: the untold story",
        "How {topic} changes everything",
        "The {topic} playbook nobody talks about",
        "What {topic} can teach us about success",
        "The future of {topic} starts here",
        "{topic} decoded for the impatient",
        "Why your {topic} approach is outdated",
        "The {topic} revolution is already happening",
        "Stop overthinking {topic}—do this instead",
    ],
    "professional": [
        "A framework for understanding {topic}",
        "Key considerations when evaluating {topic}",
        "How {topic} impacts organizational outcomes",
        "Best practices for implementing {topic}",
        "The strategic value of {topic}",
        "Measuring success in {topic} initiatives",
        "Risk factors associated with {topic}",
        "{topic}: a data-driven perspective",
        "Building competency in {topic}",
        "The business case for {topic}",
        "Industry trends shaping {topic}",
        "Optimizing your {topic} strategy",
        "How leaders approach {topic} differently",
        "The economics of {topic}",
        "Integrating {topic} into your workflow",
    ],
    "playful": [
        "What if {topic} was a superpower?",
        "The {topic} starter pack nobody asked for",
        "{topic} but make it fun",
        "Why {topic} is secretly fascinating",
        "A love letter to {topic}",
        "{topic} for people who hate {topic}",
        "The {topic} rabbit hole worth exploring",
        "Making friends with {topic}",
        "Your {topic} origin story awaits",
        "{topic}: expect the unexpected",
        "The cozy guide to {topic}",
        "Adventures in {topic} land",
        "Why {topic} deserves a second chance",
        "{topic} without the boring parts",
        "The {topic} journey starts with curiosity",
    ],
}

NEXT_STEPS = {
    "punchy": [
        "Pick one angle and draft a bold opening line",
        "List three objections your audience might have",
        "Write a one-sentence hook that demands attention",
        "Identify the single biggest misconception to attack",
        "Find a surprising stat or story to lead with",
        "Map out the emotional journey you want readers on",
    ],
    "professional": [
        "Outline key stakeholders and their concerns",
        "Gather supporting data or case studies",
        "Draft an executive summary of your main argument",
        "Identify metrics to measure impact",
        "Create a timeline for research and drafting",
        "Schedule a review with subject matter experts",
    ],
    "playful": [
        "Brainstorm five unexpected analogies for your topic",
        "Sketch a quick visual or doodle to capture the vibe",
        "Write a draft as if explaining to a curious friend",
        "Find a meme or cultural reference that fits",
        "List what makes this topic secretly delightful",
        "Try writing the piece you wish existed",
    ],
}


def tailor_for_audience(text: str, audience: Optional[str]) -> str:
    """Append audience context to relevant items."""
    if audience:
        tailored_suffixes = [
            f" (for {audience})",
            f" tailored to {audience}",
            f" with {audience} in mind",
        ]
        if random.random() > 0.6:
            return text + random.choice(tailored_suffixes)
    return text


def generate_angles(topic: str, tone: str, audience: Optional[str]) -> List[str]:
    """Generate 10 unique angles for the topic."""
    templates = ANGLE_TEMPLATES[tone]
    random.shuffle(templates)

    angles = []
    for template in templates[:10]:
        angle = template.format(topic=topic)
        angle = tailor_for_audience(angle, audience)
        # Ensure <= 12 words by truncating if needed
        words = angle.split()
        if len(words) > 12:
            angle = " ".join(words[:12])
        angles.append(angle)

    return angles


def generate_next_steps(tone: str, audience: Optional[str]) -> List[str]:
    """Generate 3 actionable next steps."""
    steps = NEXT_STEPS[tone].copy()
    random.shuffle(steps)

    result = []
    for step in steps[:3]:
        result.append(tailor_for_audience(step, audience))

    return result


def format_output(topic: str, angles: List[str], steps: List[str], tone: str) -> str:
    """Format the output for terminal display."""
    width = 60

    lines = []
    lines.append("=" * width)
    lines.append(f"  IDEA SPARK: {topic.upper()}")
    lines.append(f"  Tone: {tone}")
    lines.append("=" * width)
    lines.append("")
    lines.append("  ANGLES")
    lines.append("  " + "-" * 20)

    for i, angle in enumerate(angles, 1):
        lines.append(f"  {i:2}. {angle}")

    lines.append("")
    lines.append("  NEXT STEPS")
    lines.append("  " + "-" * 20)

    for i, step in enumerate(steps, 1):
        lines.append(f"   {chr(96 + i)}) {step}")

    lines.append("")
    lines.append("=" * width)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate creative angles and next steps for any topic.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python idea_spark.py "remote work"
  python idea_spark.py "AI ethics" --tone professional
  python idea_spark.py "cooking" --tone playful --audience "busy parents"
        """,
    )
    parser.add_argument("topic", help="The topic to generate ideas for")
    parser.add_argument(
        "--tone",
        choices=["punchy", "professional", "playful"],
        default="punchy",
        help="Tone of the suggestions (default: punchy)",
    )
    parser.add_argument(
        "--audience",
        help="Target audience to tailor suggestions (free text)",
    )

    args = parser.parse_args()

    # Seed random for reproducibility based on inputs
    random.seed(get_seed(args.topic, args.audience))

    angles = generate_angles(args.topic, args.tone, args.audience)
    steps = generate_next_steps(args.tone, args.audience)

    print(format_output(args.topic, angles, steps, args.tone))


if __name__ == "__main__":
    main()
