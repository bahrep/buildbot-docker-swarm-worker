[![Build Status](https://img.shields.io/travis/cjolowicz/buildbot-docker-swarm-worker.svg?style=flat-square)](https://travis-ci.org/cjolowicz/buildbot-docker-swarm-worker)
[![Coverage Status](https://img.shields.io/coveralls/cjolowicz/buildbot-docker-swarm-worker.svg?style=flat-square)](https://coveralls.io/github/cjolowicz/buildbot-docker-swarm-worker?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

# buildbot-docker-swarm-worker

Buildbot worker for Docker Swarm

This project has a [changelog](CHANGELOG.md).

## Contents

This package provides a worker plugin for
[buildbot](https://buildbot.net) to deploy buildbot workers on
[Docker Swarm](https://docs.docker.com/engine/swarm/).

## Installation

To install this package,

```sh
pip install buildbot-docker-swarm-worker
```

## Development

Install [pyenv](https://github.com/pyenv/pyenv), and provide
Python 3.6 and 3.7:

```sh
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

pyenv install 3.7.3
pyenv install 3.6.8

pyenv local 3.7.3 3.6.8
```

Install [tox](https://pypi.org/project/tox/) to run the test suite
against different interpreters:

```shell
pip install --user tox
```

Set up a virtualenv:

```sh
make venv
source venv/bin/activate
```

Install the requirements:

```sh
make install
```

When making changes, reformat the source using
[black](https://github.com/ambv/black):

```sh
make black
```

## Testing

The test suite is located under [tests](tests) and uses
[pytest](https://pypi.org/project/pytest/).

Run the test suite in the virtualenv:

```sh
make test
```

Run the test suite using `tox`:

```shell
tox
```

## Requirements

Requirements are declared in the files
[requirements/base.in](requirements/base.in) and
[requirements/dev.in](requirements/dev.in).

Requirements are pinned to specific versions in the files
[requirements/base.txt](requirements/base.txt) and
[requirements/dev.txt](requirements/dev.txt). These files are
generated using the following command:

```sh
make requirements
```

To force an upgrade of all requirements, invoke the following command:

```sh
make -B requirements
```

## Releasing

This project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) and
[PEP 440](https://www.python.org/dev/peps/pep-0440).

The [bumpversion](https://pypi.org/project/bumpversion/) tool is used
to update the version number and add a Git tag to the repository.

1. Run `make test`.
2. Update [CHANGELOG.md](CHANGELOG.md).
3. Bump version.
4. Push to Github.

## Continuous Integration

Continuous integration is provided by
[Travis CI](https://travis-ci.org). The Travis CI job runs the test
suite.
