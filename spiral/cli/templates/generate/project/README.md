# {{ description }}

## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a venv for development

$ make develop

$ source env/bin/activate


### run {{ label }} cli application

$ {{ label }} --help


### run pytest / coverage

$ make test
```
