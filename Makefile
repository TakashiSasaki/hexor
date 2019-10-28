test:
	$(MAKE) -C testdata
	./hexor.py testdata/bin1.md5 testdata/bin2.md5 testdata/bin3.md5
