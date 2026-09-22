# MEMORY.md

Non-obvious findings about this codebase and its operating environment, discovered during work but not designed for anywhere else — not in README.md (what it is and how to use it), DESIGN.md (architectural decisions), or agent-instruction files (rules). This is background context for whichever LLM works in this repository next, so it does not have to rediscover these findings the hard way.

If you (an LLM) make a finding like the ones below — a gotcha, an environment quirk, or a non-obvious reason one component reads or uses another — add it here rather than only mentioning it in chat. Keep entries factual and dated; note when something might have been fixed since.

## Findings

- 2015-12-24 (may be stale — recheck against current pandoc/xelatex versions) — `header.tex` redefines pandoc's syntax-highlighting token macros (`\KeywordTok`, `\StringTok`, `\CommentTok`, etc.) to plain `{#1}` (commit 9faa9b5). This was needed to get a shaded background on PDF code blocks to render at all with the Makefile's `pandoc --highlight-style="tango" ... -H header.tex`; without it, and without a language tag on the Markdown fence (```` ```bash ```` rather than a bare ```` ``` ````), code blocks didn't pick up shading in the PDF build. If PDF code-block shading looks wrong after a pandoc/xelatex upgrade, check `header.tex`'s token-macro overrides before assuming the Makefile's `--highlight-style` flag is the problem.
