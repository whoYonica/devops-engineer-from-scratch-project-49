# Brain Games

### Hexlet tests and linter status:
[![Actions Status](https://github.com/whoYonica/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/whoYonica/devops-engineer-from-scratch-project-49/actions)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=whoYonica_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=whoYonica_devops-engineer-from-scratch-project-49)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=whoYonica_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=whoYonica_devops-engineer-from-scratch-project-49)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=whoYonica_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=whoYonica_devops-engineer-from-scratch-project-49)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=whoYonica_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=whoYonica_devops-engineer-from-scratch-project-49)



## Description

Brain Games is a collection of five console games that help practice arithmetic and logical thinking. Each game asks the player a series of questions. To win, you need to answer three questions correctly in a row.

## Requirements

- Python 3.12+
- uv

## Installation

Clone the repository:

```bash
git clone git@github.com:whoYonica/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
```

Install dependencies:

```bash
uv sync
```

Build the package:

```bash
uv build
```

Install the package:

```bash
uv tool install --force dist/*.whl
```

## Usage

Run one of the following commands:

```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

## Check if the number is even:
[![asciicast](https://asciinema.org/a/DcNDSuLcFK1mKvdk.svg)](https://asciinema.org/a/DcNDSuLcFK1mKvdk)

## Calculate the result of expression:
[![asciicast](https://asciinema.org/a/ZE9VWfiQmNl4bJzN.svg)](https://asciinema.org/a/ZE9VWfiQmNl4bJzN)

## Find greatest common divisor:
[![asciicast](https://asciinema.org/a/lEs3AwgkGa3m02ID.svg)](https://asciinema.org/a/lEs3AwgkGa3m02ID)

## Find a missing number in progression:
[![asciicast](https://asciinema.org/a/EI6t0FAbUqrjVdoW.svg)](https://asciinema.org/a/EI6t0FAbUqrjVdoW)

## Check if the number is prime:
[![asciicast](https://asciinema.org/a/ldi8d97eJIc8mvcq.svg)](https://asciinema.org/a/ldi8d97eJIc8mvcq)