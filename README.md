# WebScraping-Python


## Overview

This is a simple web scraper implemented in Python, designed to extract data from an HTML web page. The scraper utilizes the lxml library for HTML parsing and the requests library for making HTTP requests.

## Dependencies

Before using the web scraper, make sure you have the following dependencies installed:

lxml
requests
You can install these dependencies using the following command:

`pip install lxml requests`

## How to Use

1. Clone or download the repository to your local machine.

2. Install the required dependencies using the command mentioned above.

3. Open the Python script containing the web scraper code.

4. Update the url variable with the URL of the web page you want to scrape.

5. Customize the XPath expression according to the structure of the HTML page you are scraping. In the provided example, the XPath expression is modified to extract names from a specific class of div elements.

Run the Python script.

`python3 scraping.py`

Check the console output. If the HTTP request is successful (status code 200), the scraper will attempt to extract data based on the provided XPath expression. If successful, it will print the retrieved data; otherwise, it will notify you that no data was found.
