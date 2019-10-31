test:
	$(MAKE) -C testdata
	./hexor.py -h testdata/bin1.md5 testdata/bin2.md5 testdata/bin3.md5
	./hexor.py testdata/bin1.md5 testdata/bin2.md5 testdata/bin3.md5
	./hexor.py -j testdata/bin1.md5 testdata/bin2.md5 testdata/bin3.md5

ntpdate:
	ntpdate ntp.nict.jp
