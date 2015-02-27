#!/usr/bin/python

from random import choice, randint
from words import adjectives, nouns


def pykunate(token_range=9999, delimiter="-"):
    """Generate a Heroku-like name, consisting of an adjective, a noun,
    and a numerical token, separated by the given delimiter."""

    if token_range <= 0:
        raise ValueError("token_range must be > 0")

    adjective = choice(adjectives)
    noun = choice(nouns)
    token = str(randint(0, token_range))
    name = delimiter.join((adjective, noun, token))
    return name
