help: ## Show this help
	@egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install-pre-commit: ## Install pre-commit hooks
	pre-commit install

test: ## Run pytest and report coverage
	pytest --cov-report term-missing --cov=eboekhouden_python

.PHONY: help init test
