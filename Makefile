# COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

TARGET_MAX_CHAR_NUM=20

## Show help
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

## Install requirements via pipenv
install:
	pipenv install

## Start virtual environment with pipenv
env:
	pipenv shell

## Run tests through pytest
run_tests:
	[ -z "$(VIRTUAL_ENV)" ] && pipenv run pytest || pytest

## Lint with flake8 [add `files` for specific folder/file]
lint:
	[[ -z "$(VIRTUAL_ENV)" ]] && pipenv run flake8 $(files) || flake8 $(files)

## Fix with yapf [add `files` for specific folder/file]
lint-fix:
	[ -z "$(VIRTUAL_ENV)" ] && pipenv run yapf -ir $(files) || yapf -ir $(files)
