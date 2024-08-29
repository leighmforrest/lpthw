import re
from collections import OrderedDict
from datetime import datetime
import pdftotext

COLUMNS = [
    "current_month",
    "prior_year_current_month",
    "current_year_cumulative_to_date",
    "prior_year_cumulative_to_date",
]

DATE_FORMATS = {"reporting_period": "%B %Y", "report_date": "%d%b%Y"}

path_string = "./ttb_10_2021.pdf"
numbers_pattern = r"^[\d,]+$"


def parse_to_iso_date(date_string, date_format=DATE_FORMATS["reporting_period"]):
    date_object = datetime.strptime(date_string.strip(), date_format)
    return date_object.date().isoformat()


def to_snake_case(str1):
    str1 = str1.lower()
    str1 = re.sub(r"[\s\-]+", "_", str1)
    str1 = re.sub(r"[^\w_]", "", str1)
    return str1


def to_capitalized(str1):
    words = str1.split("_")
    capitalized_words = [word.capitalize() for word in words]
    capitalized_string = " ".join(capitalized_words)

    return capitalized_string


def get_pdf(path_string):
    with open(path_string, "rb") as file:
        pdf = pdftotext.PDF(file)

    return pdf


def get_matching_lines(pdf, startswith):
    lines = [line for page in pdf for line in page.splitlines()]
    matching_lines = [line.strip() for line in lines if line.startswith(startswith)]
    return matching_lines


def get_number_clusters(pdf):
    """Get a list of clusters of one or more numbers based on the TTB pdf."""
    clusters = []
    current_cluster = []

    for page in pdf:
        # Remove form feed characters and split by lines
        lines = page.replace("\x0c", "").split("\n")

        for line in lines:
            if re.match(numbers_pattern, line.strip()):
                try:
                    # Convert line to integer after removing commas
                    number = int(line.replace(",", "").strip())
                    current_cluster.append(number)
                except ValueError:
                    continue
            else:
                if current_cluster:
                    clusters.append(current_cluster)
                    current_cluster = []

        if current_cluster:
            clusters.append(current_cluster)
            current_cluster = []

    return clusters


def get_large_clusters(clusters):
    """Return a dictionary based on columns and grouped rows based in the TTB pdf."""
    raw_numbers = [cluster for cluster in clusters if len(cluster) == 9]
    dictionary = dict(zip(COLUMNS, raw_numbers))
    return dictionary


def get_line_items(pdf, line_item, date_format):
    """Pull out data from a line in the PDF and return it as a dictionary."""
    line_item_list = get_matching_lines(pdf, line_item)
    if not line_item_list:
        raise ValueError(f"No matching line found for {line_item}")

    line_item_list = [item.strip().lower() for item in line_item_list[0].split(":")]
    if len(line_item_list) < 2:
        raise ValueError(f"Incorrect format for {line_item}")

    line_item_dict = {
        to_snake_case(line_item_list[0]): parse_to_iso_date(
            line_item_list[1], date_format
        )
    }
    return line_item_dict


def get_stocks_on_hand(clusters):
    """Get a dictionary of stocks on hand each month, based on returned clusters
    from the TTB pdf. Note that it need the original clusters, not the large clusters.
    """
    base_key = "stocks_on_hand_end_of_month"
    stocks_on_hand_numbers = clusters[-2:]

    return {
        f"{base_key}_{COLUMNS[0]}": stocks_on_hand_numbers[0][0],
        f"{base_key}_{COLUMNS[1]}": stocks_on_hand_numbers[1][0],
    }


def get_production(clusters):
    """Get the production numbers for all columns."""
    base_key = "production"
    data = {}

    for column, numbers in clusters.items():
        data[f"{base_key}_{column}"] = numbers[0]

    return data


def get_actual_sales(production, stocks_on_hand):
    ending_indices = COLUMNS[:2]
    base_index = "actual_sales"
    data = {}

    for index in ending_indices:
        index_production = int(production[f"production_{index}"])
        index_stocks_on_hand = int(
            stocks_on_hand[f"stocks_on_hand_end_of_month_{index}"]
        )
        data[f"{base_index}_{index}"] = index_production - index_stocks_on_hand

    return data


def generate_data_dict(*args, **kwargs):
    """Generate an OrderedDict from dictionaries in the arguments."""
    data = OrderedDict()

    for arg in args:
        data.update(arg)

    return data


def display_data(ordered_dict):
    """Display key values pairs from an OrderedDict."""
    # Find the max string length values for the keys and values
    key_width = max([len(to_capitalized(key)) for key in ordered_dict.keys()])
    value_width = max([len(str(value)) for value in ordered_dict.values()])

    for key, value in ordered_dict.items():
        print(f"{to_capitalized(key):<{key_width}} | {value:>{value_width}}")


if __name__ == "__main__":
    pdf = get_pdf(path_string)

    # get number clusters
    clusters = get_number_clusters(pdf)
    large_clusters = get_large_clusters(clusters)

    # get the data
    reporting_period = get_line_items(
        pdf, "Reporting Period", DATE_FORMATS["reporting_period"]
    )
    report_date = get_line_items(pdf, "Report Date", DATE_FORMATS["report_date"])
    stocks_on_hand = get_stocks_on_hand(clusters)
    production = get_production(large_clusters)
    actual_sales = get_actual_sales(production, stocks_on_hand)

    data = generate_data_dict(
        report_date, reporting_period, production, stocks_on_hand, actual_sales
    )

    display_data(data)
