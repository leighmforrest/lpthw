import os
from pathlib import Path
from ex51.ex51.report import generate_report


def get_pdf_links(soup):
    ordered_lists = soup.find_all("ol")

    # flatten the ordered lists and pull out links
    links = [link.get("href") for ol in ordered_lists for link in ol.find_all('a')]

    # filter links that are PDF files
    pdf_links = [link for link in links if link.endswith(".pdf")]

    return pdf_links


def get_pdfs_in_directory(path):
    """Return paths of all pdf in"""
    pdf_paths = [path + "/" + pdf_path  for pdf_path in  os.listdir(path) if pdf_path.endswith(".pdf")]
    return pdf_paths


def get_report(pdf_paths):
    data = []

    for path in pdf_paths:
        full_path = path
        print(full_path)
        report = generate_report(full_path)
        data.append(report)
    
    return data