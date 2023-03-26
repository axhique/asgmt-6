import json

file=open('employee.json','r')
file_content=json.load(file)

    
class Employee():
    def __init__(self,name,dob,height,city,state):
        self.name=name
        self.dob=dob
        self.height=height
        self.city=city
        self.state=state
        
    def __str__(self):
        return f'Name:{self.name}\nDOB:{self.dob}\nHeight:{self.height}\nCity:{self.city}\nState:{self.state}'

employees=[]
for i in file_content['employees']:
    emp_obj=Employee(i['Name'],i['DOB'],i['Height'],i['City'],i['State'])
    employees.append(emp_obj)
    

for i in employees:
    print(i,'\n')  



