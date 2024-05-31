# Assignment_text_from_pdf (Task 1)

## PDF to CSV Extractor

Overview
This project is a Python script designed to download a PDF file from a specified URL, extract text from the PDF, parse the text into individual articles, and save the parsed data into a CSV file. Each article in the CSV file includes a serial number, title, and body.

### Features

Downloads a PDF file from a given URL.
Extracts text from the PDF using PyMuPDF (fitz).
Parses the text to identify article titles and bodies.
Stores the parsed data in a CSV file with appropriate quotes for special characters.

### Requirements
Python 3.x
requests library
pymupdf (PyMuPDF) library
Installation


Download the PDF and extract data:

Run the Python script extract_pdf_to_csv.py:
Copy code
python extract_pdf_to_csv.py
The script will download the PDF from the specified URL, extract the text, parse the articles, and save the data into a CSV file named articles.csv.
Output:

### The CSV file articles.csv will contain the parsed articles with the following headers:
s_no: Serial number of the article.
article_title: Title of the article.
article_body: Body/content of the article.

### Error Handling
The script includes error handling for:
Download failures (e.g., incorrect URL, network issues).
PDF reading errors.
CSV writing errors.


# Assignment_Indian Express Article Scraper (Task 2)

## Overview
This Python script scrapes articles related to business from the Indian Express website, extracts relevant information such as title, author, publication date, and content, and stores this data in a SQLite database. It also provides functionality to view the stored data in tabular format.

## Features
Scrapes articles related to business from the Indian Express website.
Extracts title, author, publication date, and content from the scraped articles.
Stores the extracted data in a SQLite database.
Provides functionality to view stored data in tabular format with pagination.

## Requirements
Python 3.x
requests library
beautifulsoup4 library
sqlite3 library
tabulate library


## The script will scrape articles, store them in the database, and display table information.

## Example Output
The script will display tables containing information about stored articles, including their titles, authors, publication dates, and content.

##Error Handling
The script includes error handling for:
Failure to retrieve the website or individual articles.
Missing or incomplete information in scraped articles



