import pytest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import updateSalary,countEmployeeByDept,searchStudentByName,calculateTotalSalary  # Adjust the import based on your file structure

employees = [("Shivansh",50000,"CS"),("Kalindi",52000,"CS"),("Jiya",55000,"IT")]

def test_calculateTotalSalary():
    assert calculateTotalSalary(employees) == 157000
    
def test_searchStudentByNameTrue():
    empName = 'Shivansh'
    assert searchStudentByName(employees,empName)==True
    
def test_searchStudentByNameFalse():
    empName = 'Sumit'
    assert searchStudentByName(employees,empName)==False
      
def test_countEmployeeByDeptTrue():
    deptName = 'CS'
    assert countEmployeeByDept(employees,deptName) == 2
    
def test_countEmployeeByDeptFalse():
    deptName = 'Mech'
    assert countEmployeeByDept(employees,deptName) == 0
    
def test_updateSalary():
    emps = updateSalary(employees)
    for i in range(len(emps)):
      emp = list(emps[i])
      existing_emp = list(employees[i])
      existing_emp[1] += existing_emp[1] * 0.10
      assert emp[1] ==  existing_emp[1]
      

