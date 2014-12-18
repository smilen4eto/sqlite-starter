import sqlite3


conn = sqlite3.connect("mydatabase.db")
c = conn.cursor()

c.execute('''create table if not exists employees
                        (id INTEGER PRIMARY KEY,
                         name text,
                         monthly_salary integer,
                         early_bonus integer,
                         position text)'''
)

information =  [('Ivan Ivanov','5000','10000','Software Developer'),
                ('Rado Rado', '500', '0', 'Technical Support Intern'),
                ('Ivo IVo','10000', '100000', 'CEO'),
                ('Petar Petrov', '3000','1000', 'Marketing Manager'),
                ('Maria Georgieva','8000' ,'10000', 'COO')]

c.executemany("insert into employees(name, monthly_salary, early_bonus, position) values (?,?,?,?)", information)

for row in c.execute("select * from employees"):
    print(row)

choice = input("Choose an option:")

if choice == "list_employees":
    for row in c.execute("select name, position from employees;"):
        print(row)

elif choice == "monthly_spending":
    for row in c.execute("select sum(monthly_salary) as mon_salary from employees"):
        print(row)

elif choice == "yearly_spending":
    for row in c.execute("select sum(monthly_salary)*12 as mon_salary from employees"):
        print(row)

elif choice == "add_employee":
    name = input("What is the name?")
    salary = input("Salary?")
    bonus = input("Bonus?")
    position = input("Name of the position?")
    c.execute ("insert into employees(name, monthly_salary, early_bonus, position) values (?,?,?,?)", (name, salary, bonus, position))

elif choice == "delete_employee":
    id_empl = input("Id of the employee?")
    c.execute("delete from employees where id = ?", id_empl)

elif choice == "update_employee":
    id_empl = input("Id of the employee?")
    n_name = input("What is the name?")
    salary = input("Salary?")
    bonus = input("Bonus?")
    n_position = input("Name of the position?")
    c.execute("update employees set name = ?, monthly_salary = ?, early_bonus = ?, position = ? where id = ?", (n_name, salary, bonus, n_position, id_empl))

for row in c.execute("select * from employees"):
    print(row)
