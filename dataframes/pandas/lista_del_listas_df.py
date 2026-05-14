import json

import pandas as pd

salary_data = [
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9002, "Salary": 2800},
    {"Empno": 9003, "Salary": 2500},
]

emp_data = [
    ["9001","Huguinho","Sales"],
    ["9002","Zezinho","Sales"],
    ["9003","Luizinho","Sales"],
]

orders_data = [
    [2608, 9001, 35],
    [2617, 9001, 35],
    [2620, 9001, 139],
    [2621, 9002, 95],
    [2626, 9002, 218],
]

json_data = json.dumps(salary_data)

salary = pd.read_json(json_data)

salary = salary.set_index("Empno")




emps = pd.DataFrame(emp_data, columns=["Empno","Name","Job"])

column_types = {"Empno": int,"Name":str, "Job": str }

emps = emps.astype(column_types)

emps = emps.set_index("Empno")

orders = pd.DataFrame(orders_data, columns=["Pono", "Empno", "Total"])

print(salary)
print(emps)

emps_salary = emps.join(salary,how='outer')

print(emps_salary)
print(orders)

emps_salary = emps.join(salary)

emp_orders = emps_salary.merge(
    orders, how="inner", left_on="Empno", right_on="Empno"
).set_index("Pono")

print(emp_orders)

print(f"Média: ", emp_orders.groupby(["Empno"])['Total'].mean())
print(f"Soma: ", emp_orders.groupby(["Empno"])['Total'].sum())
print(f"Soma: ", emp_orders.groupby(["Name"])['Total'].sum())