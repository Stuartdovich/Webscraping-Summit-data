
# Web Scraping Script for Investor Information

## Overview

This Python script uses Selenium to scrape investor information from the AIM Summit website. It extracts details including the first name, last name, LinkedIn profile URL, and location of attendees.

## Features

- **Extracts Names**: Retrieves the first and last names of investors.
- **LinkedIn Profiles**: Collects LinkedIn profile URLs for each investor.
- **Location**: Captures the location or other details if available.
- **Data Storage**: Saves the extracted information into a CSV file for easy access.

## Prerequisites

Ensure you have the following installed:
- **Python 3.11** (or any compatible version)
- **Selenium**: Python package for web browser automation.
- **webdriver_manager**: Automatically manages browser drivers.
- **pandas**: For data manipulation and saving to CSV files.

## Installation

1. **Install Required Packages**

   Install the necessary Python packages using pip:

   ```bash
   pip install selenium webdriver-manager pandas
   ```

2. **Download and Install WebDriver**

   The script uses `webdriver_manager` to handle the WebDriver installation automatically.

## Usage

1. **Update the Script**

   Ensure the URL in the script matches the page you want to scrape. Update the XPath expressions if necessary to fit the structure of the HTML.

2. **Run the Script**

   Execute the script using Python:

   ```bash
   python webscraping_script.py
   ```

3. **Output**

   The script will generate a CSV file named `investors_list_with_location.csv` in the same directory. This file contains the extracted data with columns for First Name, Last Name, LinkedIn Profile, and Location.

## Code Explanation

- **Setup WebDriver**: Initializes the WebDriver for Chrome using `webdriver_manager`.
- **Load Page**: Opens the specified URL and waits for the page to load.
- **Scrape Data**: Iterates through speaker cards to extract names and click on each card to gather LinkedIn profiles and location details.
- **Close Modal**: Closes the modal after data extraction.
- **Save to CSV**: Converts the collected data into a pandas DataFrame and saves it as a CSV file.

## Troubleshooting

- **ModuleNotFoundError**: Ensure all required modules are installed. Use `pip install <module_name>` to install missing modules.
- **XPath Issues**: If the script does not extract data correctly, verify and update the XPath expressions according to the latest HTML structure of the target website.
