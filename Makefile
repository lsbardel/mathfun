
.PHONY: help cloc install lint

help:
	@echo ======================== METACORE ====================================================
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
	@echo ======================================================================================


cloc:			## Count lines of code
	cloc --exclude-dir=venv .


install:		## install python dependencies in venv
	@pip install -U pip
	@pip install -U -r ./requirements.txt


lint: 		## run linters
	isort .
	black codility extra hackerrank mathfun tests
	flake8
