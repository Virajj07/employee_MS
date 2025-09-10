-- Employee Management System Database Schema
-- MySQL Database Setup

CREATE DATABASE IF NOT EXISTS employee_management;
USE employee_management;

-- Departments table
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    department_id INT,
    position VARCHAR(100),
    salary DECIMAL(10, 2),
    hire_date DATE,
    status ENUM('active', 'inactive') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE SET NULL
);

-- Insert some default departments
INSERT INTO departments (department_name) VALUES 
    ('Human Resources'),
    ('Information Technology'),
    ('Finance'),
    ('Marketing'),
    ('Operations')
ON DUPLICATE KEY UPDATE department_name = department_name;

-- Insert some sample employees (optional)
INSERT INTO employees (first_name, last_name, email, department_id, position, salary, hire_date) VALUES
    ('John', 'Doe', 'john.doe@company.com', 2, 'Software Developer', 75000.00, '2023-01-15'),
    ('Jane', 'Smith', 'jane.smith@company.com', 1, 'HR Manager', 65000.00, '2022-11-20'),
    ('Mike', 'Johnson', 'mike.johnson@company.com', 3, 'Financial Analyst', 60000.00, '2023-03-10')
ON DUPLICATE KEY UPDATE first_name = first_name;