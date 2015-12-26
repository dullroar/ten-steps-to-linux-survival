BUILD = build
BOOKNAME = TenStepsToLinuxSurvival
SLIDESNAME = TenStepsToLinuxSurvivalSlides
CHAPTERS = metadata.yaml Step-1.md Step00.md Step01.md Step02.md Step03.md Step04.md Step05.md Step06.md Step07.md Step08.md Step09.md Step10.md Appendices.md Colophon.md
SLIDES = metadata.yaml Slides-1.md Slides00.md Slides01.md Slides02.md Slides03.md Slides04.md Slides05.md Slides06.md Slides07.md Slides08.md Slides09.md Slides10.md
TOC = --toc --toc-depth=3 --standalone -V lof -V toc-title="Table of Contents"
COVER_IMAGE = images/Merv.jpg
LATEX_CLASS = book
SYNTAX = --no-highlight

all: markdown book slides

book: epub html pdf markdown

clean:
	rm -r $(BUILD)

debug: markdown

epub: $(BUILD)/epub/$(BOOKNAME).epub

html: $(BUILD)/html/$(BOOKNAME).html

pdf: $(BUILD)/pdf/$(BOOKNAME).pdf

slides: beamer

beamer: $(BUILD)/slides/beamer/$(SLIDESNAME).pdf

markdown: $(BUILD)/markdown/$(BOOKNAME).md

$(BUILD)/epub/$(BOOKNAME).epub: $(CHAPTERS)
	mkdir -p $(BUILD)/epub
	mkdir -p $(BUILD)/epub/images
	cp images/* $(BUILD)/epub/images/.
	pandoc $(TOC) $(SYNTAX) --epub-cover-image=$(COVER_IMAGE) -o $@ $^
	-~/KindleGen/kindlegen $(BUILD)/epub/$(BOOKNAME).epub

$(BUILD)/html/$(BOOKNAME).html: $(CHAPTERS)
	mkdir -p $(BUILD)/css
	cp css/* $(BUILD)/css/.
	mkdir -p $(BUILD)/html
	mkdir -p $(BUILD)/html/images
	cp images/* $(BUILD)/html/images/.
	pandoc $(TOC) $(SYNTAX) -V css="../css/styles.css" --number-offset=-2 --to=html5 -o $@ $^

$(BUILD)/markdown/$(BOOKNAME).md: $(CHAPTERS)
	mkdir -p $(BUILD)/markdown
	mkdir -p $(BUILD)/markdown/images
	cp images/* $(BUILD)/markdown/images/.
	pandoc $(TOC) $(SYNTAX) --standalone --to=markdown_github -o $@ $^
	cp $(BUILD)/markdown/$(BOOKNAME).md README.md

$(BUILD)/pdf/$(BOOKNAME).pdf: $(CHAPTERS)
	mkdir -p $(BUILD)/pdf
	pandoc $(TOC) --highlight-style="tango" --latex-engine=xelatex -H header.tex -B before.tex -A after.tex --no-tex-ligatures -V linkcolor=black -V toccolor=black -V urlcolor=black -V citecolor=black -V hidelinks=true -V links-as-notes=true -V documentclass=$(LATEX_CLASS) -V fontsize=10pt -V geometry:"margin=1in, paperwidth=7in, paperheight=9in" -V mainfont="DejaVu Serif" -V sansfont="DejaVu Sans" -V monofont="Ubuntu Mono" --to=latex -o $(BUILD)/pdf/$(BOOKNAME).tex $^
	xelatex -output-directory=$(BUILD)/pdf $(BUILD)/pdf/$(BOOKNAME).tex
	makeindex $(BUILD)/pdf/$(BOOKNAME)
	xelatex -output-directory=$(BUILD)/pdf $(BUILD)/pdf/$(BOOKNAME)

$(BUILD)/slides/beamer/$(SLIDESNAME).pdf: $(SLIDES)
	mkdir -p $(BUILD)/slides
	mkdir -p $(BUILD)/slides/beamer
	pandoc $(SYNTAX) -V theme=Hannover --to=beamer --latex-engine=xelatex -V classoption="aspectratio=169" -V mainfont="DejaVu Serif" -V sansfont="DejaVu Sans" -V monofont="Ubuntu Mono" --standalone --self-contained -o $@ $^

.PHONY: all book clean epub html pdf
