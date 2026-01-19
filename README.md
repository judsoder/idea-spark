# idea_spark

A command-line tool that generates creative angles and actionable next steps for any topic.

## Usage

```bash
python idea_spark.py "your topic here"
```

### Options

- `--tone` - Choose the style of suggestions: `punchy` (default), `professional`, or `playful`
- `--audience` - Specify a target audience to tailor suggestions

### Examples

Basic usage with default punchy tone:
```bash
python idea_spark.py "remote work"
```

Professional tone for business contexts:
```bash
python idea_spark.py "AI ethics" --tone professional
```

Playful tone with a specific audience:
```bash
python idea_spark.py "cooking" --tone playful --audience "busy parents"
```

## Output

Each run generates:
- 10 short angles (each 12 words or fewer)
- 3 actionable next steps

## Requirements

Python 3.6+ (standard library only, no external dependencies)
