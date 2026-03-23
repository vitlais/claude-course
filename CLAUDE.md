# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A learning project for exploring Claude Code features — custom commands, skills, MCP servers, GitHub integration, and hooks. Built with Python 3.12 and managed via `uv`.

## Commands

```bash
# Run the project
uv run python main.py

# Add a dependency
uv add <package>
```

## Architecture

The project is minimal by design — `main.py` is the single entry point. New functionality is added there as the course progresses through Claude Code features.

The GitHub Actions workflow (`.github/workflows/claude.yml`) triggers Claude on `@claude` mentions in issues and pull request comments, using `CLAUDE_CODE_OAUTH_TOKEN` for authentication (Pro subscription).
