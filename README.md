# Employee Management System (Python + MySQL + CustomTkinter)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange?logo=mysql)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-9cf)
![License: MIT](https://img.shields.io/badge/License-MIT-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)

A modern GUI-based **Employee Management System (EMS)** built using:

-   Python
-   CustomTkinter (modern UI wrapper for Tkinter)
-   MySQL database (via `pymysql`)
-   Pillow (image support)

The application supports login authentication and provides CRUD (Create,
Read, Update, Delete) operations for employee management.

------------------------------------------------------------------------

## 📸 Screenshots

> *(Add images from your project folder here --- example formatting
> below)*

    screenshots/
    │── login_page.jpg
    │── ems_dashboard.jpg

Add them like this in README:

``` markdown
![Login Screen](screenshots/login_screen.jpg)
![EMS Dashboard](screenshots/ems_dashboard.jpg)
```

------------------------------------------------------------------------

## 🚀 Features

  -----------------------------------------------------------------------
  Feature                     Description
  --------------------------- -------------------------------------------
  🔐 Login Authentication     Only authorized users can access EMS
                              dashboard

  ➕ Add Employee             Insert employee records into MySQL database

  ✏️ Update Employee          Modify existing employee details

  ❌ Delete Employee          Delete single or all records

  🔍 Search Employees         Search by Id, Name, Role, Gender, Salary

  📋 TreeView Table           Displays employees in modern tabular format

  🗄️ MySQL Integration        Records are stored permanently
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🛠️ Tech Stack

  Tool/Library      Usage
  ----------------- ------------------------
  Python            Main language
  CustomTkinter     Modern GUI for Tkinter
  Pillow (PIL)      Image rendering
  MySQL + PyMySQL   Database backend

------------------------------------------------------------------------

## 📂 Project Structure

    Employee-Management-System/
│
├── main.py                 # Main GUI (Login + EMS)
├── database.py             # MySQL database operations
├── employee_data.sql       # MySQL DB structure/data export
├── image.jpg               # Login background image
├── image5.jpg              # EMS banner/header
├── README.md               # Project documentation for GitHub
├── LICENSE                 # MIT License (or whichever you choose)
├── requirements.txt        # Python dependencies (optional)
│
└── screenshots/            # OPTIONAL (only if you have images for readme)
      ├── login_page.png
      ├── ems_dashboard.png
------------------------------------------------------------------------

## ⚙️ Setup Instructions

### ✅ 1. Install Required Libraries

``` sh
pip install customtkinter pillow pymysql
```

------------------------------------------------------------------------

### ✅ 2. Configure MySQL Connection

Open `database.py` and update your database password:

``` python
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Your Password'
)
```

> The database (`employee_data`) and table (`data`) are auto-created
> when the program first runs.

Table schema:

``` sql
CREATE TABLE data (
    Id VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(50),
    Phone VARCHAR(10),
    Role VARCHAR(50),
    Gender VARCHAR(10),
    Salary DECIMAL(10,2)
);
```

------------------------------------------------------------------------

### ✅ 3. Run the Application

``` sh
python main.py
```

------------------------------------------------------------------------

## 🔑 Default Login Credentials

    Username: Jyoti
    Password: 123456

------------------------------------------------------------------------

## 🔐 Security Notes

-   Change login credentials in `main.py` before using in production
-   Never upload your database password to public repositories

------------------------------------------------------------------------

## ✨ Future Enhancements

-   Export data to CSV/PDF
-   Add employee profile photo
-   Add hashed login system with multiple user accounts

------------------------------------------------------------------------

## 🤝 Contributing

Pull requests are welcome --- fork the repository and submit changes.

------------------------------------------------------------------------

## 📄 License

This project is licensed under the **MIT License**.\
Feel free to modify and build upon it.

------------------------------------------------------------------------

### ⭐ If this project helped you, please give the repository a star on GitHub!
