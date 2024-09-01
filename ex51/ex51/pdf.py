import re

import pdftotext

from .utils import is_pdf, parse_to_iso_date, to_snake_case


NUMBERS_PATTERN = r"^[\d,]+$"


def get_pdf(path_string):
    """Get a text object from an existing PDF."""
    if is_pdf(path_string):
        with open(path_string, "rb") as file:
            pdf = pdftotext.PDF(file)

        return pdf
    else:
        raise ValueError("The path must be a PDF file.")


def get_matching_lines(pdf, startswith):
    """Get a line of text that starts with a certain string."""
    lines = [line for page in pdf for line in page.splitlines()]
    filtered_lines = [line.replace("REVISED", "").strip() for line in lines]
    matching_lines = [line.strip() for line in filtered_lines if line.startswith(startswith)]

    return matching_lines


def get_line_items(pdf, line_item, date_format):
    """Pull out data from a line in the pdf and return it as a dictionary."""
    line_item_list = get_matching_lines(pdf, line_item)

    if not line_item_list:
        raise ValueError(f"No matching item found for {line_item}")

    # split the line at the colon
    line_item_list = [item.strip().lower() for item in line_item_list[0].split(":")]
    if len(line_item_list) < 2:
        raise ValueError(f"Incorrect format for {line_item}.")

    # fabricate the data dict
    line_item_dict = {
        to_snake_case(line_item_list[0]): parse_to_iso_date(
            line_item_list[1], date_format
        )
    }

    return line_item_dict


def get_number_clusters(pdf):
    """Get a list of clusters containing one or more numbers based on the TTB pdf"""
    clusters = []
    current_cluster = []

    for page in pdf:
        # Remove the formfeed characters and split by lines
        lines = page.replace("\x0c", "").split("\n")

        for line in lines:
            if re.match(NUMBERS_PATTERN, line.strip()):
                try:
                    # convert line to integer after removing commas
                    number = int(line.replace(",", "").strip())
                    current_cluster.append(number)
                except ValueError:  # pragma: no cover
                    continue  # pragma: no cover
            else:
                if current_cluster:
                    clusters.append(current_cluster)
                    current_cluster = []

        if current_cluster:
            clusters.append(current_cluster)  # pragma: no cover
            current_cluster = []  # pragma: no cover
    return clusters
