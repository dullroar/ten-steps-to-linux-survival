# <Plan name> - specification and execution agreement

Status: draft | approved (by <owner>, <date>) | complete | withdrawn

Keep this short. A spec states behavior and constraints the result must satisfy; the steps say how
the work is done. Mark every rule as **documented** (cite the source) or **inferred** (AI or author
judgement, needs confirmation). Do not present an inference as a documented rule.

## Goal and exclusions

One paragraph of intent. Then an explicit list of what this work does NOT do.

## Requirements

Each requirement gets an ID heading that steps cite in their `requirements:` field.

### R1. <Short behavior statement>

- Basis: documented (<source>) | inferred (unconfirmed)
- Example: <concrete input -> expected result>
- Acceptance check: <protected check that proves it; path or command>

## Constraints and assumptions

Business rules, technical constraints, and assumptions that could be wrong (each with who can confirm).

## Domain challenge

Counterexamples considered: legitimate exceptions that would invalidate a requirement, unusual
combinations or transitions, and values that look impossible. Label each *suspicious - explain it*
or *contradicts a confirmed rule*. Record the answer and who gave it.

## Delegated authority

- The executor MAY: <paths, commands, decisions it can make alone>.
- The executor MUST NOT: <weaken, skip or delete protected checks; change requirements; widen scope;
  push, publish or touch shared systems unless listed here>.

## Acceptance and evidence

- Protected checks (the executor may not edit these without renewed agreement): <list>
- Combined validation after parallel steps merge: <command that runs the integrated result>
- Completion evidence recorded in each step's `evidence:` field.

## Escalate when

Contradictory requirements; scope expansion; an action outside delegated authority; a protected check
that cannot pass as written. Bring back the specific decision, not a status report. Failed tests and
unsuccessful approaches inside scope are implementation trouble: diagnose, repair, continue.

## Exceptions and retirements

Do not collapse these into "test retired". Record which one applies:

1. Incorrect test - fix or remove the test.
2. Incorrect or outdated documentation - correct the documentation.
3. Requirement withdrawn - record who withdrew it and why.
4. Valid requirement with a tolerated violation - keep the rule; record rationale, decision owner,
   affected parties, and a review date or trigger (see exception-record.md).
