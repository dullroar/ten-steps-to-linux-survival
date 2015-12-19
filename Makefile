BUILD = build
BOOKNAME = TenStepsToLinuxSurvival
TITLE = title.txt
METADATA = metadata.xml
CHAPTERS = metadata.yaml Step-1.md Step00.md Step01.md Step02.md Step03.md Step04.md Step05.md Step06.md Step07.md Step08.md Step09.md Step10.md Appendices.md Colophon.md
SLIDES = Slides-1.md Slides00.md Slides01.md Slides02.md Slides03.md Slides04.md Slides05.md Slides06.md Slides07.md Slides08.md Slides09.md Slides10.md
TOC = --toc --toc-depth=3 -V lof
COVER_IMAGE = images/Merv.jpg
LATEX_CLASS = book
SYNTAX = --no-highlight

all: markdown book slides

book: epub html pdf

clean:
	rm -r $(BUILD)

debug: markdown

epub: $(BUILD)/epub/$(BOOKNAME).epub

html: $(BUILD)/html/$(BOOKNAME).html

pdf: $(BUILD)/pdf/$(BOOKNAME).pdf

slides: revealjs

revealjs: $(BUILD)/slides/revealjs/$(BOOKNAME).html

markdown: $(BUILD)/markdown/$(BOOKNAME).md

$(BUILD)/epub/$(BOOKNAME).epub: $(TITLE) $(CHAPTERS)
	mkdir -p $(BUILD)/epub
	mkdir -p $(BUILD)/epub/images
	cp images/* $(BUILD)/epub/images/.
	pandoc $(TOC) $(SYNTAX) -V toc-title="Table of Contents" -S --epub-metadata=$(METADATA) --epub-cover-image=$(COVER_IMAGE) -o $@ $^
	-~/KindleGen/kindlegen $(BUILD)/epub/$(BOOKNAME).epub

$(BUILD)/html/$(BOOKNAME).html: $(CHAPTERS)
	mkdir -p $(BUILD)/css
	cp css/* $(BUILD)/css/.
	mkdir -p $(BUILD)/html
	mkdir -p $(BUILD)/html/images
	cp images/* $(BUILD)/html/images/.
	pandoc $(TOC) $(SYNTAX) -V css="../css/styles.css" --standalone --to=html5 -o $@ $^

$(BUILD)/markdown/$(BOOKNAME).md: $(CHAPTERS)
	mkdir -p $(BUILD)/markdown
	mkdir -p $(BUILD)/markdown/images
	cp images/* $(BUILD)/markdown/images/.
	pandoc $(TOC) $(SYNTAX) --to=markdown_github -o $@ $^
	cp $(BUILD)/markdown/$(BOOKNAME).md README.md

$(BUILD)/pdf/$(BOOKNAME).pdf: $(TITLE) $(CHAPTERS)
	mkdir -p $(BUILD)/pdf
	pandoc $(TOC) $(SYNTAX) --latex-engine=xelatex --template template.tex -V documentclass=$(LATEX_CLASS) -V fontsize=10pt -V geometry:"margin=1in, paperwidth=7in, paperheight=9in" -V mainfont:"DejaVu Serif" -V sansfont:"DejaVu Sans" -V monofont:"Ubuntu Mono" --to=latex -o $(BUILD)/pdf/$(BOOKNAME).tex $^
	xelatex -output-directory=$(BUILD)/pdf $(BUILD)/pdf/$(BOOKNAME).tex
	makeindex $(BUILD)/pdf/$(BOOKNAME)
	xelatex -output-directory=$(BUILD)/pdf $(BUILD)/pdf/$(BOOKNAME)

$(BUILD)/slides/revealjs/$(BOOKNAME).html: $(SLIDES)
	mkdir -p $(BUILD)/slides
	mkdir -p $(BUILD)/slides/revealjs
	pandoc $(SYNTAX) --to=revealjs --standalone --self-contained -o $@ $^

.PHONY: all book clean epub html pdf
