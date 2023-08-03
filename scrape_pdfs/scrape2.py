import os
import requests
from bs4 import BeautifulSoup

# Function to download a file from a given URL and save it in the specified directory
def download_file(url, directory, downloaded_files):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        if file_name not in downloaded_files:
            file_path = os.path.join(directory, file_name)
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {file_name}")
            downloaded_files.add(file_name)
        else:
            print(f"Already downloaded: {file_name}")
    else:
        print(f"Failed to download: {url}")

# Main function to extract the href URLs and download PDFs from multiple files
def process_html_files_in_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    downloaded_files = set()

    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")
        results_container = soup.find("div", {"id": "results-container"})

        if results_container is None:
            print(f"No results container found in {filename}.")
            continue

        pdf_links = []
        for link in results_container.find_all("a", href=True):
            if link["href"].endswith(".pdf"):
                pdf_links.append(link["href"])

        if not pdf_links:
            print(f"No PDF links found in {filename}.")
            continue

        for pdf_link in pdf_links:
            download_file(pdf_link, output_folder, downloaded_files)

if __name__ == "__main__":
    html_files_folder = "html_files"
    output_folder = "downloaded_pdfs1"

    process_html_files_in_folder(html_files_folder, output_folder)

