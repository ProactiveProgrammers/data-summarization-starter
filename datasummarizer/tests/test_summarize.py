"""Ensure that the data summarization works correctly."""

import math

from datasummarizer import summarize


def test_summarize_empty_number_list():
    """Ensure that an empty list of numbers summarizes correctly."""
    data_list_numbers = []
    mean = summarize.compute_mean(data_list_numbers)
    assert math.isnan(mean)


def test_summarize_pos_neg_number_list():
    """Ensure that a "cancel out" list of numbers summarizes correctly."""
    data_list_numbers = [-10.0, 10.0]
    mean = summarize.compute_mean(data_list_numbers)
    assert mean == 0.0


def test_summarize_equal_number_list():
    """Ensure that an equal number list of numbers summarizes correctly."""
    data_list_numbers = [10.0, 10.0]
    mean = summarize.compute_mean(data_list_numbers)
    assert mean == 10.0


def test_summarize_different_number_list():
    """Ensure that an equal number list of numbers summarizes correctly."""
    data_list_numbers = [5.0, 10.0]
    mean = summarize.compute_mean(data_list_numbers)
    assert mean == 7.5
