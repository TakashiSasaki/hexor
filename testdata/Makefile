all: bin1.md5 bin2.md5 bin3.md5

bin1:
	openssl rand -out bin1 1000

bin2:
	openssl rand -out bin2 1000

bin3:
	openssl rand -out bin3 1000

%.md5: %
	md5sum $< >$@

