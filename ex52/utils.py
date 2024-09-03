import os
from pathlib import Path
from urllib import request
from urllib.parse import urlparse
from bs4 import BeautifulSoup


BASE_URL = "https://learncodethehardway.com"
DATA_URL = f"{BASE_URL}/setup/python/ttb/"


def is_relative(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme or not parsed_url.netloc


def filename_from_url(pdf_url):
    parsed_url = urlparse(pdf_url)
    path = parsed_url.path
    return Path(path).name


def get_raw_html(ttb_page, url=DATA_URL):
    if not os.path.exists(ttb_page):
        with open(ttb_page, "wb") as f:
            resp = request.urlopen(url)
            body = resp.read()
            f.write(body)

    with open(ttb_page) as f:
        body = f.read()
    
    return body


def get_soup(body):
    soup = BeautifulSoup(body, "html5lib")
    return soup


def download_pdf(url, target_path):
    if is_relative(url):
        url = f"{BASE_URL}/{url}"
    
    with request.urlopen(url) as response:
        filename = filename_from_url(url)
        path = Path(target_path)
        with open(path / filename, "wb") as f:
            f.write(response.read())