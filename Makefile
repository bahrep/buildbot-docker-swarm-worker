.PHONY: all
all:

requirements/%.txt: requirements/%.in
	pip install pip-tools
	python -m piptools compile \
	    --verbose \
	    --upgrade \
	    --generate-hashes \
	    --output-file=$@ $<

.PHONY: requirements
requirements: requirements/base.txt requirements/dev.txt

.PHONY: install
install:
	pip install -e .[dev]

.PHONY: black
black:
	black src tests setup.py

.PHONY: test
test:
	flake8 src tests setup.py
	py.test tests --cov=buildbot_docker_swarm_worker --cov-report=term-missing

.PHONY: clean
clean:
	for dir in src tests ; \
	do \
	    find "$$dir" \
	        -name '*.pyc' -print0 -or \
	        -name '__pycache__' -print0 -or \
	        -false | xargs -0 rm -vrf ; \
	done ; \
	rm -vrf .pytest_cache

.PHONY: distclean
distclean:
	git clean -fxd

.PHONY: travis-install
travis-install: install

.PHONY: travis-script
travis-script: test
	coveralls
