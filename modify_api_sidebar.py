from bs4 import BeautifulSoup, Tag
import os, sys

def modify_toc_sidebar(file_path):
    """
    Find all toc-elements in the 'on this page' sidebar of format
    ``ndigo6g12_some_struct::some_member`` and modify them to be of format
    ``some_member``.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")

    aside = soup.find("aside", class_="toc-drawer")

    if isinstance(aside, Tag):
        for entry in aside.find_all("span", class_="pre"):
            if "::" in entry.text:
                entry.string = entry.text.split("::")[1]

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(soup))

def process_html_files(directory):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".html"):
                file_path = os.path.join(dirpath, filename)
                modify_toc_sidebar(file_path)
                print(f"Modified: {file_path}")


def main():
    if len(sys.argv) > 1:
        process_html_files(sys.argv[1])
    else:
        print("Call signature:\n"
              "modify_api_sidebar.py path/to/htmls/")

if __name__ == "__main__":
    main()
