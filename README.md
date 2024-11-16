
# Web Scraping Script for HPRERA Public Dashboard

## 📖 Overview

This script utilizes **Selenium WebDriver** to extract project details from the HPRERA Public Dashboard. The extracted data includes:  
- GSTIN Numbers  
- PAN Numbers  
- Project Names  
- Permanent Addresses  

The scraped data is saved into a CSV file for easy access and analysis.

---

## 🛠️ Requirements

Ensure the following are installed and available:
- **Python 3.x**
- **Selenium WebDriver (Chrome)**
- **csv module** (built-in with Python)

---

## 🚀 Installation

### 1️⃣ Install Selenium  
Run the following command in your terminal to install Selenium:

```bash
pip install selenium


### 2️⃣ Download ChromeDriver  
Download a ChromeDriver version compatible with your Chrome browser from the [ChromeDriver website](https://sites.google.com/chromium.org/driver/).

### 3️⃣ Update ChromeDriver Path  
Ensure the `webdriver.Chrome()` line in the script points to the path of your downloaded ChromeDriver executable.

---

## 🖥️ Usage

1. Run the script using Python:
   ```bash
   python main.py
   ```
2. The script will:
   - Open a Chrome browser window.
   - Scrape project details from the HPRERA Public Dashboard.
3. Extracted data will be saved in a CSV file named `project_details.csv`.

---

## 📂 CSV File Structure

The output file `project_details.csv` will have the following structure:

| Column Name         | Description                            |
|---------------------|----------------------------------------|
| **GSTIN No**        | GSTIN number of the project           |
| **PAN No**          | PAN number of the project             |
| **Name**            | Name of the project                  |
| **Permanent Address** | Permanent address of the project     |

---

## 🛠️ Troubleshooting

- **ChromeDriver Path**: Ensure ChromeDriver is added to your system's PATH or update the `webdriver.Chrome()` line in the script to the correct path.  
- **Dashboard Changes**: If the HPRERA Public Dashboard is updated, it may affect script functionality. Review and adjust the scraping logic if necessary.

---

## 🤝 Contributing

Contributions are welcome!  
If you find issues or have suggestions for improvement, feel free to:  
- Open an issue
- Submit a pull request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

Special thanks to:
- **Selenium WebDriver for Python**
- **HPRERA Public Dashboard** for providing accessible project data
