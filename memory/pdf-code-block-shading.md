---
gist: "Read when: PDF code blocks lose shading or highlighting after a pandoc or xelatex upgrade, or header.tex is edited."
---

# PDF code-block shading depends on header.tex

- 2015-12-24 (may be stale; recheck against current pandoc/xelatex versions) - `header.tex` redefines pandoc's syntax-highlighting token macros (`\KeywordTok`, `\StringTok`, `\CommentTok`, etc.) to plain `{#1}` (commit 9faa9b5). This was needed for a shaded background on PDF code blocks to render with the Makefile's `pandoc --highlight-style="tango" ... -H header.tex`; without it, and without a language tag on the fence (```` ```bash ```` rather than a bare fence), code blocks did not pick up shading in the PDF build. If shading looks wrong after an upgrade, check `header.tex`'s token-macro overrides before assuming the `--highlight-style` flag is the problem.
