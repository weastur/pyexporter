# Contributing Guidelines

I appreciate any contributions you make! Every bit helps, and I’ll always give credit.

## How You Can Contribute

- Report bugs
- Fix bugs
- Suggest features
- Implement features
- Improve documentation
- Join discussions
- Share the project
- Show support (thanks/donations)

## Development

### Getting Started

Clone the repository and install dependencies:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [pre-commit](https://pre-commit.com/#install)
- [docker](https://docs.docker.com/get-docker/)
- [shellcheck](https://github.com/koalaman/shellcheck?tab=readme-ov-file#installing)

Bootstrap the development environment:

```shell
make bootstrap
```

This will install and run pre-commit hooks, Python, create a virtual
environment, install dependencies inside it, build the app (including the Docker
image), and run tests. If everything is fine, you can start the app with:

```shell
uv run py-exporter
```

P.S. Although `uv` has a great ability to run anything from inside the `.venv` by
using `uv run`, you may find it useful to activate the virtual environment
manually:

```shell
source .venv/bin/activate
```

### Tests

Tests are written with [pytest](https://docs.pytest.org/en/stable/). Some tests might run with [testcontainers](https://github.com/testcontainers/testcontainers-python).
You can run tests with:

```shell
make test
```

### Build

You can build the app with:

```shell
make build
```

A Dockerized app will be built and tagged as `py-exporter:latest` and `py-exporter:${version}`

```shell
make docker-build
```

### Docs

Documentation is written in markdown and located in the `docs` directory. You can preview it by running:

```shell
make docs-dev
```

You may also want to consult with the [mkdocs](https://www.mkdocs.org/) and [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) documentation.

### Examples

If a new feature or breaking change is introduced, please update the examples in the `examples` directory.

## Rules

The only rule is to keep the code, tests, documentation, build scripts, and
examples in sync. If you change something in the code, please update the other
relevant files accordingly.

## FAQ

### Why is this project written in Python? Will it be rewritten in Golang, as it’s a more common language for exporters?

I chose Python because it's the language I am most comfortable with. From time
to time, I have to use Golang, and I have a dozen arguments against using it
when I have a choice, but this isn't the right place to discuss these. In other
words, I’m not planning to rewrite it in Golang. If you experience any issues
with Python, please open an issue, and we’ll try to resolve it.

### I have an issue with the Windows/Linux development environment. Can you help me?

I'm not a Windows user at all. I use Linux on my servers only, not on my laptop.
Still, please open an issue and describe your problem; I'll try to help.

### What about building a [zipapp](https://docs.python.org/3/library/zipapp.html)?

I'm not sure about the benefits of using zipapp. If you have a good reason to
use it, please open an issue and describe it. Moreover, zipapp has some
limitations, especially with dependencies that include C extensions. There is a
Docker image with the `py-exporter` app, so you can use it without installing any
dependencies. You can consult the examples in this repository to see how to
install on the target machine without containers.
