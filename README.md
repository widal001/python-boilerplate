# Python Boilerplate

<details open="open">
<summary>Table of Contents</summary>

<!-- TOC -->

- [About this Project](#about-this-project)
  - [Made With](#made-with)
  - [Relevant Documents](#relevant-documents)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [This Template](#this-template)
  - [{Use Case 1}](#use-case-1)
- [Vision and Roadmap](#vision-and-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Maintainers](#maintainers)
- [Acknowledgements](#acknowledgements)

<!-- /TOC -->

</details>

## About this Project

<!-- TODO: Replace with a brief description of your own project -->

Python Boilerplate provides a common file structure for a Python project and encourages best practices in python development, including some simple code quality checks set up and some idiomatic examples of python data strctures and functions. This project is a template that can be used as a foundation for future projects.

### Made With

<!-- TODO: Replace this list with your most critical dependencies -->

- [poetry](https://python-poetry.org/) - Dependency management library that makes creating and installing packages more streamlined.
- [tox](https://tox.readthedocs.io/en/latest/) - Automates and standardizes the creation of testing environments.
- [pytest](https://docs.pytest.org/en/6.2.x/) - Simplifies the design and execution of both unit and integration testing.
- [black](https://black.readthedocs.io/en/stable/) - Autoformats code for consistent styling.
- [flake8](https://flake8.pycqa.org/en/latest/) - Checks that code complies with PEP8 style guidelines.
- [pylint](https://www.pylint.org/) - Checks that code follows idiomatic best practices for Python.
- [pre-commit](https://pre-commit.com/) - Runs code quality checks before code is committed.

### Relevant Documents

- [Architecture Decision Records](docs/adrs)
- [Project Scoping Document](docs/project-scope.md)
- [Data Dictionary](docs/data-dictionary.md)
- ... <!-- other relevant documents should be added to the docs/ directory and linked here -->

## Getting Started

### Prerequisites

- Python installed on your local machine, a version between 3.7 and 3.9
- Poetry installed on your local machine

In order to check that you have both Python and Poetry installed, run the following in your command line, and the output should look something like this:

> **NOTE**: in all of the code blocks below, lines preceded with $ indicate commands you should enter in your command line (excluding the $ itself), while lines preceded with > indicate the expected output from the previous command.

```
$ python --version && poetry --version
> Python 3.9.0
> Poetry version 1.1.6
```

**TROUBLESHOOTING:** If you receive an error message, or the version of python you have installed is not between 3.7 and 3.9, consider using a tool like [pyenv](https://github.com/pyenv/pyenv) (on Mac/Linux) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) (on Windows) to manage multiple python installations.

If you have python installed but not poetry, follow these installation instructions:

- [Global install on Mac/Linux](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)
- [Global install on Windows](https://python-poetry.org/docs/#windows-powershell-install-instructions)
- Local install inside a virtual environment using `pip` **NOTE:** This is not recommended because of potential package conflicts:
  - Create a virtual environment: `python -m venv env`
  - Acvitate the virtual environment. **NOTE:** This virtual environment must be active any time you are working with this project:
    - Mac/Linux: `source env/bin/activate`
    - Windows: `env\Scripts\activate`
  - Install poetry: `pip install poetry`

### Installation

1. [Clone the repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) on your local machine: `git clone https://github.com/widal001/python-boilerplate.git`
1. Change directory into the cloned project: `cd python-boilerplate`
1. Install the package: `poetry install`
1. Install `pre-commit` to autoformat your code: `poetry run pre-commit install`
1. Execute all tests: `poetry run tox`
1. All tests should pass with an output that ends in something like this:
   ```
    py39: commands succeeded
    lint: commands succeeded
    checkdeps: commands succeeded
    pytest: commands succeeded
    coverage: commands succeeded
    congratulations :)
   ```

## Usage

### This Template

<!-- TODO: Remove this section after following the steps below -->

When using this boilerplate code as a template for your own project, follow the steps below:

1. Complete all of the `TODO` items listed as comments in this README
1. Pick a new name for your package, then replace the word `boilerplate` with that new name in the following places:
   - `pyproject.toml`
   - `tox.ini`
   - `src/boilerplate/` and all files within that directory
   - `tests/` and all of the files within that directory
1. All new python code should be added either as a single module or collection of modules under the `src/{your_package_name}/` directory. For reference:
   ```
   pyproject.toml
   src/
     your_package_name/
       main.py
       your_new_module_1.py
       your_new_module_2/
          your_new_module_2_1.py
          your_new_module_2_2.py
   tests/
   ```
1. If the new code requires a package that is not already installed, add it to the project by using `poetry add <package_name>`
1. If you make any manual changes to the `pyproject.toml` file make sure you run: `poetry lock && poetry install`
1. Each new method or function you write needs to be accompanied by a test which calls that method or function.  These unit and/or integration tests should be added to the `tests/` directory using a file structure that mirrors the modules you are contributing to. For reference:
   ```
   tests/
     conftest.py
     test_main.py
     test_your_new_module_1.py
     your_new_module_2/
        test_your_new_module_2_1.py
        test_your_new_module_2_2.py

   ```
   > **NOTE**
   >
   > - CI/CD checks will only pass if more than 90% of the code base is executed by the tests
   > - Pytest requires the following naming conventions for [test discovery](https://docs.pytest.org/en/reorganize-docs/new-docs/user/naming_conventions.html)


### {Use Case 1}

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->

## Vision and Roadmap

The vision for this template is to simplify the process of creating open source python projects with high quality codebase and mechanisms that promote smart and collaborative project governance. This project aims to fulfill this vision by:

- Adopting a common python package file structure
- Implementing basic linting and code quality checks
- Reinforcing compliance with those code quality checks using CI/CD
- Providing templates for things like documentation, issues, and pull requests
- Offering pythonic implementation examples of common data structures and scripting tasks like:
  - Creating classes, methods, and functions
  - Setting up unit and integration testing
  - Reading and writing to files

For a more detailed breakdown of the feature roadmap and other development priorities please reference the following links:

- [Feature Roadmap](https://github.com/widal001/python-boilerplate/projects/1)
- [Architecture Decisions](https://github.com/widal001/python-boilerplate/projects/2)
- [Bug Fixes](https://github.com/widal001/python-boilerplate/projects/3)
- [All Issues](https://github.com/widal001/python-boilerplate/issues)

## Contributing

<!-- TODO: Update this section as well as CONTRIBUTING.md to reflect your contributing guidelines -->

Contributions are always welcome! We encourage contributions in the form of discussion on issues in this repo and pull requests for improvements to documentation and code.

See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to get started.

## License

<!-- TODO: Update this section as well as LICENSE to reflect the license of your project -->

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Maintainers

- [@widal001](https://github.com/widal001)

## Acknowledgements

- [Python Packaging Authority Sample Project](https://github.com/pypa/sampleproject)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)
