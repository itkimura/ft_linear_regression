import pytest
import pandas as pd
from src.ft_linear_regression.utils import load_data

@pytest.fixture
def mock_data():
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'target': [7, 8, 9]
    }
    return pd.DataFrame(data)

def test_load_data(mock_data, tmp_path):
    # Save the mock data to a temporary CSV file
    mock_csv = tmp_path / "data.csv"
    mock_data.to_csv(mock_csv, index=False)
    
    # Use the load_data function to load the CSV
    data = load_data(str(mock_csv))

    print("test result: " + data)
    
    # Check that the loaded data matches what we expect
    assert data['features'].shape == (3, 2)  # 3 rows, 2 features
    assert data['target'].shape == (3,)      # 3 rows of target data
    assert data['target'][0] == 7            # First target value should be 7

