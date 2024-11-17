import psycopg2
db = psycopg2.connect(
    database = '6-dars',
    user = 'postgres',
    host = 'localhost',
    password = '1'
)

cursor = db.cursor()

cursor.execute('''
        drop table if exists course_assignments;            
        drop table if exists teachers;
        drop table if exists enrollments;
        drop table if exists courses;
        drop table if exists students;           
    ''')

cursor.execute('''
    create table if not exists students(
        student_id serial primary key,
        age integer check(age > 0 and age <= 100),
        email text not null unique
    );
    ''')

cursor.execute('''
               
    insert into students(age,email) values
    (21,'habib@gmail.com'),       
    (22,'bakir@gmailcom'),       
    (23,'toxir@gmail.com'),       
    (24,'sobir@gmail.com'),       
    (25,'sdfgh@gmail.com'),       
    (26,'jalil@gmail.com'),       
    (27,'halil@gmail.com'),       
    (20,'halim@gmail.com');      
      
    ''')

cursor.execute('''
    create table if not exists courses(
        course_id serial primary key,
        course_code integer not null unique,
        credits integer check(credits > 1 and credits < 5)    
    );           
    ''')

cursor.execute('''
               
    insert into courses(course_code,credits) values
    (123,3),         
    (222,4),         
    (432,2);                  

    ''')


cursor.execute('''
    create table if not exists enrollments(
        enrollment_id serial primary key,
        student_id integer references students(student_id) on delete cascade,
        course_id integer references courses(course_id) on delete set null       
    );           
    ''')

cursor.execute('''
    
    insert into enrollments(student_id,course_id) values
    (1,1),
    (2,2),
    (3,3);    
    
    ''')

cursor.execute('''
    create table if not exists teachers(
        teacher_id serial primary key,
        teacher_name varchar(50) not null,
        experience_years integer check(experience_years >= 0)
    );           
    ''')

cursor.execute('''
    
    insert into teachers(teacher_name,experience_years) values
    ('hasan',5),
    ('bakir',10),
    ('bakir',10);
              
    ''')

cursor.execute('''
    create table if not exists course_assignments(
        assignment_id serial primary key,
        teacher_id integer references teachers(teacher_id) on delete set default,
        course_id integer references courses(course_id) on delete cascade
    );
    ''')

cursor.execute('''
    
    insert into course_assignments(teacher_id,course_id) values
    (1,1),        
    (1,3),        
    (2,3),        
    (2,1),        
    (3,3),        
    (3,2),
    (3,1);               

    ''')


cursor.execute('''
               
    alter table students
    rename column age to yosh;           
    
    ''')

cursor.execute('''
               
    alter table students 
    rename to talabalar;
    
    ''')

cursor.execute('''update talabalar set yosh = 21 where student_id =1; ''')


cursor.execute('''
               
     update talabalar set yosh = 23 where student_id =3;         
    
    ''')

cursor.execute(''' delete from talabalar where student_id = 4; ''')
cursor.execute(''' delete from talabalar where student_id = 5; ''')


cursor.execute('select * from talabalar;')
print(cursor.fetchall())

cursor.execute('select * from courses;')
print(cursor.fetchall())

cursor.execute('select * from enrollments;')
print(cursor.fetchall())

cursor.execute('select * from teachers;')
print(cursor.fetchall())

cursor.execute('select * from course_assignments;')
print(cursor.fetchall()) 

db.commit()
db.close()