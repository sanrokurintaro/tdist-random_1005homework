import statistics
import pytest
from tdist_random import t_random


def test_count():
    assert len(t_random(0, 1, 5, 100)) == 100
    assert t_random(0, 1, 5, 0) == []


def test_mean_and_variance():
    xs = t_random(10.0, 4.0, 8, 200_000, seed=1)
    assert statistics.fmean(xs) == pytest.approx(10.0, abs=0.05)
    assert statistics.pvariance(xs) == pytest.approx(4.0, rel=0.1)


def test_seed_reproducible():
    assert t_random(0, 1, 5, 10, seed=3) == t_random(0, 1, 5, 10, seed=3)


def test_invalid():
    with pytest.raises(ValueError):
        t_random(0, 1, 2, 10)
    with pytest.raises(ValueError):
        t_random(0, -1, 5, 10)
