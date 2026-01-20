# idea_spark

A command-line tool that generates creative angles and actionable next steps for any topic.

## Installation

### With pipx (recommended)

```bash
pipx install .
```

### With pip

```bash
pip install .
```

### Development install

```bash
pip install -e .
```

## Usage

```bash
idea-spark "your topic here"
```

### Options

- `--tone` - Choose the style of suggestions: `punchy` (default), `professional`, or `playful`
- `--audience` - Specify a target audience to tailor suggestions
- `--copy` - Copy output to clipboard (macOS only)

### Examples

Basic usage with default punchy tone:
```bash
idea-spark "remote work"
```

Professional tone for business contexts:
```bash
idea-spark "AI ethics" --tone professional
```

Playful tone with a specific audience:
```bash
idea-spark "cooking" --tone playful --audience "busy parents"
```

Copy output to clipboard (macOS):
```bash
idea-spark "productivity" --copy
```

## Output

Each run generates:
- 10 short angles (each 12 words or fewer)
- 3 actionable next steps

## Smoke Test

Verify the tool works correctly:
```bash
idea-spark "test" --copy && echo "Smoke test passed"
```

## Requirements

Python 3.6+ (standard library only, no external dependencies)
