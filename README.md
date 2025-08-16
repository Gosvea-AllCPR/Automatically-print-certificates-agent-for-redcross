# 🧾 Red Cross Certificate Printing Agent

🌐 **多语言支持 / Multi-language Support**  
[English](README_EN.md) | [中文](README.md)

An automated system for batch printing American Red Cross training certificates. The program automatically identifies the latest Excel student roster files and performs batch certificate searching, filtering, selection, and downloading operations. Ideal for use with Enrollware / Red Cross platforms.

## 👨‍💻 Author Information

**Boyi Wang（王博一）**  
📞 Phone: 3148572744  
📧 Email: 1084693481@qq.com  

---

## ✅ Key Features

### Certificate Printing Phase
- 📂 **Automatic File Detection**: Identifies the **latest Excel spreadsheet** in the current folder
- 📧 **Smart Processing**: Processes student emails in batches, sorted by `First Name`
- 🧠 **Intelligent Filtering**: Automatically filters certificates meeting the following criteria:
  - Status must be `Valid`
  - Completion date must be **2025 or later**
  - Course name must not contain `online`
- 📥 **Automated Operations**: Auto-selection + size selection (11'' x 8.5'') + download
- ⏯ **Resume Capability**: Supports checkpoint continuation (can resume after interruption)
- ❌ **Failure Tracking**: Automatically exports failed printing records to `failed_certificates.xlsx`

---

## 🗂 Project Structure

redcross_agent/
├── print_certificates.py # Main certificate printing program
├── filter_successful.py # Generate successful printing list
├── [Student Roster].xlsx # Weekly updates (auto-selects latest file)
├── printed_emails.txt # Auto-generated: successfully processed emails
├── failed_certificates.xlsx # Auto-generated: failed printing email list
├── successful_certificates.xlsx # Auto-generated: successful printing student list
├── .gitignore # Git ignore cache files
├── README.md # Project documentation (current)

---

## 🚀 Complete Workflow

### 🧰 Environment Setup

1. **Install Python**: https://www.python.org/
2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
3. **Download ChromeDriver**:
   Place in local path and modify the code:
```python
chrome_driver_path = r"C:\path\to\chromedriver.exe"
```

### 📝 Certificate Printing Phase

1. Place this week's student Excel spreadsheet in the project folder
2. Ensure the Excel file is the "last modified" (or keep only the current file in the directory)
3. Open terminal and run the certificate printing program:
```bash
python print_certificates.py
```
4. The program will automatically:
   - Identify the latest Excel file
   - Process in First Name order
   - Execute batch certificate printing
   - Generate failure list (failed_certificates.xlsx)
5. Can be interrupted anytime with Ctrl + C, system saves progress and skips completed emails

### 📊 Success List Generation

1. Run the success list generation program:
```bash
python filter_successful.py
```
2. The program will automatically:
   - Read the latest Excel file
   - Compare with failure list
   - Generate successful printing student list (successful_certificates.xlsx)

### ♻️ Reset Instructions

If you want to start printing a new spreadsheet (instead of continuing with the previous failure list):

1. Delete or rename the following files:
   - printed_emails.txt (delete or rename as historical record)
   - failed_certificates.xlsx (optional)
   - successful_certificates.xlsx (optional)

2. Replace with new spreadsheet and re-run the program to complete "reset printing"

### 🧯 File Descriptions

- ✅ **printed_emails.txt**: All successfully processed emails (system automatically skips)
- ❌ **failed_certificates.xlsx**: Students who failed to print (can be re-processed)
- ✅ **successful_certificates.xlsx**: Successfully printed student list

---

Developed by Boyi Wang for Gosvea Inc. internship project, enhancing Red Cross certificate printing process automation efficiency.
