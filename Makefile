
all: zip

zip:
	tar -zcvf data.tar.gz data/

scp:
	scp root@duckyocean:/root/python-dep/data.tar.gz .