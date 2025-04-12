from io import StringIO
import pytest
import pandas as pd

from src.ft_linear_regression.models import CarData
from src.ft_linear_regression.utils import load_data

data_str = """km,price
240000,3650
139800,3800
150500,4400"""

data_list = [CarData(*map(int, line.split(","))) for line in data_str.split("\n")[1:]]


@pytest.fixture
def mock_data():
    return pd.read_csv(StringIO(data_str))


def test_load_data(mock_data, tmp_path):
    # Save the mock data to a temporary CSV file
    mock_csv = tmp_path / "data.csv"
    mock_data.to_csv(mock_csv, index=False)

    data = load_data(str(mock_csv))
    assert data == data_list
