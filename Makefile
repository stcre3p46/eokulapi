.DEFAULT_GOAL := package

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: depend

depend: ## Install requirements
	@pip install -r requirements.txt
	@pip install build
	@pip install black

.PHONY: install

install: package ## build and install module to system
	@pip install dist/*.whl --force-reinstall
	#@pip install -e . --user

.PHONY: package

package: clean test format## Create package
	@python3 -m build


.PHONY: format

format: ## Format code
	@python3 -m black . -l 100

.PHONY: test

test: clean ## Do testing
	@python3 ./tests/test.py

.PHONY: clean

clean: ## Remove build and cache files
	@rm -rfv **/*.egg-info 2>/dev/null
	@rm -rfv build 2>/dev/null
	@rm -rfv dist 2>/dev/null
	@rm -rfv .pytest_cache 2>/dev/null
	@rm -rfv **/__pycache__ 2>/dev/null
