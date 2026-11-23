# Do specifications and tests keep an AI coding agent on track?

A small pilot study on **specification- and test-based guardrails for AI coding agents**.

An AI coding agent (Claude Code) implements the same six tasks for a small
time-reporting library under two conditions:

| Condition | What the agent gets |
|---|---|
| **A – prose only** | Natural-language requirements (`docs/requirements.md`) |
| **B – specs + tests** | The same requirements **plus** Gherkin scenarios and executable tests (`tests/`) |

Each result is then checked against a set of **hidden acceptance tests** the agent
never saw. We count missed requirements, defects, and any changes the agent made
to the provided tests.

- Requirements: [`docs/requirements.md`](docs/requirements.md)
- Experiment protocol: [`docs/protocol.md`](docs/protocol.md)
- Results and report: [`docs/report.md`](docs/report.md) *(to be written)*

## Run the tests

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

The library is intentionally unimplemented on `main`: every test fails until an
agent (or a human) implements `src/timesheet/core.py`.
