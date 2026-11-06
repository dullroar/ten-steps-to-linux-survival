# Scripts

Deterministic automation. Reuse these before writing new tooling.

* [check_context.py](./check_context.py). Read when: you changed any context file (AGENTS.md, docs, memory, plans); runs every check below.
* [build_context_indexes.py](./build_context_indexes.py). Read when: you added or re-gisted a routed Markdown file; regenerates README indexes (`--check` verifies only).
* [check_plan.py](./check_plan.py). Read when: you created or changed a plan or step; validates dependencies, write-scope overlap, traceability and prints derived status.
* [check_links.py](./check_links.py). Read when: you moved or renamed a Markdown file; verifies local links and anchors.
* [scan_context_secrets.py](./scan_context_secrets.py). Read when: you added examples, logs or paths to context files; flags credentials and personal paths.
* [ctx_common.py](./ctx_common.py). Read when: editing the context scripts; shared front-matter parsing and file discovery.
