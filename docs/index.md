# Introduction

From early 2018 until late 2022 I worked as a software developer attached to
a bioinformatics team. One of the things I saw the team around me doing was
a lot of "scoring" of sequences, etc (imagine a lot of layman hand-waving
here, obviously).

Playing on the "DNA is just code" nonsense trope, it became a bit of a
running joke for me to suggest that they should try a scoring system based
on a popular tile-based word game. Eventually, with a bit of spare time on
my hands, I decided to actually write and publish a library that implemented
this.

And so the *Flounder Score* was born.

No, it's not a serious library, but I also think it makes a serious point
about [people who think "it's just code"](https://xkcd.com/1605/).

## Installation

The library can be installed [from
PyPI](https://pypi.org/project/flounder-score/):

```sh
$ pip3 install flounder-score
```

## Usage

See [the module documentation](flounder.md) for the detailed library
documentation.

### Getting the score

This function takes a string that is a sequence returns an integer value
that is the flounder score for that sequence. Case is not important. [IUAPC
codes](https://www.bioinformatics.org/sms/iupac.html) are taken into
account.

Example:

```python exec="on" source="tabbed-left" result="python"
from flounder import score

print(score("GTAC"))
```

### Getting all the scores

This function takes a string that is a sequence, and returns a list of
tuples. Each tuple is the base at that position in the input string, along
with its individual [`score`][flounder.score.score].

Example:

```python exec="on" source="tabbed-left" result="python"
from flounder import scores

print(scores("gtac"))
```

### Getting the score to the max

This function takes a string that is a sequence, and returns a "to the max"
score. Case is not important. [IUAPC
codes](https://www.bioinformatics.org/sms/iupac.html) are taken into
account.

The difference with this scoring is that, for the bases, not only do they
score for their own [`score`][flounder.score.score], they also
[`score`][flounder.score.score] for every [IUAPC
code](https://www.bioinformatics.org/sms/iupac.html) that is related to that
base.

Example:

```python exec="on" source="tabbed-left" result="python"
from flounder import score_to_the_max

print(score_to_the_max("gtac"))
```

### Getting all the scores to the max

This function is similar to [`scores`][flounder.score.scores], except it
returns a list of tuples where each tuple is the base at that position in
the input sequence, along with its individual
[`score_to_the_max`][flounder.score.score_to_the_max].

Example:

```python exec="on" source="tabbed-left" result="python"
from flounder import scores_to_the_max

print(scores_to_the_max("gtac"))
```

### Getting the codon score

This function takes the input sequence, translates it into an amino acid
sequence (using as many codons as it can find from the first position), and
then [scores][flounder.score.score] that resulting sequence.

For example:

```python exec="on" source="tabbed-left" result="python"
from flounder import codon_score

print(codon_score("AGACGCAGTCTT"))
```

### Getting the codon scores

This function takes an input sequence, translates it into an amino acid
sequence (using as many codons as it can find from the first position), and
then returns a list of tuples where the value in the first position is the
codon being scored and the second is the [score for that
codon][flounder.score.codon_score].

For example:

```python exec="on" source="tabbed-left" result="python"
from flounder import codon_scores

print(codon_scores("AGACGCAGTCTT"))
```

[//]: # (index.md ends here)
