# School Management System

A desktop-based **School Management System** developed in **Python** using **Tkinter** and **ttkbootstrap**. The application provides an intuitive graphical interface for managing student and teacher records, user accounts, application settings, and activity history.

The project stores data using Python's **Pickle (`.bin`)** files and supports profile image management for both students and teachers. For ease of use, a **Windows installer** is included, allowing users to install and run the application without configuring a Python environment.

---

# Features

## Student Management

* View students class-wise (Class 1–12)
* Add new student records
* Edit student information
* Delete student records
* Search students by name
* Upload and update student profile photographs
* Automatic roll number management
* Scrollable student information panel

---

## Teacher Management

* View teacher records
* Add new teacher records
* Edit teacher information
* Delete teacher records
* Search teachers
* Upload teacher profile photographs

Teacher records include:

* Name
* Teacher ID
* Subject
* Qualification
* Phone Number
* Salary
* Email Address
* Address
* Profile Photograph

---

## User Authentication

* Login system for authorized users
* Secure user verification
* User management from the settings panel

---

## Activity History

The software automatically records important activities, including:

* Student additions
* Student edits
* Student deletions
* Teacher additions and modifications
* Search operations
* Settings changes

History is automatically saved when the application closes.

---

## Settings

* Change application theme
* Manage users
* Change password
* Change project data location

---

## Modern Themes

The application uses **ttkbootstrap**, providing several modern UI themes, including:

* Cosmo
* Lumen
* Morph
* Solar
* Superhero
* Darkly
* Cyborg
* Vapor

---

# Technologies Used

* Python 3
* Tkinter
* ttkbootstrap
* Pillow (PIL)
* Pickle
* OS Module
* shutil
* tkinter.messagebox

---

# Project Structure

```
School Management System
│
├── School GUI.py
├── School GUI Installer.exe
├── README.md
│
└── class 12 project data/
    ├── Basic info.bin
    ├── History.bin
    ├── teacher.bin
    ├── class1.bin
    ├── class2.bin
    ├── ...
    ├── class12.bin
    ├── Profile Images/
    └── Application Icons/
```

---

# Data Storage

The project stores all records using **Pickle (.bin)** files.

Examples:

```
Basic info.bin
History.bin
teacher.bin
class1.bin
class2.bin
...
class12.bin
```

Student and teacher profile photographs are stored separately as image files.

---

# Installation

## Option 1 – Using the Windows Installer (Recommended)

The project includes a Windows installer:

```
School GUI Installer.exe
```

Simply run the installer and follow the installation wizard.

After successful installation, the application executable:

```
School GUI.exe
```

is created automatically and can be launched directly without installing Python or any external libraries.

> **Note:** The installer is intended for Windows operating systems.

---

## Option 2 – Running from Source Code

Install the required libraries:

```bash
pip install ttkbootstrap pillow
```

Tkinter is included with most standard Python installations.

Run the application:

```bash
python "School GUI.py"
```

---

# Student Information Stored

Each student record contains:

* Student Name
* Roll Number
* Father's Name
* Mother's Name
* Email Address
* Phone Number
* Address
* Aadhaar Number
* Profile Photograph

---

# Teacher Information Stored

Each teacher record contains:

* Teacher Name
* Teacher ID
* Subject
* Qualification
* Phone Number
* Salary
* Email Address
* Address
* Profile Photograph

---

# Application Modules

The software includes the following modules:

* Login
* Student Management
* Teacher Management
* Search
* Add Student
* Edit Student
* Delete Student
* Add Teacher
* Edit Teacher
* Delete Teacher
* Settings
* History Viewer

---

# Input Validation

The application validates user inputs, including:

* Required fields
* Phone number length
* Aadhaar number length
* Numeric-only fields
* Duplicate record prevention where applicable

---

# Future Enhancements

Possible future improvements include:

* Attendance Management
* Fee Management
* Result Management
* School Administration Module
* SQLite/MySQL Database Integration
* Report Card Generation
* User Roles and Permissions
* Backup and Restore Functionality

---

# Libraries Used

* tkinter
* ttkbootstrap
* Pillow
* pickle
* os
* shutil
* time

---

# Learning Outcomes

This project demonstrates practical implementation of:

* Python GUI Development
* Event-Driven Programming
* CRUD Operations
* File Handling using Pickle
* Image Handling
* Data Validation
* User Authentication
* Theme Customization
* School Record Management

---

# Author

**School Management System**

A Python desktop application developed as an academic project to simplify the management of student and teacher records through a user-friendly graphical interface.
