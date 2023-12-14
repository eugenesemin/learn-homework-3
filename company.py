"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


# 1. Вывести названия всех отделов

dep_list=[]
for deps in departments:
    if deps['title'] not in dep_list: 
        dep_list.append(deps['title'])
    else:
        pass

print(dep_list, '\n')

# 2. Вывести имена всех сотрудников компании.

employee_list=[]
for deps in departments:
    for a in deps['employers']:
        b= (a.get('first_name'), a.get('last_name'))
        if b not in employee_list:
            employee_list.append(b)
        else:
            pass

print(employee_list, '\n')

# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.

employee_list=[]
for deps in departments:
    for a in deps['employers']:
        b= (a.get('first_name'), a.get('last_name'), deps.get('title'))
        if b not in employee_list:
            employee_list.append(b)
        else:
            pass

print(employee_list, '\n')

# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.

employee_list=[]
for deps in departments:
    for a in deps['employers']:
        b= (a.get('first_name'), a.get('last_name'))
        c=a.get('salary_rub')
        if c>=100000:
            employee_list.append(b)
        else:
            pass

print(employee_list, '\n')

# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).

position_list=[]
for deps in departments:
    for a in deps['employers']:
        c=a.get('salary_rub')
        d=a.get('position')
        if c<80000 and d not in position_list:
            position_list.append(d)
        else:
            pass

print(position_list, '\n')

# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

dep_salary=[]
for deps in departments:
    title=deps['title']
    salary=0
    for a in deps['employers']:
        salary+=a.get("salary_rub")
    dep_salary.append((title,salary))
print(dep_salary, '\n')


# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.

min_salary_list=[]
for deps in departments:
    title=deps['title']
    salary=[]
    for a in deps['employers']:
        salary.append(a.get("salary_rub"))
    min_salary=min(salary)
    min_salary_list.append((title,min_salary))
print(min_salary_list, '\n')

# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.

salary_list=[]
for deps in departments:
    title=deps['title']
    salary=[]
    for a in deps['employers']:
        salary.append(a.get("salary_rub"))
    min_salary=min(salary)
    max_salary=max(salary)
    avg_salary=sum(salary)/len(salary)
    deps_salary_dict={'title':title, 'min_salary':min_salary, 'max_salary':max_salary, 'avg_salary':avg_salary}
    salary_list.append(deps_salary_dict)
print(salary_list, '\n')

# 9. Вывести среднюю зарплату по всей компании.

salary_list=[]
for deps in departments:
    for a in deps['employers']:
        salary.append(a.get("salary_rub"))
avg_salary=sum(salary)/len(salary)
print(avg_salary, '\n')

# 10. Вывести названия должностей, которые получают больше 90к без повторений.

position_list=[]
for deps in departments:
    for a in deps['employers']:
        c=a.get('salary_rub')
        d=a.get('position')
        if c>90000 and d not in position_list:
            position_list.append(d)
        else:
            pass

print(position_list, '\n')

# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).

woman_list=['Michelle', 'Nicole', 'Christina', 'Caitlin']

salary_list=[]
for deps in departments:
    title=deps['title']
    salary=[]
    for a in deps['employers']:
        if a['first_name'] in woman_list:
            salary.append(a.get("salary_rub"))
        else:
            pass
    avg_salary=sum(salary)/len(salary)
    salary_list.append((title, avg_salary))
print(salary_list, '\n')

# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

employee_list=[]
vse_gls = ['a', 'e', 'i', 'o', 'u', 'y']

for deps in departments:
    for a in deps['employers']:
        b= (a.get('first_name'), a.get('last_name'))
        if b not in employee_list and a.get('last_name')[-1] in vse_gls:
            employee_list.append(b)
        else:
            pass

print(employee_list, '\n')


# 13. Вывести список отделов со средним налогом на сотрудников этого отдела.

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

def add_taxes_to_departments(departments, taxes):
    for dep in departments:
        dep_tax_list=[]
        for tax in taxes:
            if tax.get("department") is None:
                x=tax.get('value_percents')
                dep_tax_list.append(x)
            elif tax.get("department").lower()==dep.get("title").lower():
                y=tax.get('value_percents')
                dep_tax_list.append(y)
            else:
                pass
        dep['taxes']=dep_tax_list
    return departments

dep_tax_info=[]
departments=add_taxes_to_departments(departments, taxes)


for dep in departments:
    dep_avg_tax=(dep.get("title"), sum(dep.get('taxes'))/len(dep.get('taxes')))
    dep_tax_info.append(dep_avg_tax)
print(dep_tax_info, '\n')

# 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.

departments=add_taxes_to_departments(departments, taxes)

employee_salary_list=[]
for deps in departments:
    for a in deps['employers']:
        name= f"{a.get('first_name')} {a.get('last_name')}"
        emp_salary=a.get("salary_rub")
        emp_salary_gross=emp_salary*(100-sum(deps.get('taxes')))/100
        output=(name, emp_salary_gross)
        employee_salary_list.append(output)

print(employee_salary_list, '\n')

# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.

departments=add_taxes_to_departments(departments, taxes)

dep_list=[]
for deps in departments:
    if deps['title'] not in dep_list: 
        dep_title=deps['title']
        dep_tax=sum(deps['taxes'])
        output=(dep_title,dep_tax)
        dep_list.append(output)
    else:
        pass

print(sorted(dep_list, key=lambda dep_list: dep_list[1], reverse=True), '\n')

# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.

departments=add_taxes_to_departments(departments, taxes)

employee_list=[]
for deps in departments:
    for a in deps['employers']:
        name= f"{a.get('first_name')} {a.get('last_name')}"
        emp_tax_gross=12*a.get("salary_rub")*(sum(deps.get('taxes')))/100
        output=(name, emp_tax_gross)
        if emp_tax_gross>100000:
            employee_list.append(output)
        else:
            pass

print(employee_list, '\n')

# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.

departments=add_taxes_to_departments(departments, taxes)

employee_list=[]
for deps in departments:
    for a in deps['employers']:
        name= f"{a.get('first_name')} {a.get('last_name')}"
        emp_tax_gross=a.get("salary_rub")*(sum(deps.get('taxes')))/100
        output=(name, emp_tax_gross)
        employee_list.append(output)

employee_list=sorted(employee_list, key=lambda employee_list: employee_list[1], reverse=False)[0]
print(employee_list, '\n')