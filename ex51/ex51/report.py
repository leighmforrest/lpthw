from .pdf import get_pdf, get_number_clusters, get_line_items
from .ttb import get_large_clusters, get_stocks_on_hand, get_production, get_actual_sales
from .utils import DATE_FORMATS, generate_data_dict


def generate_report(pdf_path):
    pdf = get_pdf(pdf_path)
    clusters = get_number_clusters(pdf)
    large_clusters = get_large_clusters(clusters)

    reporting_period = get_line_items(pdf, "Reporting Period", DATE_FORMATS["reporting_period"])
    report_date = get_line_items(pdf, "Report Date", DATE_FORMATS["report_date"])
    stocks_on_hand = get_stocks_on_hand(clusters)
    production = get_production(large_clusters)
    actual_sales = get_actual_sales(production, stocks_on_hand)
    data = generate_data_dict(reporting_period, report_date, production, stocks_on_hand, actual_sales)
    
    return data
