# Invoice Data Extractor (Amazon & Flipkart)

A Python-based tool to extract structured data from Amazon and Flipkart PDF invoices without using any third-party APIs. It processes PDF files and stores cleaned, structured data into an Excel file for further analysis or automation.

---

##  Folder Structure

```
Assignment/
├── Input/                # Original PDF invoices (4 files: 2 Amazon, 2 Flipkart)
├── Output/               # Extracted Excel output
│   └── extracted_invoices.xlsx
├── Coding/               # Python scripts
│   ├── extract_invoices.py
│   └── debug_extract_text.py
├── venv/                 # Python virtual environment (excluded via .gitignore)
├── requirements.txt      # Frozen pip dependencies
└── .gitignore
```

---

## 🚀 Features

- 📄 Extracts key invoice fields:
  - Invoice Number
  - Order Date
  - Customer Name
  - Phone
  - Address
  - Total Amount
  - Payment Method
  - Platform (Amazon / Flipkart)

-  No third-party APIs used
-  Uses standard Python libraries: `PyPDF2`, `openpyxl`, `re`
-  Regex patterns tuned to actual Amazon/Flipkart invoice formats

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/invoice-extractor.git
cd invoice-extractor
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
.\venv\Scripts\Activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add PDF invoices

Place 2 Amazon and 2 Flipkart invoice PDFs inside the `Input/` folder.

### 5. Run the script

```bash
cd Coding
python extract_invoices.py
```

### 6. Check output

Go to the `Output/` folder. You’ll find the structured Excel file:
```
extracted_invoices.xlsx
```

---

##  Notes

- Regex rules are hardcoded to parse common invoice formats from Amazon and Flipkart (India region).
- Masked phone numbers or missing fields are handled with `"NA"` fallback.
- Unicode support (₹ symbol, Indian text) is handled with UTF-8.
- This project adheres strictly to the assignment requirement: **no external API libraries** are used.

---

##  Author

**Ayantika Dhar**  
M.Tech CSE, IIT Jodhpur  
Assignment: Invoice Extraction using Python (Internship Task)
