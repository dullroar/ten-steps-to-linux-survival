---
id: 00-step-template
status: pending
depends_on: []
touches:
  - path/or/glob/this/step/will/change
lane: none
gate: exact command that proves this step complete
requirements: [R1]
evidence: ""
---

# <One-sentence goal>

Write for an agent with no chat history.

## Change

- `path`: the intended change.

## Do not change

- Paths or behavior outside this step, and protected acceptance checks.

## Dependencies already satisfied

- <step id and what it provides>

## Completion criteria

- <observable result>

## Record

Set `status: done` and fill `evidence:` with the gate's outcome (command, result, date). Note any
missing verification instead of omitting it.
