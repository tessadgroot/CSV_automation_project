
# **CSV Automation & Data Cleaning Tool (Python)**
## 📌 Project Overview

This project is a small Python data engineering utility that automatically reads, combines, cleans, and exports sensor data stored in multiple CSV files.

The goal of this project is to demonstrate:

- Object-Oriented Programming (OOP)
- File automation
- Data cleaning with pandas
- Error handling and logging
- Writing clean, reusable Python code

This project was built as part of a structured learning path towards a software / data engineering role.


## 🧱 Project Architecture
    csv_tools/

    ├── reader.py        # CSV ingestion
    ├── cleaner.py       # Data cleaning & validation

    database/

    ├── db.py            # Database configuration
    ├── models.py        # SQLAlchemy ORM models
    ├── crud.py          # Database operations (CRUD)
    ├── init_db.py       # Database initialization

    main.py              # Pipeline orchestration


## ⚙️ Features

✔ Automatically reads multiple CSV files

✔ Combines all files into a single DataFrame

✔ Cleans and standardizes the data:
- Normalizes column names
- Removes empty rows
- Fixes incorrect data types
- Handles invalid timestamps
 
    ✔ Exports the cleaned dataset to an Excel file

    ✔ Logs important actions and errors

## 🗄️ Database & CRUD Integration (Update)

This project was extended with a persistent storage layer using SQLite and SQLAlchemy, transforming it from a standalone data-cleaning script into a complete data pipeline.
- Newly added functionality:
- SQLite database integration for persistent data storage
- SQLAlchemy ORM models to define and manage database tables
- Automatic database and table creation on startup
- Bulk insertion of cleaned sensor data into the database
- Full CRUD operations:
    - Create: Insert cleaned sensor data from pandas DataFrames
    - Read: Retrieve stored sensor records
    - Update: Modify sensor status values based on business rules
    - Delete: Remove invalid or unwanted records
- Centralized and robust database path handling using pathlib

This update demonstrates:
- Python ↔ SQL integration
- Practical use of ORMs
- Clean separation of concerns (ingestion, cleaning, persistence)
- Real-world data engineering workflow patterns