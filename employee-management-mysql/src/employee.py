from datetime import datetime
from database import DatabaseManager

class Employee:
    def __init__(self, first_name, last_name, email, phone=None, department_id=None, 
                 position=None, salary=None, hire_date=None, employee_id=None, status='active'):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.department_id = department_id
        self.position = position
        self.salary = salary
        self.hire_date = hire_date if hire_date else datetime.now().date()
        self.status = status
    
    def __str__(self):
        return f"Employee(ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Email: {self.email})"

class EmployeeManager:
    def __init__(self):
        self.db = DatabaseManager()
        self.db.connect()
    
    def add_employee(self, employee):
        """Add a new employee to the database"""
        query = """
        INSERT INTO employees (first_name, last_name, email, phone, department_id, 
                              position, salary, hire_date, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (employee.first_name, employee.last_name, employee.email, 
                 employee.phone, employee.department_id, employee.position,
                 employee.salary, employee.hire_date, employee.status)
        
        if self.db.execute_query(query, params):
            print(f"Employee {employee.first_name} {employee.last_name} added successfully!")
            return True
        return False
    
    def get_all_employees(self):
        """Retrieve all employees from the database"""
        query = """
        SELECT e.*, d.department_name 
        FROM employees e 
        LEFT JOIN departments d ON e.department_id = d.department_id
        WHERE e.status = 'active'
        ORDER BY e.last_name, e.first_name
        """
        return self.db.fetch_query(query)
    
    def get_employee_by_id(self, employee_id):
        """Retrieve a specific employee by ID"""
        query = """
        SELECT e.*, d.department_name 
        FROM employees e 
        LEFT JOIN departments d ON e.department_id = d.department_id
        WHERE e.employee_id = %s
        """
        result = self.db.fetch_query(query, (employee_id,))
        return result[0] if result else None
    
    def update_employee(self, employee_id, **kwargs):
        """Update employee information"""
        # Build dynamic update query based on provided fields
        set_clauses = []
        params = []
        
        for field, value in kwargs.items():
            if field in ['first_name', 'last_name', 'email', 'phone', 'department_id', 
                        'position', 'salary', 'hire_date', 'status']:
                set_clauses.append(f"{field} = %s")
                params.append(value)
        
        if not set_clauses:
            print("No valid fields provided for update")
            return False
        
        query = f"UPDATE employees SET {', '.join(set_clauses)} WHERE employee_id = %s"
        params.append(employee_id)
        
        if self.db.execute_query(query, params):
            print(f"Employee ID {employee_id} updated successfully!")
            return True
        return False
    
    def delete_employee(self, employee_id):
        """Soft delete an employee (set status to inactive)"""
        query = "UPDATE employees SET status = 'inactive' WHERE employee_id = %s"
        if self.db.execute_query(query, (employee_id,)):
            print(f"Employee ID {employee_id} deactivated successfully!")
            return True
        return False
    
    def search_employees(self, search_term):
        """Search employees by name or email"""
        query = """
        SELECT e.*, d.department_name 
        FROM employees e 
        LEFT JOIN departments d ON e.department_id = d.department_id
        WHERE e.status = 'active' 
        AND (e.first_name LIKE %s OR e.last_name LIKE %s OR e.email LIKE %s)
        ORDER BY e.last_name, e.first_name
        """
        search_pattern = f"%{search_term}%"
        return self.db.fetch_query(query, (search_pattern, search_pattern, search_pattern))
    
    def get_departments(self):
        """Get all departments"""
        query = "SELECT * FROM departments ORDER BY department_name"
        return self.db.fetch_query(query)
    
    def close(self):
        """Close database connection"""
        self.db.disconnect()