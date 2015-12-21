.PHONY: all
all:

.PHONY: update-readme
update-readme:
	rm -f ReadMe.md.tmp
	devscripts/update-readme.py ReadMe.md >ReadMe.md.tmp
	mv ReadMe.md.tmp ReadMe.md
