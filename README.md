# File Timestamp Modifier (Python + PowerShell)

A simple automation script that updates the **creation, last modified, and last accessed timestamps** of all files and folders inside a specified directory.

---

## 🚀 Features

* Recursively updates timestamps for all files and subfolders
* Supports both files and directories
* Uses PowerShell for system-level timestamp modification
* Lightweight and easy to run

---

## 🧰 Tech Stack

* Python 3.x
* PowerShell (Windows)

---

## 📦 Requirements

* Windows OS (PowerShell required)
* Python installed

No external Python libraries required.

---

## ⚙️ How It Works

1. Takes user input:

   * Folder path
   * Target date & time

2. Passes the values into a PowerShell script

3. PowerShell:

   * Iterates through all files and folders
   * Updates:

     * Creation time
     * Last write time
     * Last access time

---

## ▶️ Usage

Run the script:

```bash
python script.py
```

You will be prompted:

```text
Enter the folder path --> C:\example\folder
Enter the date and time DD/MM/YYYY HH:MM:SS --> 01/01/2024 12:00:00
```

---

## 📁 Example

Input:

```text
Folder: C:\Projects\Test
Time: 01/01/2024 12:00:00
```

Output:

All files and folders inside `Test` will have:

* Created time → 01 Jan 2024, 12:00
* Modified time → 01 Jan 2024, 12:00
* Accessed time → 01 Jan 2024, 12:00

---

## ⚠️ Notes

* Script modifies **all timestamps permanently**
* Requires appropriate file system permissions
* Works only on Windows due to PowerShell dependency
* Date format must match:

  ```text
  DD/MM/YYYY HH:MM:SS
  ```

---

## 🛠️ Troubleshooting

### ❌ Permission denied

Run terminal as **Administrator**

---

### ❌ Invalid date format

Ensure input matches:

```text
DD/MM/YYYY HH:MM:SS
```

---

### ❌ PowerShell blocked

If execution policy blocks scripts, the script already uses:

```text
-ExecutionPolicy Bypass
```

---

## 📄 License

For educational and personal use.
