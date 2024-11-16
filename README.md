Web Scraping Script for HPRERA Public Dashboard

Overview

This script uses Selenium WebDriver to scrape project details from the HPRERA Public Dashboard. It extracts GSTIN numbers, PAN numbers, names, and permanent addresses of projects and saves them to a CSV file.

Requirements

•⁠  ⁠Python 3.x
•⁠  ⁠Selenium WebDriver (Chrome)
•⁠  ⁠csv module

Installation

1.⁠ ⁠Install Selenium using pip: ⁠ pip install selenium ⁠
2.⁠ ⁠Download ChromeDriver (compatible with your Chrome version) from (link unavailable)
3.⁠ ⁠Update the ⁠ webdriver.Chrome() ⁠ line to point to the downloaded ChromeDriver executable

Usage

1.⁠ ⁠Run the script using Python: ⁠ python main.py ⁠
2.⁠ ⁠The script will open a Chrome browser window and start scraping project details
3.⁠ ⁠The scraped data will be saved to a CSV file named ⁠ project_details.csv ⁠

CSV File Structure

The CSV file contains the following columns:

| Column Name | Description |
| --- | --- |
| GSTIN No | GSTIN number of the project |
| PAN No | PAN number of the project |
| Name | Name of the project |
| Permanent Address | Permanent address of the project |

Troubleshooting

•⁠  ⁠Ensure ChromeDriver is in the system's PATH or update the ⁠ webdriver.Chrome() ⁠ line
•⁠  ⁠Check for any updates to the HPRERA Public Dashboard that may affect the script's functionality

Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

License

This script is released under the MIT License.

Acknowledgments

•⁠  ⁠Selenium WebDriver for Python
•⁠  ⁠HPRERA Public Dashboard for providing the data
