from tkinter import *

import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='u0_a134',
                             db='example_crud',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()


def draw_edit_employee_window():
    root = Tk()
    root.title("Edit employee")
    root.config(width=500, height=200)
    employee_id_label = Label(root, text="Employee id ", fg="black")
    employee_id_label.place(x=50, y=30)
    employee_id_entry = Entry(root)
    employee_id_entry.place(x=50, y=60)

    new_name_label = Label(root, text="New employee name ", fg="black")
    new_name_label.place(x=50, y=90)
    new_name_entry = Entry(root)
    new_name_entry.place(x=50, y=120)

    new_salary_label = Label(root, text="New employee salary ", fg="black")
    new_salary_label.place(x=50, y=150)
    new_salary_entry = Entry(root)
    new_salary_entry.place(x=50, y=180)

    btn_add_employee = Button(root, text="Add employee",
                              command=lambda: update_employee(employee_id_entry.get(), new_name_entry.get(),
                                                              new_salary_entry.get(), root), bg="blue", fg="black",
                              width=15)
    btn_add_employee.place(x=50, y=210)
    mainloop()


def draw_add_employee_window():
    root = Tk()
    root.title("Add employee")
    root.config(width=500, height=200)
    name_label = Label(root, text="Employee name ", fg="black")
    name_label.place(x= 50, y= 30)
    name_entry = Entry(root)
    name_entry.place(x=50, y=60)

    salary_label = Label(root, text="Employee salary ", fg="black")
    salary_label.place(x= 50, y= 90)
    salary_entry = Entry(root)
    salary_entry.place(x=50, y=120)

    btn_add_employee = Button(root, text="Add employee",
                              command=lambda: add_employee(name_entry.get(), salary_entry.get(), root), bg="blue",
                              fg="black", width=15)
    btn_add_employee.place(x=50, y=150)

    mainloop()


def draw_find_employee_window():
    root = Tk()
    root.title("Find employee")
    root.config(width=500, height=200)
    id_label = Label(root, text="Employee id ", fg="black")
    id_label.place(x=50, y=30)
    id_entry = Entry(root)
    id_entry.place(x=50, y=60)
    btn_add_employee = Button(root, text="Find employee", command=lambda: find_employee(id_entry.get(), root),
                              bg="blue", fg="black", width=15)
    btn_add_employee.place(x=50, y=90)
    mainloop()


def draw_delete_employee_window():
    root = Tk()
    root.title("Delete employee")
    root.config(width=500, height=200)
    employee_id_label = Label(root, text="Employee id", fg="black")
    employee_id_label.place(x=50, y=30)
    employee_id_entry = Entry(root)
    employee_id_entry.place(x=50, y=60)
    btn_delete_employee = Button(root, text="Add employee",
                                 command=lambda: delete_employee(employee_id_entry.get(), root), bg="blue", fg="black",
                                 width=15)
    btn_delete_employee.place(x=50, y=90)
    mainloop()


def add_employee(employee_name, employee_salary,root):
    insert_query = "INSERT INTO employees(name, salary) VALUES ('" + str(employee_name) + "', " + str(employee_salary) + ");"
    cursor.execute(insert_query)
    connection.commit()
    remove_window(root)


def find_employee(employee_id, root):
    select_query = "SELECT * FROM employees WHERE id = " + employee_id + ";"
    cursor.execute(select_query)
    connection.commit()
    result = cursor.fetchone()

    name_label = Label(root, text=result['name'], fg="black")
    name_label.place(x=50, y=120)
    salary_label = Label(root, text=result['salary'], fg="black")
    salary_label.place(x=50, y=150)
    print(result)


def update_employee(employee_id, new_employee_name, new_employee_salary, root):
    update_query = "UPDATE employees SET name = '" + new_employee_name + "', salary = " + new_employee_salary + " WHERE id = " + employee_id + ";"
    cursor.execute(update_query)
    connection.commit()
    remove_window(root)


def delete_employee(employee_id, root):
    delete_query = "DELETE FROM employees WHERE id = " + employee_id + ";"
    cursor.execute(delete_query)
    connection.commit()
    remove_window(root)


def remove_window(window):
    window.destroy()


def main():
    window = Tk()
    window.title("Simple CRUD UI example")
    window.geometry('800x400')
    btn_add_employee = Button(window, text="Add employee", command=draw_add_employee_window, bg="blue", fg="black",
                              width=15)
    btn_edit_employee = Button(window, text="Edit employee", command=draw_edit_employee_window, bg="blue", fg="black",
                               width=15)
    btn_delete_employee = Button(window, text="Delete employee", command=draw_delete_employee_window, bg="blue",
                                 fg="black", width=15)
    btn_find_employee = Button(window, text="Find employee", command=draw_find_employee_window, bg="blue", fg="black",
                               width=15)
    btn_add_employee.grid(column=0, row=1)
    btn_edit_employee.grid(column=0, row=3)
    btn_delete_employee.grid(column=0, row=5)
    btn_find_employee.grid(column=0, row=7)
    mainloop()


if __name__ == "__main__":
    main()

