# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AgenticAI is a data engineering project that leverages Claude (Anthropic's AI) for agentic workflows — automating and orchestrating data pipelines, transformations, and analysis tasks.

## Repository Structure

```
AgenticAI/
├── claude/
│   ├── agents/          # Claude agent definitions
│   └── prompts/         # Reusable prompt templates
├── pipelines/
│   ├── databricks/
│   │   ├── ingestion/
│   │   │   ├── batch/       # File-based batch ingestion (CSV, JSON, Parquet)
│   │   │   ├── sql/         # SQL database ingestion
│   │   │   ├── api/         # REST/GraphQL API ingestion
│   │   │   └── streaming/   # Streaming ingestion (Kafka, Kinesis, etc.)
│   │   ├── transformation/  # Data transformation logic
│   │   └── validation/      # Data quality checks
│   └── snowflake/
│       ├── ingestion/
│       │   ├── batch/
│       │   ├── sql/
│       │   ├── api/
│       │   └── streaming/
│       ├── transformation/
│       └── validation/
├── data/
│   ├── raw/             # Raw/source data (gitignored)
│   ├── processed/       # Transformed data (gitignored)
│   └── schemas/         # Schema definitions
├── notebooks/           # Exploratory analysis
├── tests/
│   ├── databricks/
│   │   ├── ingestion/
│   │   │   ├── batch/
│   │   │   ├── sql/
│   │   │   ├── api/
│   │   │   └── streaming/
│   │   ├── transformation/
│   │   └── validation/
│   └── snowflake/
│       ├── ingestion/
│       │   ├── batch/
│       │   ├── sql/
│       │   ├── api/
│       │   └── streaming/
│       ├── transformation/
│       └── validation/
├── configs/             # Environment/pipeline configs
├── docs/
│   └── architecture/    # Architecture diagrams (see below)
└── .github/             # GitHub Actions workflows
```

## Development Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # then add your ANTHROPIC_API_KEY
```

Run tests:
```bash
pytest tests/
```

## Architecture Diagrams

Diagrams live in `docs/architecture/`. Use `.mermaid` or `.md` with Mermaid blocks for source, `.png`/`.svg` for rendered output.

**When to update this file:** Any time a new diagram is added or a major component changes, update the list below and reflect the change in the relevant section of CLAUDE.md.

| Diagram | Description |
|---------|-------------|
| _(none yet)_ | Add diagrams as the project evolves |

## Testing Requirements

Every code change must include corresponding test cases in `tests/`. Mirror the source structure by platform (e.g., `pipelines/databricks/ingestion/sql/loader.py` → `tests/databricks/ingestion/sql/test_loader.py`). Tests must pass before moving to the next step.
