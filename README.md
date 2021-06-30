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
  - [Your Package](#your-package)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

<!-- /TOC -->

</details>

## About this Project

<!-- TODO: Replace with a brief description of your own project -->

Python Boilerplate provides a common file structure for a Python project and encourages best practices in python development, including some simple code quality checks set up and some idiomatic examples of python data strctures and functions. This project is a template that can be used as a foundation for future projects.

### Made With

<!-- TODO: Replace this list with your most critical dependencies -->

- [tox](https://tox.readthedocs.io/en/latest/) - Automates and standardizes the creation of testing environments.
- [pytest](https://docs.pytest.org/en/6.2.x/) - Simplifies the design and execution of both unit and integration testing.
- [black](https://black.readthedocs.io/en/stable/) - Autoformats code for consistent styling.
- [flake8](https://flake8.pycqa.org/en/latest/) - Checks that code complies with PEP8 style guidelines.
- [pylint](https://www.pylint.org/) - Checks that code follows idiomatic best practices for Python.
- [pre-commit](https://pre-commit.com/) - Runs code quality checks before code is committed.

### Relevant Documents

- [Architecture Decision Records](docs/decisions): Directory of all of the architectural decisions made within the project.
- [Project Scoping Document](docs/project-scope.md)
- [Data Dictionary](docs/data-dictionary.md)
- ... <!-- other relevant documents should be added to the docs/ directory and linked here -->

## Getting Started

### Prerequisites

- Python installed on your local machine, preferably a version between 3.7 and 3.9

In order to check which version of python you have installed, run the following in your command line, and the output should look something like this:

> **NOTE**: in all of the code blocks below, lines preceded with $ indicate commands you should enter in your command line (excluding the $ itself), while lines preceded with > indicate the expected output from the previous command.

```
$ python --version
> Python 3.9.0
```

If you receive an error message, or the version of python you have installed is not between 3.7 and 3.9, consider using a tool like [pyenv](https://github.com/pyenv/pyenv) (on Mac/Linux) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) to manage multiple python interpreters.

### Installation

1. Create a new virtual environment by running `python -m venv env` in the command line.
1. Activate the virtual environment by running `source env/bin/activate` (on Mac/Linux) or `.\env\Scripts\activate` (on Windows).
1. Install this package in editable mode by running `pip install -e .` which makes changes made to scripts within this package available without re-installing it.
1. Install the other dependencies required to contribute to the project by running `pip -r requirements.txt`
1. Execute all tests by running `tox`

## Usage

### This Template

<!-- TODO: Remove this section after following the steps below -->

When using this boilerplate code as a template for your own project, follow the steps below:

1. Complete all of the `TODO` items listed as comments in this README
1. Pick a new name for your package, then replace the word `boilerplate` with that new name in the following places:
   - `setup.py`
   - `tox.ini`
   - `src/boilerplate/` and all files within that directory
   - `tests/` and all of the files within that directory
1. All new python code should be added either as a single module or collection of modules under the `src/{your_package_name}/` directory. For reference:
   ```
   setup.py
   src/
     your_package_name/
       main.py
       your_new_module_1.py
       your_new_module_2/
          your_new_module_2_1.py
          your_new_module_2_2.py
   tests/
   ```
1. If the new code requires a package that is not already listed in the `requirementst.txt` add that dependency to the following locations in this package:
   - Add the name of the package to the list of packages passed to `install_requires` in `setup.py` like so:
     ```
     import os

     from setuptools import find_packages
     from setuptools import setup

     # ...

     setup(
        # ...
        install_requires=[
            "pandas",  # needs to be a string
        ],
        include_package_data=True,
        package_dir={'': 'src'},
        packages=find_packages(where="src"),
     )
     ```
   - Add the name and version to `requirements.txt` like so:
     ```
     # ...
     pytest-cov==2.12.1
     pandas==1.2.4
     ```
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

## Contributing

<!-- TODO: Update this section as well as CONTRIBUTING.md to reflect your contributing guidelines -->

Contributions are always welcome! We encourage contributions in the form of discussion on issues in this repo and pull requests for improvements to documentation and code.

See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to get started.

## License

<!-- TODO: Update this section as well as LICENSE to reflect the license of your project -->

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Acknowledgements

- [Python Packaging Authority Sample Project](https://github.com/pypa/sampleproject)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)
