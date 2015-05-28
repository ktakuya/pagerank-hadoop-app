.PHONY: test data

convert: src/convert
	python src/convert/convert.py -p -pl

data:
	mkdir data && \
		wget http://dumps.wikimedia.org/jawiki/20150512/jawiki-20150512-page.sql.gz -P data/ && \
		wget http://dumps.wikimedia.org/jawiki/20150512/jawiki-20150512-pagelinks.sql.gz -P data/ && \
		gunzip data/jawiki-20150512-page.sql.gz && \
		gunzip data/jawiki-20150512-pagelinks.sql.gz

test:
	cd test && \
	sh test.sh
