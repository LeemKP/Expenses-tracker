# Personal-expenses-tracker
A lightweight Command Line Interface (CLI) expense tracker written in Python. All financial records, category breakdowns and monthly histories persist locally on your machine in a private `.json` file.

For your information, this python script is just a personal mini project done by the author. It is not recognized by any school, university or any government sectors.

---

## Prerequisites: Installing Python
Ensure you have Python 3 installed on your machine before running the application.

### Windows
Install Python via the Windows Package Manager directly from PowerShell:
```powershell
#To search available python to be installed
winget search Python.Python

#To install the selected python, Eg: Python version 3.14 is selected to be installed
winget install Python.Python.3.14
```
After python successfully installed, close the PowerShell and reopen it. This is to refresh the PowerShell.

### Linux / Ubuntu (via Mamba)
If you are working in an Ubuntu or WSL environment using Mamba, you can install Python with the following coding:
```bash
#To search available python to be installed
mamba search python

#To install selected python, Eg: Python version 3.14.7
mamba install python=3.14.7
#Take note that you must not have any spacing for ('python=3.14.7').
```

### MacOS
Unfortunately, the author does not have any experience with MacOS 🥲. But as long as python is installed in the machine, this expenses_tracker.py will be able to work.

---

## How to Run
1. Download the expenses_tracker.py file from this repository.
2. Open your machine's terminal (PowerShell/Ubuntu/so on).
3. Navigate to the folder containing `expenses_tracker.py`.
4. Copy the path of the folder and paste it in your terminal like this.

Windows (PowerShell)
```powershell
#For example, I saved `expenses_tracker.py` in Downloads.
cd C:\Users\User\Downloads
```
Ubuntu/WSL:
```bash
#For example, I saved `expenses_tracker.py` in Downloads.
cd /mnt/c/Users/User/Downloads 

#Or I saved `expenses_tracker.py` in mamba's environment.
cd path
```
5. Launch the script:

Windows (PowerShell)
```powershell
python expenses_tracker.py
#OR using the Windows launcher:
py expenses_tracker.py
```
Ubuntu/WSL:
```bash
python expenses_tracker.py
```

---

## Features
* Add Expenses: Track spending across Food, Transport, Entertainment and Bills with custom notes and automatic dates.
* Category Breakdown: View subtotal costs and spending percentages for each individual category.
* Full Financial Report: View an itemized spending ledger alongside monthly budget balances and threshold alerts.
* Budget Limits: Set or adjust a monthly spending cap with automated warnings when approaching limit thresholds.
* Automatic Rollover: Archives spending automatically at the turn of each month and resets the active budget.
* Historical Archive: Review historical summaries and detailed itemized receipts from previous months.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
