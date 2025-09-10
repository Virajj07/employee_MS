# Employee Management System - MySQL Implementation

This directory contains a Python-based employee management system with MySQL database integration.

## Structure
- `database/` - Database schema and initialization scripts
- `src/` - Application source code
- `config/` - Configuration files
- `requirements.txt` - Python dependencies

## Database Schema
The system manages employees with the following basic structure:
- Employee ID (Primary Key)
- First Name
- Last Name
- Email
- Department
- Position
- Salary
- Hire Date

## Setup Instructions
1. Install Python dependencies: `pip install -r requirements.txt`
2. Set up MySQL database using scripts in `database/`
3. Configure database connection in `config/database.py`
4. Run the application: `python src/main.py`

## Usage
The system provides a simple command-line interface for managing employees:
- Add new employees
- View employee list
- Update employee information
- Delete employees
- Search employees by various criteria