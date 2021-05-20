from unittest.mock import patch

import pandas as pd

from src.report import read_csv, to_parquet


@patch('src.report.pd.read_csv')
def test_read_csv(mock):
    expected = pd.DataFrame({'test': [1, 2, 3, 4, 5]})
    mock.return_value = expected
    actual = read_csv('test_file_path')
    assert (actual, expected)


@patch('src.report.to_parquet')
def test_to_parquet(mock):
    expected = pd.DataFrame({'test': [1, 2, 3, 4, 5]})
    mock.path.return_value = expected
    actual = to_parquet(expected, 'test_file_path_dest')
    assert (actual, expected)
