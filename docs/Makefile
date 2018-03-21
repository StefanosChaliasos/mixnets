.SUFFIXES:.eps .pdf .gz .data .dot

mimicry.pdf: mixnets.tex mixnets.bib
	pdflatex -shell-escape mixnets
	bibtex mixnets
	pdflatex -shell-escape mixnets
	pdflatex -shell-escape mixnets

clean:
	rm -f mixnets.aux mixnets.bbl mixnets.blg mixnets.log mixnets.pdf *.log
	rm -r _minted-mixnets
	rm -fr metrics/*.pdf
