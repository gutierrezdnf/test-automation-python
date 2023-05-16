# Test Automation Python

[![GitHub Actions status](https://github.com/gutierrezdnf/test-automation-python/actions/workflows/checks.yml/badge.svg)](https://github.com/gutierrezdnf/test-automation-python/actions)

This project is a template for a Test Framework using Python, pytest and Selenium WebDriver.

**Instructions:**

You need to have installed the following:

1. Python 3.11
2. Pipenv
3. One of the following browsers:
   1. Google Chrome
   2. Firefox
   3. Microsoft Edge

Once installed, follow the instructions below:

~~~shell
# Create a virtual environment
$ pipenv shell

# Install the dependencies
$ pipenv install --dev --python 3.11

# Run the tests
$ pytest --gui --browser=chrome  # Available browser options: (chrome | firefox | edge)
~~~
