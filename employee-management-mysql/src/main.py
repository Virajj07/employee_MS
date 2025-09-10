#!/usr/bin/env python3
"""
Employee Management System
A simple command-line application for managing employee records with MySQL database.
"""

import sys
import os
from datetime import datetime

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from employee import Employee, EmployeeManager

class EmployeeManagementApp:
    def __init__(self):
        self.employee_manager = EmployeeManager()
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("    EMPLOYEE MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. View Departments")
        print("0. Exit")
        print("-"*50)
    
    def add_employee(self):
        """Add a new employee"""
        print("\n--- Add New Employee ---")
        try:
            first_name = input("First Name: ").strip()
            last_name = input("Last Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone (optional): ").strip() or None
            
            # Show departments
            departments = self.employee_manager.get_departments()
            if departments:
                print("\nAvailable Departments:")
                for dept in departments:
                    print(f"{dept['department_id']}. {dept['department_name']}")
                
                dept_input = input("Department ID (optional): ").strip()
                department_id = int(dept_input) if dept_input else None
            else:
                department_id = None
            
            position = input("Position (optional): ").strip() or None
            salary_input = input("Salary (optional): ").strip()
            salary = float(salary_input) if salary_input else None
            
            hire_date_input = input("Hire Date (YYYY-MM-DD, optional): ").strip()
            hire_date = datetime.strptime(hire_date_input, "%Y-%m-%d").date() if hire_date_input else None
            
            employee = Employee(first_name, last_name, email, phone, department_id, position, salary, hire_date)
            self.employee_manager.add_employee(employee)
            
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error adding employee: {e}")
    
    def view_all_employees(self):
        """Display all employees"""
        print("\n--- All Employees ---")
        employees = self.employee_manager.get_all_employees()
        
        if not employees:
            print("No employees found.")
            return
        
        print(f"{'ID':<5} {'Name':<25} {'Email':<30} {'Department':<20} {'Position':<20}")
        print("-" * 100)
        
        for emp in employees:
            name = f"{emp['first_name']} {emp['last_name']}"
            dept_name = emp['department_name'] or "N/A"
            position = emp['position'] or "N/A"
            print(f"{emp['employee_id']:<5} {name:<25} {emp['email']:<30} {dept_name:<20} {position:<20}")
    
    def search_employee(self):
        """Search for employees"""
        print("\n--- Search Employee ---")
        search_term = input("Enter search term (name or email): ").strip()
        
        if not search_term:
            print("Search term cannot be empty.")
            return
        
        employees = self.employee_manager.search_employees(search_term)
        
        if not employees:
            print("No employees found matching your search.")
            return
        
        print(f"\nFound {len(employees)} employee(s):")
        print(f"{'ID':<5} {'Name':<25} {'Email':<30} {'Department':<20} {'Position':<20}")
        print("-" * 100)
        
        for emp in employees:
            name = f"{emp['first_name']} {emp['last_name']}"
            dept_name = emp['department_name'] or "N/A"
            position = emp['position'] or "N/A"
            print(f"{emp['employee_id']:<5} {name:<25} {emp['email']:<30} {dept_name:<20} {position:<20}")
    
    def update_employee(self):
        """Update employee information"""
        print("\n--- Update Employee ---")
        try:
            emp_id = int(input("Enter Employee ID to update: "))
            
            employee = self.employee_manager.get_employee_by_id(emp_id)
            if not employee:
                print("Employee not found.")
                return
            
            print(f"\nCurrent employee details:")
            print(f"Name: {employee['first_name']} {employee['last_name']}")
            print(f"Email: {employee['email']}")
            print(f"Department: {employee['department_name'] or 'N/A'}")
            print(f"Position: {employee['position'] or 'N/A'}")
            
            print("\nEnter new values (press Enter to keep current value):")
            
            updates = {}
            
            new_first_name = input(f"First Name ({employee['first_name']}): ").strip()
            if new_first_name:
                updates['first_name'] = new_first_name
            
            new_last_name = input(f"Last Name ({employee['last_name']}): ").strip()
            if new_last_name:
                updates['last_name'] = new_last_name
            
            new_email = input(f"Email ({employee['email']}): ").strip()
            if new_email:
                updates['email'] = new_email
            
            new_position = input(f"Position ({employee['position'] or 'N/A'}): ").strip()
            if new_position:
                updates['position'] = new_position
            
            if updates:
                self.employee_manager.update_employee(emp_id, **updates)
            else:
                print("No changes made.")
                
        except ValueError:
            print("Invalid Employee ID.")
        except Exception as e:
            print(f"Error updating employee: {e}")
    
    def delete_employee(self):
        """Delete (deactivate) an employee"""
        print("\n--- Delete Employee ---")
        try:
            emp_id = int(input("Enter Employee ID to delete: "))
            
            employee = self.employee_manager.get_employee_by_id(emp_id)
            if not employee:
                print("Employee not found.")
                return
            
            print(f"Employee: {employee['first_name']} {employee['last_name']} ({employee['email']})")
            confirm = input("Are you sure you want to delete this employee? (y/N): ").strip().lower()
            
            if confirm == 'y':
                self.employee_manager.delete_employee(emp_id)
            else:
                print("Delete cancelled.")
                
        except ValueError:
            print("Invalid Employee ID.")
        except Exception as e:
            print(f"Error deleting employee: {e}")
    
    def view_departments(self):
        """Display all departments"""
        print("\n--- Departments ---")
        departments = self.employee_manager.get_departments()
        
        if not departments:
            print("No departments found.")
            return
        
        print(f"{'ID':<5} {'Department Name':<30}")
        print("-" * 35)
        
        for dept in departments:
            print(f"{dept['department_id']:<5} {dept['department_name']:<30}")
    
    def run(self):
        """Main application loop"""
        print("Welcome to the Employee Management System!")
        print("Please ensure your MySQL database is set up and running.")
        
        try:
            while True:
                self.display_menu()
                choice = input("Enter your choice (0-6): ").strip()
                
                if choice == '1':
                    self.add_employee()
                elif choice == '2':
                    self.view_all_employees()
                elif choice == '3':
                    self.search_employee()
                elif choice == '4':
                    self.update_employee()
                elif choice == '5':
                    self.delete_employee()
                elif choice == '6':
                    self.view_departments()
                elif choice == '0':
                    print("Thank you for using Employee Management System!")
                    break
                else:
                    print("Invalid choice. Please try again.")
                
                input("\nPress Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\nApplication interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.employee_manager.close()

if __name__ == "__main__":
    app = EmployeeManagementApp()
    app.run()