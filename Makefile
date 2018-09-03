install:
	pipenv install

env:
	pipenv shell

run_tests:
	[ -z "$(VIRTUAL_ENV)" ] && pipenv run pytest || pytest

lint:
	[[ -z "$(VIRTUAL_ENV)" ]] && pipenv run flake8 $(files) || flake8 $(files)

lint-fix:
	[ -z "$(VIRTUAL_ENV)" ] && pipenv run yapf -ir $(files) || yapf -ir $(files)
