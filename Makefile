BUILD = build
BOOKNAME = TenStepsToLinuxSurvival
TITLE = title.txt
METADATA = metadata.xml
CHAPTERS = metadata.yaml Step-1.md Step00.md Step01.md Step02.md Step03.md Step04.md Step05.md Step06.md Step07.md Step08.md Step09.md Step10.md Appendices.md Colophon.md
TOC = --toc --toc-depth=3
COVER_IMAGE = images/Merv.jpg
LATEX_CLASS = book
SYNTAX = --no-highlight

all: book markdown

book: epub html pdf

clean:
	rm -r $(BUILD)

debug: markdown

epub: $(BUILD)/epub/$(BOOKNAME).epub

html: $(BUILD)/html/$(BOOKNAME).html

pdf: $(BUILD)/pdf/$(BOOKNAME).pdf

markdown: $(BUILD)/markdown/$(BOOKNAME).md

$(BUILD)/epub/$(BOOKNAME).epub: $(TITLE) $(CHAPTERS)
	mkdir -p $(BUILD)/epub
	pandoc $(TOC) $(SYNTAX) -V toc-title="Table of Contents" -S --epub-metadata=$(METADATA) --epub-cover-image=$(COVER_IMAGE) -o $@ $^

$(BUILD)/html/$(BOOKNAME).html: $(CHAPTERS)
	mkdir -p $(BUILD)/html
	mkdir -p $(BUILD)/html/images
	cp images/* $(BUILD)/html/images/.
	pandoc $(TOC) $(SYNTAX) --standalone --to=html5 -o $@ $^

$(BUILD)/pdf/$(BOOKNAME).pdf: $(TITLE) $(CHAPTERS)
	mkdir -p $(BUILD)/pdf
	pandoc $(TOC) $(SYNTAX) --latex-engine=xelatex --template template.tex -V documentclass=$(LATEX_CLASS) -V fontsize=10pt -V geometry:"margin=1in, paperwidth=7in, paperheight=9in" -V monofont:"Ubuntu Mono" -o $@ $^

$(BUILD)/markdown/$(BOOKNAME).md: $(CHAPTERS)
	mkdir -p $(BUILD)/markdown
	mkdir -p $(BUILD)/markdown/images
	cp images/* $(BUILD)/markdown/images/.
	pandoc $(TOC) $(SYNTAX) --to=markdown_github -o $@ $^
	cp $(BUILD)/markdown/$(BOOKNAME).md README.md

.PHONY: all book clean epub html pdf
