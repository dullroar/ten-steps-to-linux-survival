BUILD = build
BOOKNAME = TenStepsToLinuxSurvival
TITLE = title.txt
METADATA = metadata.xml
CHAPTERS = metadata.yaml Step-1.md Step00.md Step01.md Step02.md Step03.md Step04.md Step05.md Step06.md Step07.md Step08.md Step09.md Step10.md Appendices.md Colophon.md
TOC = --toc --toc-depth=3
COVER_IMAGE = images/Merv.jpg
LATEX_CLASS = report

all: book

book: epub html pdf

clean:
	rm -r $(BUILD)

epub: $(BUILD)/epub/$(BOOKNAME).epub

html: $(BUILD)/html/$(BOOKNAME).html

pdf: $(BUILD)/pdf/$(BOOKNAME).pdf

$(BUILD)/epub/$(BOOKNAME).epub: $(TITLE) $(CHAPTERS)
	mkdir -p $(BUILD)/epub
	pandoc $(TOC) -S --epub-metadata=$(METADATA) --epub-cover-image=$(COVER_IMAGE) -o $@ $^

$(BUILD)/html/$(BOOKNAME).html: $(CHAPTERS)
	mkdir -p $(BUILD)/html
	mkdir -p $(BUILD)/html/images
	cp images/* $(BUILD)/html/images/.
	pandoc $(TOC) --standalone --to=html5 -o $@ $^

$(BUILD)/pdf/$(BOOKNAME).pdf: $(TITLE) $(CHAPTERS)
	mkdir -p $(BUILD)/pdf
	pandoc $(TOC) --latex-engine=pdflatex -V documentclass=$(LATEX_CLASS) -o $@ $^

.PHONY: all book clean epub html pdf
