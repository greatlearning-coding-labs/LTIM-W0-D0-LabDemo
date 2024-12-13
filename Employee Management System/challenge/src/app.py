
def calculateTotalSalary(employees):
    '''
    Calculate and return the total salary of all employees.
    '''
    
    # write your code here
    totalSalary = 0
    for emp in employees:
      totalSalary += emp[1]
    return totalSalary
def searchStudentByName(employees,empName):
    '''
    Search for an employee in the list based on the given name and return True if the employee exists; otherwise, return False.
    '''
    for emp in employees:
      if emp[0] == empName:
        return True
    return False
        
def countEmployeeByDept(employees,deptName):
    '''
    Find the total number of employees in the given department and return the value of count.
    '''
    cnt = 0
    for emp in employees:
      if emp[2] == deptName:
        cnt += 1
    return cnt
    
    
    # write your code here
    
    
def updateSalary(employees):
    '''
    Apply a 10% increment to the salary of all employees and return the updated list of employees.
    '''
    updatedLst = [] # update salary and store a new list of employees into a list named updatedLst
    for emp in employees:
      emp = list(emp)
      emp[1] += emp[1] * 0.10
      updatedLst.append(tuple(emp))
      
    return updatedLst
    
