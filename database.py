from sqlalchemy import create_engine
my_conn = create_engine("sqlite:///my_db.db")

print("Connected to database successfully")
my_conn.execute('''
        CREATE TABLE IF NOT EXISTS order(id integer primary key AUTOINCREMENT,
                      first_name text,
                      last_name text,
                      phone text,
                      email text,
                      paid integer,
                      sent integer,
                      comments text                      
                      );''')
r_set=my_conn.execute('''SELECT * from student''');
for row in r_set:
    print(row)



r_set=my_conn.execute('''INSERT INTO `student` 
  ( `name`, `class`, `mark`, `sex`) VALUES
  ( 'John Deo', 'Four', 75, 'female'),
  ( 'Max Ruin', 'Three', 85, 'male'),
  ( 'Arnold', 'Three', 55, 'male'),
  ( 'Krish Star', 'Four', 60, 'female');''')


r_set=my_conn.execute('''select name from sqlite_master 
		where type = 'table' ''')
for row in r_set:
    print(row)
r_set=my_conn.execute('''SELECT * from student''');
for row in r_set:
    print(row)
# except SQLAlchemyError as e:
#   #print(e)
#   error = str(e.__dict__['orig'])
#   print(error)
# else:
#   print("Student Table created successfully..")
