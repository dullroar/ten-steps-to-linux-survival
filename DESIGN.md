# DESIGN.md

# Ten Steps to Linux Survival Build Design

## Boundary

This repository is an authored Linux/Bash learning book with multiple distributable forms. README.md is the generated, standalone Markdown edition for readers; the modular chapter files and Makefile are the editing and publishing source.

## Core decisions

- Keep chapters, appendices, and colophon as separate Markdown inputs so the book and slide deck can share structure while remaining editable in parts.
- Use Pandoc to produce Markdown, HTML, EPUB, PDF, and Beamer outputs from the same source set.
- Regenerate README.md from the book’s Markdown target. Do not hand-edit README.md for repository documentation changes because the build will overwrite it.
- Keep presentation inputs separate from book chapters where slide pacing and format need different treatment.

## Constraints

The repository favors portable Markdown source and reproducible document builds over a web application or custom publishing framework. Changes to content structure should be made in source chapters and the Makefile, then regenerated.


