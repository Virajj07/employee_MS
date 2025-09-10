# Employee Management System - MySQL Implementation

This is a Python-based employee management system that uses MySQL as the database backend.

## Features

- **Employee Management**: Add, view, update, and delete employee records
- **Department Management**: View departments and associate employees with departments
- **Search Functionality**: Search employees by name or email
- **Data Validation**: Basic input validation and error handling
- **Command Line Interface**: Easy-to-use interactive menu system

## Prerequisites

- Python 3.6 or higher
- MySQL Server 5.7 or higher
- pip package manager

## Installation & Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up MySQL database**:
   - Start your MySQL server
   - Run the database schema script:
   ```bash
   mysql -u root -p < database/schema.sql
   ```

3. **Configure database connection**:
   - Copy `.env.example` to `.env`
   - Update the database credentials in the `.env` file:
   ```
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=employee_management
   DB_PORT=3306
   ```

4. **Run the application**:
   ```bash
   python src/main.py
   ```

## Usage

The application provides an interactive command-line interface with the following options:

1. **Add New Employee**: Enter employee details including name, email, department, position, and salary
2. **View All Employees**: Display a list of all active employees
3. **Search Employee**: Find employees by name or email
4. **Update Employee**: Modify existing employee information
5. **Delete Employee**: Deactivate an employee record (soft delete)
6. **View Departments**: List all available departments

## Database Schema

### Employees Table
- `employee_id`: Primary key (auto-increment)
- `first_name`: Employee's first name
- `last_name`: Employee's last name  
- `email`: Unique email address
- `phone`: Contact phone number (optional)
- `department_id`: Foreign key to departments table
- `position`: Job title/position
- `salary`: Employee salary
- `hire_date`: Date of hiring
- `status`: Employee status (active/inactive)
- `created_at`, `updated_at`: Timestamps

### Departments Table
- `department_id`: Primary key (auto-increment)
- `department_name`: Department name (unique)
- `created_at`: Creation timestamp

## Sample Data

The database schema includes sample departments:
- Human Resources
- Information Technology
- Finance
- Marketing
- Operations

And sample employees for demonstration purposes.

## Error Handling

The application includes comprehensive error handling for:
- Database connection issues
- Invalid input validation
- SQL execution errors
- Missing employee records

## Future Enhancements

Potential improvements could include:
- Web-based interface
- Advanced reporting features
- Employee photo management
- Role-based access control
- Backup and restore functionality
- Email notifications

## Contributing

This is a basic implementation intended for learning and demonstration purposes. Feel free to extend and improve the functionality.