COLUMNS = [
    "current_month",
    "prior_year_current_month",
    "current_year_cumulative_to_date",
    "prior_year_cumulative_to_date",
]


def get_large_clusters(clusters):
    """Get a dictionary based on clumns and grouped rows based in the TTB PDF."""
    raw_numbers = [cluster for cluster in clusters if len(cluster) == 9]
    dictionary = dict(zip(COLUMNS, raw_numbers))

    return dictionary


def get_stocks_on_hand(clusters):
    """Get a dictionary of stocks on hand each month, based on returned
    clusters from the TTB PDF. Not that it needs the original clusters,
    not the large clusters.
    """
    base_key = "stocks_on_hand_end_of_month"
    stocks_on_hand_numbers = [numbers[0] for numbers in clusters[-2:]]
    columns = [f"{base_key}_{column}" for column in COLUMNS[:2]]

    return dict(zip(columns, stocks_on_hand_numbers))


def get_production(clusters):
    """Get the production numbers for all columns."""
    base_key = "production"
    data = {f"{base_key}_{column}": numbers[0] for column, numbers in clusters.items()}
    
    return data


def get_actual_sales(production, stocks_on_hand):
    ending_indices = COLUMNS[:2]
    base_index = "actual_sales"
    data = {}
    
    for index in ending_indices:
        index_production = int(production[f"production_{index}"])
        index_stocks_on_hand = int(stocks_on_hand[f"stocks_on_hand_end_of_month_{index}"])
        data[f"{base_index}_{index}"] = index_production - index_stocks_on_hand
    
    return data
