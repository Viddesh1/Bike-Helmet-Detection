# Contributing to Bike Helmet Detection

Thank you for considering contributing to the **Bike Helmet Detection** project. Contributions are essential to make this project better and more reliable for users worldwide. Whether you are fixing a bug, improving the documentation, adding features, or enhancing the codebase, we welcome your efforts.

## Table of Contents
- [Getting Started](#getting-started)
- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Submitting Changes](#submitting-changes)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Setting Up the Project Locally](#setting-up-the-project-locally)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [Contact](#contact)

---

## Getting Started

1) Please read through the readme.md file.
2) Open the [issue](https://github.com/Viddesh1/Bike-Helmet-Detection/issues) if you have any.
3) Feel free to create a [pull request](https://github.com/Viddesh1/Bike-Helmet-Detection/pulls)
4) If you encounter any [bug](https://github.com/Viddesh1/Bike-Helmet-Detection/issues/new/choose) or [feature request](https://github.com/Viddesh1/Bike-Helmet-Detection/issues/new/choose).
5) Have any questions? or Solve others queries at [Community discussion](https://github.com/Viddesh1/Bike-Helmet-Detection/discussions)

To start contributing:
1. Fork this repository.
2. Clone the fork to your local machine:
   ```bash
   git clone https://github.com/<your-username>/Bike-Helmet-Detection.git
   ```
3. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

---

## Code of Conduct

By participating in this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md). Please treat others with respect and professionalism.

---

## How to Contribute

### Reporting Issues

If you find a bug or have a feature request, open an issue on the [Issues](https://github.com/Viddesh1/Bike-Helmet-Detection/issues) page. Ensure to provide:
- A clear description of the issue or feature request.
- Steps to reproduce the issue, if applicable.
- Any relevant logs or screenshots.

### Improving Documentation

Help us improve the documentation by:
- Fixing typos or grammatical errors.
- Adding examples or more detailed explanations.
- Updating outdated sections.

### Adding Features or Fixing Bugs

Follow these steps:
1. Ensure your changes align with the project’s goals and architecture.
2. Open a new issue describing the feature or bug.
3. Wait for approval from a maintainer before starting work.

---

## Submitting Changes

1. Commit your changes with clear and concise messages:
   ```bash
   git add .
   git commit -m "[Feature] Add feature description"
   ```
2. Push your branch to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```
3. Open a pull request to the `main` branch of the original repository.
4. Link your pull request to the corresponding issue, if applicable.
5. Follow up on reviews and address feedback promptly.

---

## Pull Request Guidelines

- Ensure all changes are well-documented and tested.
- Keep your PR small and focused on a single issue or feature.
- Run all tests and linters before submitting:
  ```bash
  tox
  isort .
  black .
  python manage.py test
  ```
- Update the `README.md` file if your changes affect the usage or functionality of the project.

---

## Setting Up the Project Locally

To set up the project locally, follow these steps:
1. Clone the repository.
2. Set up a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .\.venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Testing

Testing is crucial to maintain project stability. Ensure you:
- Write unit tests for any new feature or bug fix.
- Run tests using:
  ```bash
  python manage.py test
  ```
- Check test coverage:
  ```bash
  coverage run manage.py test
  coverage report -m
  ```
- Generate an HTML coverage report:
  ```bash
  coverage html
  ```

---

## Code Quality

Maintain high-quality code by following these standards:
- **Code Formatting**: Use [Black](https://github.com/psf/black):
  ```bash
  black .
  ```
- **Static Typing**: Use [Mypy](http://mypy-lang.org/):
  ```bash
  mypy .
  ```
- **Import Sorting**: Use [Isort](https://github.com/PyCQA/isort):
  ```bash
  isort .
  ```
- **Testing Across Environments**: Use [Tox](https://tox.readthedocs.io/):
  ```bash
  tox
  ```

---

## Contact

If you have any questions or need further assistance:
- Open a discussion on the [Discussions](https://github.com/Viddesh1/Bike-Helmet-Detection/discussions) page.

---

Thank you for contributing! Together, we can make this project even better.

