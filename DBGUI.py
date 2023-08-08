from DBTableCreation import Base, engine, session, School, Teacher, Class, Students
import wx


class DBManager(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)


        # Title
        self.quote = wx.StaticText(self, label="Choose Table:", pos=(20, 20))


        # Result Textbox
        self.logger1 = wx.TextCtrl(self, pos=(220, 20), size=(700, 500), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # School - Selection (b)
        self.insure = wx.CheckBox(self, label="School", pos=(20, 50))
        self.Bind(wx.EVT_CHECKBOX, self.School_EVT, self.insure)

        b = 50 # 50
        abcx = 115
        self.quote_b1 = wx.StaticText(self, label="School ID:", pos=(20, b + 20))
        self.quote_b2 = wx.StaticText(self, label="School Name:", pos=(20, b + 40))
        self.quote_b3 = wx.StaticText(self, label="School location:", pos=(20, b + 60))

        self.logger_b1 = wx.TextCtrl(self, pos=(abcx, b + 20), size=(99, 20))
        self.logger_b2 = wx.TextCtrl(self, pos=(abcx, b + 40), size=(99, 20))
        self.logger_b3 = wx.TextCtrl(self, pos=(abcx, b + 60), size=(99, 20))

        self.upload_b1 = wx.Button(self, label="Upload", pos=(90, 530))
        self.Bind(wx.EVT_BUTTON, self.Upload_School, self.upload_b1)

        self.Search_all = wx.Button(self, label="Search All", pos=(160, 530))
        self.Bind(wx.EVT_BUTTON, self.Search_All, self.Search_all)

        self.delete_b1 = wx.Button(self, label="Delete", pos=(20, 530))
        self.Bind(wx.EVT_BUTTON, self.Delete_School, self.delete_b1)

        self.joint_search_b1 = wx.Button(self, label=" Search School ", pos=(abcx, b - 5))
        self.Bind(wx.EVT_BUTTON, self.Search_School, self.joint_search_b1)

        self.Search_all.Hide(), self.upload_b1.Hide(), self.delete_b1.Hide(), self.joint_search_b1.Hide()
        self.logger_b1.Hide(), self.logger_b2.Hide(), self.logger_b3.Hide()
        self.quote_b1.Hide(), self.quote_b2.Hide(), self.quote_b3.Hide()

        # Teacher - Selection
        a = 140 # 140
        self.checkbox = wx.CheckBox(self, label="Teacher", pos=(20, a))
        self.Bind(wx.EVT_CHECKBOX, self.Teacher_EVT, self.checkbox)

        self.quote_a1 = wx.StaticText(self, label="Teacher-ID:", pos=(20, a + 20))
        self.quote_a2 = wx.StaticText(self, label="Firstname:", pos=(20, a + 40))
        self.quote_a3 = wx.StaticText(self, label="Surname:", pos=(20, a + 60))
        self.quote_a4 = wx.StaticText(self, label="Date of Birth:", pos=(20, a + 80))
        self.quote_a5 = wx.StaticText(self, label="Subject:", pos=(20, a + 100))
        self.quote_a6 = wx.StaticText(self, label="School-ID:", pos=(20, a + 120))

        self.logger_a1 = wx.TextCtrl(self, pos=(abcx, a + 20), size=(99, 20))
        self.logger_a2 = wx.TextCtrl(self, pos=(abcx, a + 40), size=(99, 20))
        self.logger_a3 = wx.TextCtrl(self, pos=(abcx, a + 60), size=(99, 20))
        self.logger_a4 = wx.TextCtrl(self, pos=(abcx, a + 80), size=(99, 20))
        self.logger_a5 = wx.TextCtrl(self, pos=(abcx, a + 100), size=(99, 20))
        self.logger_a6 = wx.TextCtrl(self, pos=(abcx, a + 120), size=(99, 20))

        self.upload_a1 = wx.Button(self, label="Upload", pos=(90, 530))
        self.Bind(wx.EVT_BUTTON, self.Upload_Teacher, self.upload_a1)

        self.Search_all = wx.Button(self, label="Search All", pos=(160, 530))
        self.Bind(wx.EVT_BUTTON, self.Search_All, self.Search_all)

        self.delete_a1 = wx.Button(self, label="Delete", pos=(20, 530))
        self.Bind(wx.EVT_BUTTON, self.Delete_Teacher, self.delete_a1)

        self.joint_search_a1 = wx.Button(self, label="Search Teacher", pos=(abcx, a - 5))
        self.Bind(wx.EVT_BUTTON, self.Search_Teacher, self.joint_search_a1)

        self.Search_all.Hide(), self.upload_a1.Hide(), self.delete_a1.Hide(), self.joint_search_a1.Hide()
        self.logger_a1.Hide(), self.logger_a2.Hide(), self.logger_a3.Hide(), self.logger_a4.Hide(), self.logger_a5.Hide(), self.logger_a6.Hide()
        self.quote_a1.Hide(), self.quote_a2.Hide(), self.quote_a3.Hide(), self.quote_a4.Hide(), self.quote_a5.Hide(), self.quote_a6.Hide()

        # Class - Selection (c)
        self.insure = wx.CheckBox(self, label="Class", pos=(20, 290))
        self.Bind(wx.EVT_CHECKBOX, self.Class_EVT, self.insure)

        c = 290    # 290
        self.quote_c1 = wx.StaticText(self, label="Class-ID:", pos=(20, c + 20))
        self.quote_c2 = wx.StaticText(self, label="Room:", pos=(20, c + 40))
        self.quote_c3 = wx.StaticText(self, label="Teacher-ID:", pos=(20, c + 60))

        self.logger_c1 = wx.TextCtrl(self, pos=(abcx, c + 20), size=(99, 20))
        self.logger_c2 = wx.TextCtrl(self, pos=(abcx, c + 40), size=(99, 20))
        self.logger_c3 = wx.TextCtrl(self, pos=(abcx, c + 60), size=(99, 20))

        self.upload_c1 = wx.Button(self, label="Upload", pos=(90, 530))
        self.Bind(wx.EVT_BUTTON, self.Upload_Class, self.upload_c1)

        self.Search_all = wx.Button(self, label="Search All", pos=(160, 530))
        self.Bind(wx.EVT_BUTTON, self.Search_All, self.Search_all)

        self.delete_c1 = wx.Button(self, label="Delete", pos=(20, 530))
        self.Bind(wx.EVT_BUTTON, self.Delete_Class, self.delete_c1)

        self.search_c1 = wx.Button(self, label="  Search Class  ", pos=(abcx, c - 5))
        self.Bind(wx.EVT_BUTTON, self.Search_Class, self.search_c1)

        self.Search_all.Hide(), self.upload_c1.Hide(), self.delete_c1.Hide(), self.search_c1.Hide()
        self.logger_c1.Hide(), self.logger_c2.Hide(), self.logger_c3.Hide()
        self.quote_c1.Hide(), self.quote_c2.Hide(), self.quote_c3.Hide()

        # Students - Selection (d)
        d = 380  # 380
        self.insure = wx.CheckBox(self, label="Students", pos=(20, d))
        self.Bind(wx.EVT_CHECKBOX, self.Student_EVT, self.insure)

        self.quote_d1 = wx.StaticText(self, label="Student-ID:", pos=(20, d + 20))
        self.quote_d2 = wx.StaticText(self, label="Firstname:", pos=(20, d + 40))
        self.quote_d3 = wx.StaticText(self, label="Surname:", pos=(20, d + 60))
        self.quote_d4 = wx.StaticText(self, label="Date of Birth:", pos=(20, d + 80))
        self.quote_d5 = wx.StaticText(self, label="Class-ID:", pos=(20, d + 100))

        self.logger_d1 = wx.TextCtrl(self, pos=(abcx, d + 20), size=(99, 20))
        self.logger_d2 = wx.TextCtrl(self, pos=(abcx, d + 40), size=(99, 20))
        self.logger_d3 = wx.TextCtrl(self, pos=(abcx, d + 60), size=(99, 20))
        self.logger_d4 = wx.TextCtrl(self, pos=(abcx, d + 80), size=(99, 20))
        self.logger_d5 = wx.TextCtrl(self, pos=(abcx, d + 100), size=(99, 20))

        self.upload_d1 = wx.Button(self, label="Upload", pos=(90, 530))
        self.Bind(wx.EVT_BUTTON, self.Upload_Student, self.upload_d1)

        self.Search_all = wx.Button(self, label="Search All", pos=(160, 530))
        self.Bind(wx.EVT_BUTTON, self.Search_All, self.Search_all)

        self.delete_d1 = wx.Button(self, label="Delete", pos=(20, 530))
        self.Bind(wx.EVT_BUTTON, self.Delete_Students, self.delete_d1)

        self.joint_search_d1 = wx.Button(self, label="Search Students", pos=(abcx, d - 5))
        self.Bind(wx.EVT_BUTTON, self.Search_Students, self.joint_search_d1)

        self.Search_all.Hide(), self.upload_d1.Hide(), self.delete_d1.Hide(), self.joint_search_d1.Hide()
        self.logger_d1.Hide(), self.logger_d2.Hide(), self.logger_d3.Hide(), self.logger_d4.Hide(), self.logger_d5.Hide()
        self.quote_d1.Hide(), self.quote_d2.Hide(), self.quote_d3.Hide(), self.quote_d4.Hide(), self.quote_d5.Hide()


    # -----------------------------------------------------------------------------------------------------------------------

    def Search_All(self, event):
        pass
    #self.logger_a2.GetValue()


    def Search_School(self, event):

        self.logger1.SetValue("")
        print("Searching School")
        search = session.query(School.school_id, School.school_name, School.location)
        for result in search:
            self.logger1.AppendText(str(result) + '\n')

    def Search_Teacher(self, event):
        self.logger1 = wx.TextCtrl(self, pos=(220, 20), size=(700, 500), style=wx.TE_MULTILINE | wx.TE_READONLY)
        print("Searching Teachers")
        #search = session.query(Teacher.teacher_id, Teacher.firstname, Teacher.surname, Teacher.date_of_birth, Teacher.subject, Teacher.school_id)\
        #.join(Teacher, Teacher.teacher_id == Class.teacher_id)

        search = session.query(Class).join(Teacher).filter(Class.class_id == 2).all()
        for result in search:
            self.logger1.AppendText(result.Teacher.surname + '\n')
            #self.logger1.AppendText(str(result) + '\n')

    def Search_Class(self, event):
        self.logger1 = wx.TextCtrl(self, pos=(220, 20), size=(700, 500), style=wx.TE_MULTILINE | wx.TE_READONLY)
        print("Searching Class")
        search = session.query(Class.class_id, Class.room, Class.teacher_id)
        for result in search:
            self.logger1.AppendText(str(result) + '\n')

    def Search_Students(self, event):
        self.logger1 = wx.TextCtrl(self, pos=(220, 20), size=(700, 500), style=wx.TE_MULTILINE | wx.TE_READONLY)
        print("Searching Student")
        search = session.query(Students.student_id, Students.firstname, Students.surname, Students.surname, Students.date_of_birth,Students.class_id)
        for result in search:
            self.logger1.AppendText(str(result) + '\n')

    # ----------------------------------------------------------------------------------------------------------------------


    def Delete_School(self, event):
        pass

    def Delete_Teacher(self):
        pass

    def Delete_Class(self):
        pass

    def Delete_Students(self):
        pass


    # ----------------------------------------------------------------------------------------------------------------------

    def Upload_School(self, event):
        pass

    def Upload_Teacher(self, event):
        pass

    def Upload_Class(self, event):
        pass

    def Upload_Student(self, event):
        pass

    # ----------------------------------------------------------------------------------------------------------------------


    def Class_EVT(self, event):
        self.logger1 = wx.TextCtrl(self, pos=(220, 20), size=(700, 500), style=wx.TE_MULTILINE | wx.TE_READONLY)
        if event.IsChecked() == True:
            self.Search_all.Show(), self.upload_c1.Show(), self.delete_c1.Show(), self.search_c1.Show()
            self.logger_c1.Show(), self.logger_c2.Show(), self.logger_c3.Show()
            self.quote_c1.Show(), self.quote_c2.Show(), self.quote_c3.Show()
        elif event.IsChecked() == False:
            self.Search_all.Hide(), self.upload_c1.Hide(), self.delete_c1.Hide(), self.search_c1.Hide()
            self.logger_c1.Hide(), self.logger_c2.Hide(), self.logger_c3.Hide()
            self.quote_c1.Hide(), self.quote_c2.Hide(), self.quote_c3.Hide()

    def Student_EVT(self, event):
        self.logger1 = wx.TextCtrl(self, pos=(220, 20), size=(700, 500), style=wx.TE_MULTILINE | wx.TE_READONLY)
        if event.IsChecked() == True:
            self.Search_all.Show(),self.upload_d1.Show(), self.delete_d1.Show(), self.joint_search_d1.Show()
            self.logger_d1.Show(), self.logger_d2.Show(), self.logger_d3.Show(), self.logger_d4.Show(), self.logger_d5.Show()
            self.quote_d1.Show(), self.quote_d2.Show(), self.quote_d3.Show(), self.quote_d4.Show(), self.quote_d5.Show()
        elif event.IsChecked() == False:
            self.Search_all.Hide(), self.upload_d1.Hide(), self.delete_d1.Hide(), self.joint_search_d1.Hide()
            self.logger_d1.Hide(), self.logger_d2.Hide(), self.logger_d3.Hide(), self.logger_d4.Hide(), self.logger_d5.Hide()
            self.quote_d1.Hide(), self.quote_d2.Hide(), self.quote_d3.Hide(), self.quote_d4.Hide(), self.quote_d5.Hide()

    def Teacher_EVT(self, event):
        self.logger1 = wx.TextCtrl(self, pos=(220, 20), size=(700, 500), style=wx.TE_MULTILINE | wx.TE_READONLY)
        if event.IsChecked() == True:
            self.Search_all.Show(),self.upload_a1.Show(), self.delete_a1.Show(), self.joint_search_a1.Show()
            self.logger_a1.Show(), self.logger_a2.Show(), self.logger_a3.Show(), self.logger_a4.Show(), self.logger_a5.Show(), self.logger_a6.Show()
            self.quote_a1.Show(), self.quote_a2.Show(), self.quote_a3.Show(), self.quote_a4.Show(), self.quote_a5.Show(), self.quote_a6.Show()
        elif event.IsChecked() == False:
            self.Search_all.Hide(), self.upload_a1.Hide(), self.delete_a1.Hide(), self.joint_search_a1.Hide()
            self.logger_a1.Hide(), self.logger_a2.Hide(), self.logger_a3.Hide(), self.logger_a4.Hide(), self.logger_a5.Hide(), self.logger_a6.Hide()
            self.quote_a1.Hide(), self.quote_a2.Hide(), self.quote_a3.Hide(), self.quote_a4.Hide(), self.quote_a5.Hide(), self.quote_a6.Hide()

    def School_EVT(self, event):
        #self.logger1 = wx.TextCtrl(self, pos=(220, 20), size=(700, 500), style=wx.TE_MULTILINE | wx.TE_READONLY)
        if event.IsChecked() == True:
            self.Search_all.Show(), self.upload_b1.Show(), self.delete_b1.Show(), self.joint_search_b1.Show()
            self.logger_b1.Show(), self.logger_b2.Show(), self.logger_b3.Show()
            self.quote_b1.Show(), self.quote_b2.Show(), self.quote_b3.Show()
        elif event.IsChecked() == False:
            self.Search_all.Hide(),self.upload_b1.Hide(), self.delete_b1.Hide(), self.joint_search_b1.Hide()
            self.logger_b1.Hide(), self.logger_b2.Hide(), self.logger_b3.Hide()
            self.quote_b1.Hide(), self.quote_b2.Hide(), self.quote_b3.Hide()

# ----------------------------------------------------------------------------------------------------------------------


def main():
    app = wx.App(False)
    frame = wx.Frame(None, title="School-DB-Manager", size=(1000, 600))
    panel = DBManager(frame)
    frame.Show()
    app.MainLoop()


    """
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()

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

main()
