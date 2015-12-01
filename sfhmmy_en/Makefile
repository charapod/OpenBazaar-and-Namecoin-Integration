NAME=crypto
SUBMITNAME="crypto"
LATEXFLAGS=-halt-on-error --shell-escape
INCLUDEFILES=

.PHONY: all backup clean create distclean submit

all: create

$(NAME).pdf: create

backup: $(NAME).pdf
	mv -f $(NAME).pdf $(NAME).old.pdf

clean: backup
	rm -f $(NAME).aux $(NAME).blg $(NAME).log $(NAME).out $(NAME).pyg $(NAME).pdf

create: $(NAME).tex $(INCLUDEFILES)
	pdflatex $(LATEXFLAGS) $^

distclean:
	rm -f $(NAME).aux $(NAME).bbl $(NAME).blg $(NAME).log $(NAME).out $(NAME).pyg $(NAME).pdf $(NAME).old.pdf

fix: $(NAME).tex $(INCLUDEFILES)
	pdflatex $(LATEXFLAGS) $^
	rm -f $(NAME).aux $(NAME).blg $(NAME).log $(NAME).out $(NAME).pyg

submit: $(NAME).pdf
	cp $(NAME).pdf $(SUBMITNAME).pdf
