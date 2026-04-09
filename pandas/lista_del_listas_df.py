import pandas as pd
import json

data = [
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9001, "Salary": 2800},
    {"Empno": 9001, "Salary": 2600},
]

json_data = json.dumps(data)

salary = pd.read_json(json_data)
salary = salary.set_index("Empno")
data=  [
    ["9001", "Huguinho", "Sales"],
    ["9002", "Zezinho", "Sales"],
    ["9003", "Luizinho", "Sales"],
]

emps = pd.DataFrame(data, columns=["Empno", "Name", "Job"])
column_types = {"Empno": int, "Name": str, "Job": str}
emps = emps.astype(column_types)
emps = emps.set_index("Empno")
print(emps)

emps_salary = emps.join(salary, how='in')
print(emps_salary)