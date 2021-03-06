import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])


def get_project_by_title(title):
    query = """SELECT title FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """
Title: %s"""%(title)

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "get_project":
            get_project_by_title(*args)
        elif command == "new_project":
            make_new_project(raw_input('title-> '),raw_input('description-> '), raw_input('grade-> '))

    CONN.close()

def make_new_student(first_name, last_name, github):
    # query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute("insert into Students Values (?, ?, ?)", (first_name, last_name, github) ) 
    # DB.execute(query, (first_name, last_name, github))
    
    CONN.commit()
    print "Successfully added student: %s %s"%(first_name, last_name)

# def make_new_project(title, description, max_grade):
#     query = """SELECT title, description, max_grade FROM Projects Where title = ?"""
#     DB.execute("query, (title, description, max_grade)")

#     CONN.commit()
#     print "Successfully added project: %s %s"%(title, description)

def make_new_project(title, description, max_grade):   
    DB.execute("insert into Projects Values (?, ?, ?)", (title, description, max_grade))

    CONN.commit()
    print "Successfully added project: %s %s"%(title, description)

if __name__ == "__main__":
    main()
