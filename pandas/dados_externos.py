import json
import pandas as pd

# já define a coluna e o dado
data = [
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9001, "Salary": 2800},
    {"Empno": 9001, "Salary": 2600},
]

json_data = json.dumps(data)

salary = pd.read_json(json_data)
salary = salary.set_index("Empno")
# salary = salary.reset_index()
print(salary)