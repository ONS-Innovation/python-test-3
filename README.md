# python-test-3

[![Build Status](https://github.com/ONS-Innovation/python-test-3/actions/workflows/ci.yml/badge.svg)](https://github.com/ONS-Innovation/python-test-3/actions/workflows/ci.yml)
[![Build Status](https://github.com/ONS-Innovation/python-test-3/actions/workflows/security-scan.yml/badge.svg)](https://github.com/ONS-Innovation/python-test-3/actions/workflows/security-scan.yml)
[![Build Status](https://github.com/ONS-Innovation/python-test-3/actions/workflows/codeql.yml/badge.svg)](https://github.com/ONS-Innovation/python-test-3/actions/workflows/codeql.yml)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![poetry-managed](https://img.shields.io/badge/poetry-managed-blue)](https://python-poetry.org/)
[![License - MIT](https://img.shields.io/badge/licence%20-MIT-1ac403.svg)](https://github.com/ONS-Innovation/python-test-3/blob/main/LICENSE)

python-test-3

**IMPORTANT**: This README was generated from a template.
Please update it with specific information about your project, including:

> - Detailed project description and purpose
> - Specific installation requirements
> - Usage examples and API documentation
> - Contributing guidelines specific to your project
> - Any project-specific compliance requirements

---

## Table of Contents

[//]: # (:TODO: Enable link checking once https://github.com/tcort/markdown-link-check/issues/250 is resolved.)
<!-- markdown-link-check-disable -->
- [Getting Started](#getting-started)
    - [Pre-requisites](#pre-requisites)
    - [Installation](#installation)
- [Development](#development)
    - [Run Tests with Coverage](#run-tests-with-coverage)
    - [Linting and Formatting](#linting-and-formatting)
    - [Security Scanning](#security-scanning)
- [Contributing](#contributing)
- [License](#license)
<!-- markdown-link-check-enable -->

## Getting Started

To get a local copy up and running, follow these simple steps.

### Pre-requisites

Ensure you have the following installed:

1. **Python**: Version specified in `.python-version`.
2. **[Poetry](https://python-poetry.org/)**: This is used to manage package dependencies and virtual
   environments.
3. **Operation System**: MacOS

### Installation

1. Clone the repository and install the required dependencies.

```bash
git clone https://github.com/ONS-Innovation/python-test-3.git
```

2. Install dependencies

[Poetry](https://python-poetry.org/) is used to manage dependencies in this project. For more information, read
the [Poetry documentation](https://python-poetry.org/).

To install all dependencies, including development dependencies, run:

```bash
make install-dev
```

To install only production dependencies, run:

```bash
make install
   ```

3. Run the application

```bash
make run
```

## Development

Get started with development by running the following commands.
Before proceeding, make sure you have the development dependencies installed using the `make install-dev` command.

A Makefile is provided to simplify common development tasks. To view all available commands, run:

```bash
make
```

### Run Tests with Coverage

The unit tests are written using the [pytest](https://docs.pytest.org/en/stable/) framework. To run the tests and check
coverage, run:

```bash
make test
```

### Linting and Formatting

[Ruff](https://github.com/astral-sh/ruff) is used for both linting and formatting of the Python code in this project.
Ruff is a fast Python linter and formatter that replaces multiple tools with a single, efficient solution.

The tool is configured using the `pyproject.toml` file.

To lint the Python code, run:

```bash
make lint
```

To auto-format the Python code and correct fixable linting issues, run:

```bash
make format
```

### Security Scanning

[Bandit](https://bandit.readthedocs.io/en/latest/) is used for security scanning of the Python code.
It helps identify common security issues in Python applications.

To run the security scan, run:

```bash
make security-scan
```

#### Pre-commit Hooks

The project includes pre-commit hooks to automatically run linting, formatting, and security checks before each commit.

1. Install **pre-commit** using your selected package manager:


```bash
poetry add --group dev pre-commit
```


2. Activate the git hooks:

```bash
pre-commit install
```

From now on Ruff and Bandit will run automatically on the files you stage before every commit.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

See [LICENSE](LICENSE) for details.
