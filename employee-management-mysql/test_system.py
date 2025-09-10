#!/usr/bin/env python3
"""
Simple test script for Employee Management System
Tests basic database connectivity and core functions
"""

import sys
import os
from datetime import datetime

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from employee import Employee, EmployeeManager
    print("✓ Successfully imported employee modules")
except ImportError as e:
    print(f"✗ Failed to import employee modules: {e}")
    sys.exit(1)

def test_database_connection():
    """Test database connection"""
    print("\n--- Testing Database Connection ---")
    try:
        emp_manager = EmployeeManager()
        print("✓ Database connection successful")
        return emp_manager
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        print("Please ensure MySQL is running and database is set up correctly")
        return None

def test_departments(emp_manager):
    """Test department retrieval"""
    print("\n--- Testing Department Retrieval ---")
    try:
        departments = emp_manager.get_departments()
        if departments:
            print(f"✓ Retrieved {len(departments)} departments:")
            for dept in departments:
                print(f"  - {dept['department_name']}")
        else:
            print("! No departments found")
        return True
    except Exception as e:
        print(f"✗ Failed to retrieve departments: {e}")
        return False

def test_employee_operations(emp_manager):
    """Test basic employee operations"""
    print("\n--- Testing Employee Operations ---")
    
    # Test adding an employee
    try:
        test_employee = Employee(
            first_name="Test",
            last_name="User", 
            email=f"test.user.{datetime.now().timestamp()}@company.com",
            position="Test Position",
            department_id=2,  # IT department
            salary=50000
        )
        
        success = emp_manager.add_employee(test_employee)
        if success:
            print("✓ Successfully added test employee")
        else:
            print("✗ Failed to add test employee")
            return False
            
    except Exception as e:
        print(f"✗ Error adding employee: {e}")
        return False
    
    # Test retrieving all employees
    try:
        employees = emp_manager.get_all_employees()
        if employees:
            print(f"✓ Retrieved {len(employees)} employees")
            
            # Find our test employee
            test_emp = None
            for emp in employees:
                if emp['first_name'] == 'Test' and emp['last_name'] == 'User':
                    test_emp = emp
                    break
            
            if test_emp:
                print(f"✓ Found test employee: {test_emp['first_name']} {test_emp['last_name']}")
                
                # Test updating the employee
                emp_manager.update_employee(test_emp['employee_id'], position="Updated Test Position")
                print("✓ Updated test employee")
                
                # Test deleting the employee
                emp_manager.delete_employee(test_emp['employee_id'])
                print("✓ Deleted test employee")
                
            else:
                print("! Could not find test employee in results")
        else:
            print("! No employees found")
            
    except Exception as e:
        print(f"✗ Error in employee operations: {e}")
        return False
    
    return True

def test_search_functionality(emp_manager):
    """Test employee search"""
    print("\n--- Testing Search Functionality ---")
    try:
        # Search for existing employees (should find sample data)
        results = emp_manager.search_employees("John")
        if results:
            print(f"✓ Search found {len(results)} employee(s) with 'John'")
        else:
            print("! No employees found in search")
        
        # Test empty search
        empty_results = emp_manager.search_employees("NonexistentEmployee123")
        if not empty_results:
            print("✓ Empty search returned no results as expected")
        else:
            print("! Unexpected results for non-existent search")
            
        return True
    except Exception as e:
        print(f"✗ Error in search functionality: {e}")
        return False

def main():
    """Run all tests"""
    print("Employee Management System - Basic Tests")
    print("="*50)
    
    # Test database connection
    emp_manager = test_database_connection()
    if not emp_manager:
        print("\n❌ Cannot proceed without database connection")
        return
    
    try:
        # Run tests
        tests_passed = 0
        total_tests = 4
        
        if test_departments(emp_manager):
            tests_passed += 1
            
        if test_employee_operations(emp_manager):
            tests_passed += 1
            
        if test_search_functionality(emp_manager):
            tests_passed += 1
            
        # Test connection close
        try:
            emp_manager.close()
            print("\n✓ Database connection closed successfully")
            tests_passed += 1
        except Exception as e:
            print(f"\n✗ Error closing database connection: {e}")
        
        # Summary
        print("\n" + "="*50)
        print(f"Test Results: {tests_passed}/{total_tests} passed")
        
        if tests_passed == total_tests:
            print("🎉 All tests passed! The system is working correctly.")
        else:
            print("⚠️  Some tests failed. Please check the error messages above.")
            
    except Exception as e:
        print(f"\n❌ Unexpected error during testing: {e}")
    finally:
        if emp_manager:
            try:
                emp_manager.close()
            except:
                pass

if __name__ == "__main__":
    main()