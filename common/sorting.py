"""Sorting functions."""
import re


def natural_sort_key(string):
    """Make sure folders named '10....' appear after/below folders named '9...'."""
    _nsre = re.compile('([0-9]+)')
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, string)]
