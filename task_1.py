# -*- coding: utf-8 -*-
"""Task_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pT9fLJITE_GGZelA4P5RHkfJUpSVkdik
"""

import pandas as pd

pip install pdfplumber

import csv
import pdfplumber
import re

def extract_articles_from_pdf(pdf_file):
    articles = []
    article_start_pattern = re.compile(r"(\d+\.\d+)\.\s+(.+)")
    current_article = None
    article_started = False

    with pdfplumber.open(pdf_file) as pdf:

        for page_number in range(5, len(pdf.pages)):
            page = pdf.pages[page_number]
            text = page.extract_text()

            if text:
                for line in text.split("\n"):
                    match = article_start_pattern.match(line)

                    if match:
                        if article_started and current_article:

                            articles.append(current_article)


                        current_article = {
                            "s_no": match.group(1),
                            "article_title": match.group(2).strip(),
                            "article_body": ""
                        }
                        article_started = True
                    elif article_started and current_article:

                        current_article["article_body"] += line + "\n"


        if article_started and current_article:
            articles.append(current_article)

    return articles

def write_to_csv(data, csv_file):
    headers = ["s_no", "article_title", "article_body"]
    try:
        with open(csv_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print("Writing to CSV completed successfully.")
    except Exception as e:
        print(f"Error writing to CSV: {e}")

def main(pdf_file, csv_file):
    try:
        articles = extract_articles_from_pdf(pdf_file)
        write_to_csv(articles, csv_file)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    pdf_file = "/content/drive/MyDrive/Access file/saars/VisionIAS Monthly Current Affairs January 2024 January 2024.pdf"
    csv_file = "output.csv"
    main(pdf_file, csv_file)

import pandas as pd

df=pd.read_csv('/content/out.csv')

df.head()
