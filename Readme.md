# Deeper Testing

This exercise set offers a number of smaller sections to consider how we can take our automated testing beyond just that of unit & integration tests.

Feel free to choose a different path through the exercises, but we recommend the following order; each link contains some more specific instructions.

## Requirements

Some exercises use Poetry instead of pip to manage Python dependencies. If you run `poetry --version` and it outputs something like `Poetry (version 1.7.1)` then you're all good to go!
If not, you can install Poetry by following the instructions [here](https://python-poetry.org/docs/#installation). Read the instructions carefully: you may need to install `pipx` first.
To understand more about Poetry, you can watch this 8 minute video: https://www.youtube.com/watch?v=Ji2XDxmXSOM

Some exercises require you to have a recent version of node/npm installed. If you need to, you can install those [here](https://nodejs.org/en/download/).

> Note that since we will be triggering a browser session from the command line in various exercises, WSL on Windows will not be an option.

Before you start the exercises, fork this repo and clone it onto your local machine.

> Each exercise is configured as a separate codebase so if you want VSCode to correctly handle intellisense etc., it is best to open each subfolder directly in VSCode during that exercise.

## Exercises

Part 1 - End to End testing:
* [Selenium](./e2e-selenium/Readme.md)
* [Playwright](./playwright/Readme.md)

Part 2 - Performance & Load Testing
* [Artillery](./artillery/Readme.md)

Part 3 - Performance & Accessibility testing
* [Google Lighthouse](./lighthouse/Readme.md)

## Part 4 (Optional) - Use the tools in anger!

If you have time after exploring each of the tools, have a go at setting them up fresh for the Bank API exercise (or indeed, a work project). What useful tests can you generate?
