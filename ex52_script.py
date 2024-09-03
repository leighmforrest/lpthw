import os
import json
from pathlib import Path
from ex52.utils import get_raw_html, get_soup, download_pdf
from ex52.ex52 import get_pdf_links, get_pdfs_in_directory, get_report


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "ex52" / "data"


if __name__ == "__main__":
    data_dir = str(DATA_DIR)
    if not os.path.exists("ttb_stats.json"):
        body = get_raw_html("ttb_page.html")

    soup = get_soup(body)
    pdf_links = get_pdf_links(soup)

    for link in pdf_links:
        download_pdf(link, DATA_DIR)

    pdf_paths = get_pdfs_in_directory(data_dir)
    report_data = get_report(pdf_paths)

    with open('ttb.json', 'w') as file:
        json.dump(report_data, file, indent=4)