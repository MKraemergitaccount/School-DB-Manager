from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Relationship

engine = create_engine('postgresql://postgres:Emmi123@gemini.konzept-is.de:5432/MaikKraemer')
Base = declarative_base()


class School(Base):
    __tablename__= "school_table"

    school_id      = Column(Integer, primary_key=True)
    school_name    = Column(String)
    location       = Column(String)


class Teacher(Base):
    __tablename__= "teacher_table"

    teacher_id      = Column(Integer, primary_key=True)
    firstname       = Column(String)
    surname         = Column(String)
    date_of_birth   = Column(String)
    subject         = Column(String)
    school_id       = Column(Integer, ForeignKey("school_table.school_id", ondelete="CASCADE"))


class Class(Base):
    __tablename__ = "class_table"

    class_id         = Column(Integer, primary_key=True)
    room             = Column(String)
    teacher_id       = Column(Integer, ForeignKey("teacher_table.teacher_id", ondelete="CASCADE"))
    Teacher          = Relationship("Teacher")

class Students(Base):
    __tablename__ = "students_table"

    student_id       = Column(Integer, primary_key=True)
    firstname        = Column(String)
    surname          = Column(String)
    date_of_birth    = Column(String)
    class_id         = Column(Integer, ForeignKey("class_table.class_id", ondelete="CASCADE"))



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

School_list = [
    {"school_id":1, "school_name":"Die_Schule", "location":"Meersburg"}
]


Teacher_list = [
    {"teacher_id":1, "firstname":"Robert", "surname":"Son"    , "date_of_birth":"01.01.2000", "subject":"Mathe",   "school_id":1},
    {"teacher_id":2, "firstname":"Bob"   , "surname":"Dil"    , "date_of_birth":"02.04.1950", "subject":"English", "school_id":1},
    {"teacher_id":3, "firstname":"Rudolf", "surname":"Meier"  , "date_of_birth":"05.12.1960", "subject":"Kunst",   "school_id":1},
    {"teacher_id":4, "firstname":"John"  , "surname":"Wick"   , "date_of_birth":"12.04.1950", "subject":"Sport",   "school_id":1},
]

Class_list = [
    {"class_id":1,  "room":"a", "teacher_id":1},
    {"class_id":2,  "room":"b", "teacher_id":2},
    {"class_id":3,  "room":"c", "teacher_id":3},
    {"class_id":4,  "room":"d", "teacher_id":4}
]

Student_list = [
    {"student_id": 1,    "firstname": "Mark",        "surname": "Marksman",   "date_of_birth": "04.09.1999",    "class_id": 1},
    {"student_id": 2,    "firstname": "Mick",        "surname": "Dock",       "date_of_birth": "19,06,1998",    "class_id": 2},
    {"student_id": 3,    "firstname": "Martin",      "surname": "Marksman",   "date_of_birth": "04.08.1999",    "class_id": 3},
    {"student_id": 4,    "firstname": "Mathis",      "surname": "man",        "date_of_birth": "01.09.1999",    "class_id": 4},
    {"student_id": 5,    "firstname": "Matias",      "surname": "Cook",       "date_of_birth": "04.07.2000",    "class_id": 1},
    {"student_id": 6,    "firstname": "Kevin",       "surname": "Marksman",   "date_of_birth": "04.09.1999",    "class_id": 2},
    {"student_id": 7,    "firstname": "Kai",         "surname": "Dock",       "date_of_birth": "19,06,1998",    "class_id": 3},
    {"student_id": 8,    "firstname": "Konrad",      "surname": "Marksman",   "date_of_birth": "04.08.1999",    "class_id": 4},
    {"student_id": 9,    "firstname": "Karl",        "surname": "Man",        "date_of_birth": "01.09.1999",    "class_id": 1},
    {"student_id": 10,   "firstname": "Kim",         "surname": "Yo",         "date_of_birth": "04.07.2000",    "class_id": 2},
    {"student_id": 11,   "firstname": "Mark",        "surname": "Marksman",   "date_of_birth": "04.09.1999",    "class_id": 3},
    {"student_id": 12,   "firstname": "Kai",         "surname": "Dock",       "date_of_birth": "19,06,1998",    "class_id": 4},
    {"student_id": 13,   "firstname": "Fabian",      "surname": "Marksman",   "date_of_birth": "04.08.1999",    "class_id": 1},
    {"student_id": 14,   "firstname": "Mark",        "surname": "man",        "date_of_birth": "01.09.1999",    "class_id": 2},
    {"student_id": 15,   "firstname": "Tim",         "surname": "Cook",       "date_of_birth": "04.07.2000",    "class_id": 3},
    {"student_id": 16,   "firstname": "Mark",        "surname": "Marksman",   "date_of_birth": "04.09.1999",    "class_id": 4},
    {"student_id": 17,   "firstname": "Kai",         "surname": "Dock",       "date_of_birth": "19,06,1998",    "class_id": 1},
    {"student_id": 18,   "firstname": "Fabian",      "surname": "Marksman",   "date_of_birth": "04.08.1999",    "class_id": 2},
    {"student_id": 19,   "firstname": "Mark",        "surname": "man",        "date_of_birth": "01.09.1999",    "class_id": 3},
    {"student_id": 20,   "firstname": "Tim",         "surname": "Cook",       "date_of_birth": "04.07.2000",    "class_id": 4}
]


for School_Element in School_list:
    school_object = School(school_id=School_Element["school_id"],
                           school_name=School_Element["school_name"],
                           location=School_Element["location"])
    session.add(school_object)
session.commit()



for Teacher_Element in Teacher_list:
    teacher_object = Teacher(teacher_id=Teacher_Element["teacher_id"],
                             firstname=Teacher_Element["firstname"],
                             surname=Teacher_Element["surname"],
                             date_of_birth=Teacher_Element["date_of_birth"],
                             subject=Teacher_Element["subject"],
                             school_id=Teacher_Element["school_id"])
    session.add(teacher_object)
session.commit()



for Class_Element in Class_list:
    class_object = Class(class_id=Class_Element["class_id"],
                         room=Class_Element["room"],
                         teacher_id=Class_Element["teacher_id"])
    session.add(class_object)
session.commit()



for Student_Element in Student_list:
    student_object = Students(student_id=Student_Element["student_id"],
                              firstname=Student_Element["firstname"],
                              surname=Student_Element["surname"],
                              date_of_birth=Student_Element["date_of_birth"],
                              class_id=Student_Element["class_id"])
    session.add(student_object)
session.commit()


"""
search = session\
    .query(Teacher.teacher_id, Teacher.firstname, Teacher.surname, Teacher.surname, Teacher.date_of_birth, Teacher.subject, Teacher.school_id)\
    .join(Teacher, Teacher.teacher_id == Class.teacher_id)
    

for result in search:
    print(result)
"""



