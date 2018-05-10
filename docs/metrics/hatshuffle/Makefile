.SUFFIXES:.eps .pdf .gz .data .dot

metrics.pdf:
	python3 memory.py
	python3 protocol.py
	pdflatex hat_shuffle_metrics.tex
	pdflatex files_size.tex
	pdflatex metrics.tex

clean:
	rm -f *.log *.out *.aux *.pdf
