"""Unit tests for matched-control scoring in Task 2."""

import pandas as pd
import pytest

from quantium_task2_analysis import corr_score, magnitude_score, select_controls


def test_similarity_scores_identical_store_series():
    pivot = pd.DataFrame({77: [10.0, 20.0, 30.0], 1: [10.0, 20.0, 30.0]})

    assert corr_score(pivot, 77, 1) == pytest.approx(1.0)
    assert magnitude_score(pivot, 77, 1) == pytest.approx(0.0)


def test_select_controls_ranks_each_matching_candidate_first():
    patterns = {
        77: [10.0, 20.0, 30.0],
        86: [30.0, 20.0, 10.0],
        88: [10.0, 15.0, 40.0],
        1: [10.0, 20.0, 30.0],
        2: [30.0, 20.0, 10.0],
        3: [10.0, 15.0, 40.0],
        4: [18.0, 23.0, 16.0],
    }
    rows = []
    for store, sales in patterns.items():
        for month_index, total_sales in enumerate(sales):
            rows.append(
                {
                    "STORE_NBR": store,
                    "YEARMONTH": 201807 + month_index,
                    "TOTAL_SALES": total_sales,
                    "CUSTOMERS": total_sales + 5,
                }
            )
    pre_trial = pd.DataFrame(rows)

    scores = select_controls(pre_trial, list(patterns))
    best = scores.groupby("TRIAL_STORE", as_index=False).first()

    assert dict(zip(best["TRIAL_STORE"], best["CONTROL_STORE"])) == {
        77: 1,
        86: 2,
        88: 3,
    }
    assert not scores["CONTROL_STORE"].isin([77, 86, 88]).any()
