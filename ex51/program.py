import sys
import os
from collections import OrderedDict
from ex51.report import generate_report
from ex51.utils import to_capitalized, is_pdf

def display_dict(report):
    if isinstance(report, OrderedDict):
        # get max length of keys and values
        max_key = max([len(key) for key in report.keys()])
        max_value = max([len(str(value)) for value in report.values()])
        
        # display dict with padding
        for key, value in report.items():
            print(f"{to_capitalized(key):<{max_key}} | {value:>{max_value}}")
        print(f"{'-'*(max_key + max_value + 3)}\n\n")
    else:
        print("You must use an OrderedDict.")

if __name__ == "__main__":
    files = sys.argv[1:]

    if not files:
        print("Please eneter a pdf path.")
    else:
        try:
            for file in files:
                pdf_path = os.path.join(os.path.dirname(__file__), file)
                if is_pdf(pdf_path):
                    report = generate_report(pdf_path)
                    display_dict(report)
                else:
                    print("You must enter a valid PDF path.")
        except Exception as e:
            print("File could not be parsed.")
            print(e)
