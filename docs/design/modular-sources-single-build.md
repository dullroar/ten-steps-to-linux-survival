---
gist: "Read when: editing chapters or the Makefile, adding an output format, or about to hand-edit README.md."
---

# Modular Markdown sources, one Pandoc build

**Decision.** Chapters, appendices, and colophon are separate Markdown inputs so the book and slide deck share structure while staying editable in parts. Pandoc produces Markdown, HTML, EPUB, PDF, and Beamer from the same source set. Presentation inputs stay separate from book chapters where slide pacing needs different treatment.

**Generated file.** README.md is regenerated from the book's Markdown target. Do not hand-edit it for documentation changes; change source chapters and the Makefile, then regenerate.

**Boundary.** Portable Markdown source and reproducible builds, not a web application or custom publishing framework.
