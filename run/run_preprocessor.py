from bs4 import BeautifulSoup

from data_processor.pre_processor import process_ptt_html

def run_process_ptt_html():
    # Read HTML file
    with open("var/M.1732505498.A.54D.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    process_ptt_html(soup)

if __name__ == "__main__":
    run_process_ptt_html()