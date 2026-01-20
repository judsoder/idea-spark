# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development Commands

```bash
# Install for development
pip install -e .

# Run the CLI (after install)
idea-spark "topic"

# With options
idea-spark "topic" --tone professional --audience "target audience"

# Or run directly without install
python -m idea_spark.cli "topic"
```

No external dependencies - uses Python standard library only.

## Architecture

Python package (`idea_spark/`) with CLI entry point. Template-based generation with tone-specific angle/step templates. Deterministic output via seeded random based on topic+audience hash.

- `idea_spark/__init__.py` - Package init with version
- `idea_spark/cli.py` - CLI implementation with `main()` entry point
- `pyproject.toml` - Package config with `idea-spark` console script entry point
