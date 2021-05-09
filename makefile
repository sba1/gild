.PHONY: all
all:

.PHONY: update-readme
update-readme:
	rm -f ReadMe.md.tmp
	devscripts/update-readme.py ReadMe.md >ReadMe.md.tmp
	mv ReadMe.md.tmp ReadMe.md

.PHONY: type-check
type-check:
	cd bin && mypy --disallow-untyped-defs --ignore-missing-imports --py2 *.py

# Target for setting up the CI environment
.PHONY: ci-setup
ci-setup:
	sudo python3 -m pip install -U mypy
