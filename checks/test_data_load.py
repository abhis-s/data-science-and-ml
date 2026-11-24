"""Starter checks verifying the main bakery sales dataset loads as documented."""

import pandas as pd

BASE_URL = (
    "https://raw.githubusercontent.com/opencampus-sh/"
    "intro-to-data-science-and-ml/main/data/bakery/"
)


def test_sales_data_loads_with_expected_schema_and_count():
    """Verify the raw sales CSV matches documented columns, row count, and bounds."""
    sales = pd.read_csv(BASE_URL + "umsatzdaten_gekuerzt.csv", parse_dates=["Datum"])

    assert list(sales.columns) == ["id", "Datum", "Warengruppe", "Umsatz"]
    assert len(sales) == 9334
    assert sales["id"].is_unique
    assert set(sales["Warengruppe"].unique()) == {1, 2, 3, 4, 5, 6}
    assert (sales["Umsatz"] >= 0).all()
