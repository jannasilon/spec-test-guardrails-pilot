# Experiment protocol

## Research question
Does giving an AI coding agent executable behaviour specifications (Gherkin + tests),
in addition to prose requirements, reduce requirement violations in its code?

## Tasks
| Task | Requirements | Instruction to the agent |
|---|---|---|
| T1 | R1, R2, R10 | Implement `work_day` for weekdays |
| T2 | R3 | Add the minimum-break rule |
| T3 | R4, R9 | Handle weekends and public holidays |
| T4 | R5 | Support night shifts |
| T5 | R6 | Validate input |
| T6 | R7, R8 | Implement `work_week` with rounding |

## Conditions
- **A (prose):** working copy contains `docs/requirements.md` and `src/` only; `tests/` removed.
- **B (specs + tests):** working copy contains requirements, `src/` and `tests/`; the agent is told to make the tests pass.

The tasks run in order, in a fresh branch per condition. Each condition is run **3 times** (agents are non-deterministic).

## Controls
- Same model and version for all runs; record it, with the date.
- Same prompt template; only the condition-specific sentence differs.
- `evaluation/hidden_tests/` is **moved outside the working copy** before every run.
- The agent may run commands; we do not edit its code.

## Measures (per run)
1. Hidden acceptance tests passed / total.
2. Requirements violated (each failing hidden test mapped to an R-number).
3. Did the agent modify, skip or weaken any provided test? (`git diff tests/`)
4. How did it handle R8's ambiguity: asked, stated an assumption, or silent?
5. Agent turns and wall-clock time.

## Threats to validity
- Six tasks and one small domain: results do not generalise.
- The same person wrote the requirements, scenarios and hidden tests.
- Model behaviour changes across versions and days.
