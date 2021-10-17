import sqlite3


conn = sqlite3.connect("data1.db",check_same_thread = False)
c = conn.cursor()


# Database
# Table
# Field/Colums
# Datatyoe

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT,taks_due_date DATE,task_description TEXT)')

def add_data(task,task_status,taks_due_date,task_description):
	c.execute('INSERT INTO taskstable(task,task_status,taks_due_date,task_description) VALUES (?,?,?,?)',(task,task_status,taks_due_date,task_description))
	conn.commit()

def view_all_data():
	c.execute('SELECT * FROM taskstable;')
	data = c.fetchall()
	return data

def view_unique_tasks():
    c.execute('SELECT task FROM taskstable;')
    data = c.fetchall()
    return data

def get_task(task):
	c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
	# c.execute('SELECT * FROM taskstable WHERE task=?'.(task))
	data = c.fetchall()
	return data


def edit_task_data(new_task,new_task_status,new_task_description,new_task_due_date,task,task_status,taks_due_date,task_description):
	c.execute("UPDATE taskstable SET task=?,task_status=?,taks_due_date=?,task_description=? WHERE task = ? and task_status=? and taks_due_date=? and task_description=? ",(new_task,new_task_status,new_task_description,new_task_due_date,task,task_status,taks_due_date,task_description))
	conn.commit()
	data = c.fetchall()
	return data

def delete_task(task):
    c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))

