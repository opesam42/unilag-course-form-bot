# UNILAG Course Form Downloader 🚀

A Python script that automates logging into the UNILAG Student Portal, selects a session and semester, and downloads the course registration form as a PDF using Selenium.

---

## 📌 Features
- Automates login to the UNILAG student portal.
- Selects session and semester.
- Extracts the course form download link.
- Downloads and saves the course form as a PDF.
- Uses environment variables for secure authentication.

---

## 🛠️ Requirements
Ensure you have the following installed before running the script:
- **Python
- **Google Chrome**
- **Selenium**
- **Python-dotenv**

---

## 🚀 Setup Instructions

### 1️. Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone https://github.com/yourusername/unilag-course-downloader.git
cd unilag-course-downloader

### 2. Install Dependencies
```bash
pip install -r requirements.txt

### 3. Set Up Environment Variable
```bash
MATRIC_NO=your_matric_no
PASSWORD=your_password

### 4. Run the Script
```bash
python main.py


## 🔍 How It Works  
1. Opens the **UNILAG student portal** login page.  
2. Logs in using credentials stored in `.env`.  
3. Navigates to the **course form page**.  
4. Selects the **session and semester**.  
5. Extracts the **course form download URL**.  
6. Saves the file as **`course.pdf`**.  

---

## 🛠️ Troubleshooting  
### 🔹 Selenium Errors  
Ensure your **ChromeDriver** version matches your installed **Chrome browser** version.  
Download the correct **ChromeDriver** from [here](https://sites.google.com/chromium.org/driver/).  

### 🔹 Login Issues  
- Verify your **matric number** and **password** in the `.env` file.  
- Ensure your **UNILAG portal account** is active.  

### 🔹 Timeout Errors  
If elements take too long to load, increase the **WebDriverWait** duration in the script.  

---

## 📜 License  
This project is open-source and available under the **MIT License**.  
Feel free to modify and distribute it according to the license terms.  
