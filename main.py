import pandas as pd
import numpy as np
from data import data

#task 1
def task1():
    print(f"1\n")
    #sub-task 1.1
    my_series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    print(f"Series:\n{my_series}\n")

    #sub-task 1.2
    data = {
        'Имя': ['Иван', 'Антон', 'Виктор', 'Маша'],
        'Возраст': [20, 27, 14, 45],
        'Город': ['Тула', 'Щекино', 'Воронеж', 'Москва']
    }
    df_ts1 = pd.DataFrame(data)
    print(f"DataFrame:\n{df_ts1}\n")

    #sub-task 1.3
    print(f"Первые строки:\n{df_ts1.head()}\n")
    print(f"Последние строки:\n{df_ts1.tail()}\n")
    print("Информация о типах данных:")
    df_ts1.info()
    print(f"\nСтатистика:\n{df_ts1.describe()}\n")

#task 2
def task2():
    print(f"2\n")
    df = pd.DataFrame(data)
    
    #sub-task 2.1
    it_employees = df[df['department'] == 'IT'][['name', 'salary']]
    print(f"Сотрудники IT отдела:\n{it_employees}\n")

    #sub-task 2.2
    first_rows_cols = df.iloc[:3, :2]
    print(f"Первые 3 строки и 2 столбца:\n{first_rows_cols}\n")

    #sub-task 2.3
    high = df[df['salary'] > 70000]
    print(f"Сотрудники с зарплатой выше 70000:\n{high}\n")

    #sub-task 2.4
    df['total_comp'] = df['salary'] + df['bonus'].fillna(0)
    print(f"DataFrame с новым столбцом\n{df}\n")

    #sub-task 2.5
    df = df.drop('hire_date', axis=1)
    print(f"DataFrame после удаления столбца:\n{df}\n")

#task 3
def task3():
    print(f"3\n")
    df = pd.DataFrame(data)

    #sub-task 3.1
    missing = df.isna().sum()
    print(f"Количество пропусков:\n{missing}\n")

    #sub-task 3.2
    df['salary'] = df['salary'].fillna(df.groupby('department')['salary'].transform('mean'))
    print(f"DataFrame после заполнения пропусков:\n{df}\n")

    #sub-task 3.3
    df['bonus'] = df['bonus'].fillna(0)
    print(f"DataFrame после заполнения пропусков:\n{df}\n")

#task 4
def task4():
    print(f"4\n")
    df = pd.DataFrame(data)

    #sub-task 4.1
    avg_salary = df.groupby('department')['salary'].mean()
    print(f"Средняя зарплата:\n{avg_salary}\n")

    #sub-task 4.2
    dept_stats = df.groupby('department').agg(
        avg_salary=('salary', 'mean'),
        max_bonus=('bonus', 'max'),
        employee_count=('name', 'count')
    )
    print(f"Статистика по отделам:\n{dept_stats}\n")

    #sub-task 4.3
    table = df.pivot_table(index='department', values='salary', aggfunc='mean')
    print(f"Сводная таблица:\n{table}\n")

    #sub-task 4.4
    sorted = avg_salary.sort_values(ascending=False)
    print(f"Отделы по средней зарплате:\n{sorted}\n")

#task 5
def task5():
    print(f"5\n")
    df = pd.DataFrame(data)

    #sub-task 5.1
    managers_data = {
        'department': ['IT', 'HR', 'Finance', 'Marketing'],
        'manager': ['Jacob', 'Lucia', 'Noelle', 'Jeff']
    }
    managers = pd.DataFrame(managers_data)
    print(f"DataFrame с менеджерами:\n{managers}\n")

    #sub-task 5.2
    df = pd.merge(df, managers, on='department', how='left')
    print(f"Объединенный DataFrame:\n{df}\n")

    #sub-task 5.3
    new_employee = pd.DataFrame([{
        'name': 'Peter',
        'department': 'IT',
        'salary': 95000,
        'bonus': 7000,
        'hire_date': pd.to_datetime('2026-11-25'),
        'manager': 'Jacob'
    }])
    df = pd.concat([df, new_employee])
    print(f"DataFrame после добавления нового сотрудника:\n{df}\n")

    #sub-task 5.4
    df = df.reset_index(drop=True)
    print(f"DataFrame после сброса индекса:\n{df}\n")

    df['total_comp'] = df['salary'] + df['bonus'].fillna(0)

    return df

#task 6
def task6():
    df = task5()

    input("Нажмите для продолжения...")
    print(f"6\n")

    #sub-task 6.1
    top = df.sort_values(by='total_comp', ascending=False).head(3)
    print(f"Топ 3 сотрудников по общей компенсации:\n{top}\n")

    #sub-task 6.2
    avg = df.groupby('department')[['salary', 'bonus']].mean()
    print(f"Средняя зарплата и бонус по отделам:\n{avg}\n")

    #sub-task 6.3
    above = (df['salary'] > 75000).groupby(df['department']).mean()
    print(f"Доля сотрудников с зарплатой выше 75000 по отделам:\n{above}\n")

task1()
input("Нажмите для продолжения...")
task2()
input("Нажмите для продолжения...")
task3()
input("Нажмите для продолжения...")
task4()
input("Нажмите для продолжения...")
task6()