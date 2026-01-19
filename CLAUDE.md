# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development Commands

```bash
# Run the CLI
python idea_spark.py "topic"

# With options
python idea_spark.py "topic" --tone professional --audience "target audience"
```

No dependencies to install - uses Python standard library only.

## Architecture

Single-file CLI app (`idea_spark.py`) using argparse. Template-based generation with tone-specific angle/step templates. Deterministic output via seeded random based on topic+audience hash.
