import csv
from typing import List

from src.ft_linear_regression.models import CarData


def load_data(filename) -> List[CarData]:
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        return [CarData(*map(int, row)) for row in reader]
