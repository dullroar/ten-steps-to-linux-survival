# Agent contract

An authored Linux/Bash learning book built with Pandoc into Markdown, HTML, EPUB, PDF and Beamer. README.md is generated; chapter files and the Makefile are the source.

## Load context in this order

1. Read this file.
2. Read the short indexes in full: `README.md`, `docs/README.md`, `memory/README.md`, `scripts/README.md`.
3. Match the task against each index's **Read when** entries and open only matching documents.
4. For a large file, search its headings and read only the relevant ranges.
5. Stop loading when the decision, intended files, constraints and validation method are known.

User instructions take precedence over repository guidance. When sources conflict, prefer: user
instruction, this file, `docs/design/`, the named plan, domain documentation and references,
`memory/`, implementation and tests, historical notes.

## Context ownership

- Universal rules belong here.
- Architectural reasons belong in `docs/design/` (one premise per file).
- Non-obvious findings that cost time to discover belong in `memory/` (one topic per file; edit the existing topic, do not append a rival).
- Execution state belongs in `plans/`; deterministic automation in `scripts/`.
- Every routed Markdown file starts with `gist: "Read when: ..."` front matter. Do not hand-edit the generated section of an index; run `python scripts/build_context_indexes.py`.

Do not duplicate a fact across layers. Correct its canonical source.

## Planned work (spec-driven)

- Work only on a named plan in `plans/<plan>/` (`spec.md` plus `steps/`) or an explicitly identified off-plan task. Copy `plans/TEMPLATE/` to start one.
- Once its spec is approved, proceed through the steps without asking permission for routine work. Failed tests and dead ends inside scope: diagnose, repair, continue. Return to the user only for a new decision: contradictory requirements, scope expansion, or an action outside the spec's delegated authority.
- Acceptance checks named in the spec are protected. Never weaken, skip or delete one to get green; if one cannot pass as written, escalate.
- Parallel steps must have no dependency between them and no overlapping `touches`; if independence is uncertain, serialize. After parallel steps merge, run the spec's combined validation.
- A step is done only with recorded evidence. Report unavailable verification honestly.
- Retiring a rule, correcting documentation, and tolerating a known violation are different outcomes; record which one (see `plans/TEMPLATE/spec.md`).

## Validation

Run the smallest check that proves the change, then `python scripts/check_context.py` for any change to context files.

## Safety

Do not commit credentials, personal data, personal filesystem paths or sensitive record-level examples. Use placeholders and aggregate evidence. Do not push, publish, force-push or add a remote without authorization.
