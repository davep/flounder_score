# Flounder Score

## Introduction

As a software developer who knows little to nothing about biology, genetics
or bioinformatics, I felt it was important that I tried to make my mark on
these fields. Over the last couple or so years, I've seen that a lot of time
and effort goes into deciding how "good" or "bad" a sequence is, involving
massive amounts of data-crunching and machine learning and the like.

Personally, I think this all seems too much like hard work.

Surely, I thought, there has to be a simple way of assigning some value to a
letter and then summing up all of those values. I mean, that's all this
genetics lark is, right? A handful of letters stuck together?

With this deep and valuable insight in mind, I looked around for a simple
method of scoring letters. After a very long search (seriously, it must have
lasted a whole mug of coffee!), I found some ancient tiles, each of which
described the value of the letters normally used in English. At this point
it was obvious that this traditional way of weighting the constituent parts
of one language should and could be applied to another.

And so the *Flounder Score* was born.

## Usage

The Flounder Score library provides the following functions:

### score( sequence: str ) -> int

This function takes a string that is a sequence, applies a complex algorithm
using the values found on the ancient tiles, and returns an integer value
that is the Flounder Score for that sequence. Case is not important. IUAPC
codes are taken into account.

Example:

```python
>>> from flounder import score
>>> score( "gtac" )
7
```

### scores( sequence: str ) -> list[ tuple[ str, int ] ]

This function takes a string that is a sequence, applies a complex algorithm
using the values found on the ancient tiles, and returns a list of tuples.
Each tuple is the base at that position in the input string, along with its
individual score.

Example:

```python
>>> from flounder import scores
>>> scores( "gtac" )
[('g', 2), ('t', 1), ('a', 1), ('c', 3)]
```

### score_to_the_max( sequence: str ) -> integer

This function takes a string that is a sequence, applies an even more
complex algorithm using the values found on the ancient tiles, and returns
an integer value that is the "to-the-max" Flounder Score. Case is not
important. IUAPC codes are taken into account.

The difference with this scoring is that, for the bases, not only do they
score for their own ancient tile value, they also score for the ancient tile
value of every IUAPC code that is related to that base.

Example:

```python
>>> from flounder import score_to_the_max
>>> score_to_the_max( "gtac" )
86
```

### scores_to_the_max( sequence: str ) -> list[ tuple[ str, int ] ]

This function takes a string that is a sequence, applies a complex algorithm
using the values found on the ancient tiles, and returns a list of tuples.
Each tuple is the base at that position in the input string, along with its
individual score. The score provided for each base is the `score_to_the_max`
Flounder Score.

Example:

```python
>>> from flounder import scores_to_the_max
>>> scores_to_the_max( "gtac" )
[('g', 19), ('t', 24), ('a', 20), ('c', 23)]
>>>
```

### codon_score( sequence: str ) -> int

This function takes a string that is a sequence, translates it to an AA
sequence (using as many codons as it can find from the first position),
applies a complex algorithm using the values found on the ancient tiles, and
returns an integer value that is the Flounder Score for that sequence. Case
is not important. IUAPC codes are taken into account.

For example:

```python
>>> from flounder import codon_score
>>> codon_score( "AGACGCAGTCTT" )
4
```

### codon_scores( sequence: str ) -> list[ tuple[ str, int ] ]

This function takes a string that is a sequence, translates it to an AA
sequence (using as many codons as it can find from the first position),
applies a complex algorithm using the values found on the ancient tiles, and
returns a list of tuples. Each tuple is the codon that was found in the
input string, along with its individual score.

For example:

```python
>>> from flounder import codon_scores
>>> codon_scores( "AGACGCAGTCTT" )
[('AGA', 1), ('CGC', 1), ('AGT', 1), ('CTT', 1)]
```

## Building and testing

This library is designed to built using `make`, `pipenv` and Python 3.7. If
you have `pipenv` installed and have an installation of Python 3.7 that it
can see you should only need to type `make` in the root directory of the
repository.

```sh
$ make
pipenv sync --dev
Installing dependencies from Pipfile.lock (e55651)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 41/41 — 00:00:04
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
All dependencies are now up-to-date!
```

Unit tests can be run like this:

```sh
$ make test
PYTHONPATH=. pipenv run coverage run tests/tests.py
test_case (__main__.TestFlounderScore)
Test that we don't care about case. ... ok
test_empty (__main__.TestFlounderScore)
Test that an empty sequence is handled. ... ok
test_unknown (__main__.TestFlounderScore)
Test sequences containing things we don't score. ... ok
test_case (__main__.TestFlounderScoreToTheMax)
Test that we don't care about case. ... ok
test_empty (__main__.TestFlounderScoreToTheMax)
Test that an empty sequence is handled. ... ok
test_unknown (__main__.TestFlounderScoreToTheMax)
Test sequence containing things we don't score. ... ok
test_empty (__main__.TestFlounderScores)
Test that an empty sequence is handled. ... ok
test_scores (__main__.TestFlounderScores)
Test that the individual scores are correct. ... ok
test_unknown (__main__.TestFlounderScores)
Test sequences containing things we don't score. ... ok
test_empty (__main__.TestFlounderScoresToTheMax)
Test that an empty sequence is handled. ... ok
test_scores (__main__.TestFlounderScoresToTheMax)
Test that the individual scores are correct. ... ok
test_unknown (__main__.TestFlounderScoresToTheMax)
Test sequences containing things we don't score. ... ok
```

There are a number of other `Makefile` targets available for all sorts of
linting and testing, as well as for building a package. Simple type:

```sh
$ make help
```

to get a list of them all.

[//]: # (README.md ends here)
