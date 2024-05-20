POETRY ?= poetry run
MIN_TEST_COVERAGE ?= 80

#####################
# Build commands #
#####################

check-prereqs:
	@echo "=> Checking for pre-requisites"
	@if ! poetry --version; then echo "=> Poetry isn't installed" && exit 1; fi
	@echo "=> All pre-requisites satisfied"

install: check-prereqs
	@echo "=> Installing python dependencies"
	poetry install

setup: install lint test-audit
	poetry run pre-commit install

##########################
# Formatting and linting #
##########################

format: ## runs code formatting
	@echo "=> Running code formatting"
	@echo "============================="
	$(POETRY) black src tests
	$(POETRY) ruff check --fix src tests
	@echo "============================="
	@echo "=> Code formatting complete"

format-check: ## runs code formatting checks
	@echo "=> Running code formatting checks"
	@echo "============================="
	$(POETRY) black --check src tests
	$(POETRY) ruff check --exit-non-zero-on-fix src tests
	@echo "============================="
	@echo "=> All formatting checks succeeded"

lint: format-check
	@echo "============================="
	@echo "=> Running linters"
	@echo "============================="
	$(POETRY) pylint src tests
	$(POETRY) mypy src
	@echo "============================="
	@echo "=> All linters succeeded"

#################
# Test commands #
#################

unit-test:
	@echo "=> Running unit tests"
	@echo "===================================="
	$(POETRY) pytest --cov=src

test-audit: unit-test
	@echo "=> Running test coverage report"
	@echo "===================================="
	$(POETRY) coverage report --show-missing --fail-under=$(MIN_TEST_COVERAGE)
