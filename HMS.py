from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql

class School():
    def __init__(self,root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background="gainsboro")


        MainFrame = Frame(self.root, bd=10, width = 1350, height = 700, relief=RIDGE)
        MainFrame.grid()
        UFrame = Frame(MainFrame, bd=10, width = 1340, height = 600, relief=RIDGE)
        UFrame.grid(row = 0, column = 0)
        ULFrame = Frame(UFrame, bd=5, width = 600, height = 500, bg = 'cadet blue', relief=RIDGE)
        ULFrame.grid(row = 0, column = 0)
        URFrame = Frame(UFrame, bd=5, width = 800, height = 500, bg = 'cadet blue', relief=RIDGE)
        URFrame.grid(row = 0, column = 1, sticky = N)
        LFrame = Frame(MainFrame, bd=7, width = 1340, height = 300, bg = 'cadet blue', relief=RIDGE)
        LFrame.grid(row = 2, column = 0, sticky=W, padx =5)

        PatientListFrame = Frame(URFrame, bd=5, width = 800, height =300, relief = RIDGE)
        PatientListFrame.grid()
        PatientInfoFrame = Frame(ULFrame, bd=4, width = 400, height=300, relief=RIDGE)
        PatientInfoFrame.grid()
        Subject_Frame_Left = Frame(LFrame, bd=5, width = 600, height=300, relief=RIDGE)
        Subject_Frame_Left.grid(row=0, column=0, sticky = NW)
        Subject_Frame_Right = Frame(LFrame, bd=5, width = 700, height=300, bg='cadet blue', relief=RIDGE)
        Subject_Frame_Right.grid(row=0, column=1)
        
        SubjectFrame1 = Frame(Subject_Frame_Left, bd=5, width = 300, height = 250, padx=2, relief=RIDGE)
        SubjectFrame1.grid(row=0, column=0, sticky=W)
        SubjectFrame2 = Frame(Subject_Frame_Left, bd=5, width = 400, height = 250, padx=2, relief=RIDGE)
        SubjectFrame2.grid(row=0, column=1, sticky = NW)
        DoctorFrame = Frame(Subject_Frame_Right, bd=5, width = 400, height=250, padx=4, pady=4, relief=RIDGE)
        DoctorFrame.grid(row=0, column=0, sticky = N)
        ButtonsFrame = Frame(Subject_Frame_Right, bd=5, width = 200, height=250, padx=4, pady=4, relief=RIDGE)
        ButtonsFrame.grid(row=0, column=1)


#variables
        self.PatientID = StringVar()
        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.Age = StringVar()
        self.Gender = StringVar()
        self.BloodGroop = StringVar()
        self.Address = StringVar()
        self.Mobile = StringVar()
        self.Email = StringVar()
        self.RoomNumber = StringVar()
        self.DoctorID = StringVar()
        self.ApptID = StringVar()
        self.Diagnosis = StringVar()
        self.Date = StringVar()
        self.DoctorAge = StringVar()
        self.DoctorName = StringVar()








#Patient Details
        self.lblPatientInfo = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Patient Information", bd=7)
        self.lblPatientInfo.grid(row=0, column=1, padx=5, pady= 5)
        self.lblPatientID = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Patient ID", bd=7)
        self.lblPatientID.grid(row=1, column=0, sticky = W, padx=5, pady= 5)
        self.txtPatientID = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19, textvariable=self.PatientID)
        self.txtPatientID.grid(row=1, column=1, padx=5, pady= 5)
        self.lblFirstName = Label(PatientInfoFrame, font=('arial',12,'bold'), text="First Name", bd=7)
        self.lblFirstName.grid(row=2, column=0, sticky = W, padx=5, pady= 5)
        self.txtFirstName = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19,textvariable=self.FirstName)
        self.txtFirstName.grid(row=2, column=1, padx=5, pady= 5)
        self.lblLastName = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Last Name", bd=7)
        self.lblLastName.grid(row=3, column=0, sticky = W, padx=5, pady= 5)
        self.txtLastName = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19,textvariable=self.LastName)
        self.txtLastName.grid(row=3, column=1, padx=5, pady= 5)
        self.lblAge = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Age", bd=7)
        self.lblAge.grid(row=4, column=0, sticky = W, padx=5, pady= 5)
        self.txtAge = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19,textvariable=self.Age)
        self.txtAge.grid(row=4, column=1, padx=5, pady= 5)
        self.lblGender= Label(PatientInfoFrame, font=('arial',12,'bold'), text="Gender", bd=7)
        self.lblGender.grid(row=5, column=0, sticky = W, padx=5, pady= 5)
        self.cboGender = ttk.Combobox(PatientInfoFrame, width=19, font=('arial', 12,'bold'), state='readonly',textvariable=self.Gender)
        self.cboGender['values'] = ('','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5,column=1)
        self.lblBloodGroup = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Blood Group", bd=7)
        self.lblBloodGroup.grid(row=6, column=0, sticky = W, padx=5, pady= 5)
        self.txtBloodGroup = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19,textvariable=self.BloodGroop)
        self.txtBloodGroup.grid(row=6, column=1, padx=5, pady= 5)
       
        self.lblAddress = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=7, column=0, sticky = W, padx=5, pady= 5)
        self.txtAddress = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19,textvariable=self.Address)
        self.txtAddress.grid(row=7, column=1, padx=5, pady= 5)
        
        

       

       

        #self.lblDOB= Label(PatientInfoFrame, font=('arial',12,'bold'), text="Date of Birth", bd=7)
        #self.lblDOB.grid(row=6, column=0, sticky = W, padx=5, pady= 5)
        #self.txtDOB = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19)
        #self.txtDOB.grid(row=6, column=1, padx=5, pady= 5)
        self.lblMobile = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=8, column=0, sticky = W, padx=5, pady= 5)
        self.txtMobile = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19, textvariable=self.Mobile)
        self.txtMobile.grid(row=8, column=1, padx=5, pady= 5)
        self.lblEmail = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=9, column=0, sticky = W, padx=5, pady= 5)
        self.txtEmail = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19, textvariable= self.Email)
        self.txtEmail.grid(row=9, column=1, padx=5, pady= 5)

        self.lblRoomNumber = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Room Number", bd=7)
        self.lblRoomNumber.grid(row=10, column=0, sticky = W, padx=5, pady= 5)
        self.txtRoomNumber = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19, textvariable= self.RoomNumber)
        self.txtRoomNumber.grid(row=10, column=1, padx=5, pady= 5)


#Student Records
        scroll_x = Scrollbar(PatientListFrame, orient = HORIZONTAL)
        scroll_y = Scrollbar(PatientListFrame, orient = VERTICAL)
        columns = ("PatientID","First Name","Last Name","Age","Gender","Blood Group","Address","Mobile","Email","Room Number")
        self.student_records = ttk.Treeview(PatientListFrame, height = 13, columns=columns, xscrollcommand=scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side= BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT, fill=Y) 

        self.student_records.heading("PatientID", text = "PatientID")
        self.student_records.heading("First Name", text = "First Name")
        self.student_records.heading("Last Name", text = "Last Name")
        self.student_records.heading("Age", text = "Age")
        self.student_records.heading("Gender", text = "Gender")
        self.student_records.heading("Blood Group", text = "Blood Group")
        self.student_records.heading("Address", text = "Address")
        self.student_records.heading("Mobile", text = "Mobile")
        self.student_records.heading("Email", text = "Email")
        self.student_records.heading("Room Number", text = "Room Number")

        self.student_records['show'] = 'headings'
        
        self.student_records.column("PatientID", width = 100)
        self.student_records.column("First Name", width = 70)
        self.student_records.column("Last Name", width = 70)
        self.student_records.column("Age", width = 70)
        self.student_records.column("Gender", width = 70)
        self.student_records.column("Blood Group", width = 70)
        self.student_records.column("Address", width = 70)
        self.student_records.column("Mobile", width = 70)
        self.student_records.column("Email", width = 200)
        self.student_records.column("Room Number", width = 70)
        

        self.student_records.pack(fill=BOTH, expand = 1)
        self.student_records.bind("<ButtonRelease-1>", self.LearnersInfo)
        self.view_data()


        
#Appointment
        self.lblAppointmentInfo = Label(SubjectFrame1, font=('arial',12,'bold'), text="Appointment Information", bd=7)
        self.lblAppointmentInfo.grid(row=0, column=1, padx=5, pady= 5)
        self.lblApptPatientID = Label(SubjectFrame1, font=('arial',12,'bold'), text="Patient ID", bd=7)
        self.lblApptPatientID.grid(row=1, column=0, sticky = W, padx=5, pady= 5)
        self.txtApptPatientID = Entry(SubjectFrame1, font=('arial',12,'bold'), bd=5,width=19, textvariable=self.PatientID)
        self.txtApptPatientID.grid(row=1, column=1, padx=5, pady= 5)
        self.lblApptDoctorID = Label(SubjectFrame1, font=('arial',12,'bold'), text="Doctor ID", bd=7)
        self.lblApptDoctorID.grid(row=2, column=0, sticky = W, padx=5, pady= 5)
        self.txtApptDoctorID = Entry(SubjectFrame1, font=('arial',12,'bold'), bd=5,width=19, textvariable=self.DoctorID)
        self.txtApptDoctorID.grid(row=2, column=1, padx=5, pady= 5)
        self.lblDate = Label(SubjectFrame1, font=('arial',12,'bold'), text="Date", bd=7)
        self.lblDate.grid(row=3, column=0, sticky = W, padx=5, pady= 5)
        self.txtDate = Entry(SubjectFrame1, font=('arial',12,'bold'), bd=5,width=19, textvariable=self.Date)
        self.txtDate.grid(row=3, column=1, padx=5, pady= 5)
        self.lblApptID = Label(SubjectFrame1, font=('arial',12,'bold'), text="Appt ID", bd=7)
        self.lblApptID.grid(row=4, column=0, sticky = W, padx=5, pady= 5)
        self.txtApptID = Entry(SubjectFrame1, font=('arial',12,'bold'), bd=5,width=19, textvariable=self.ApptID)
        self.txtApptID.grid(row=4, column=1, padx=5, pady= 5)

#Medical History
        self.lblMedicalHistInfo = Label(SubjectFrame2, font=('arial',12,'bold'), text="Medical History", bd=7)
        self.lblMedicalHistInfo.grid(row=0, column=1, padx=5, pady= 5)
        self.lblHistApptID = Label(SubjectFrame2, font=('arial',12,'bold'), text="Appt ID", bd=7)
        self.lblHistApptID.grid(row=1, column=0, sticky = W, padx=5, pady= 5)
        self.txtHistApptID= Entry(SubjectFrame2, font=('arial',12,'bold'), bd=5,width=20, textvariable=self.ApptID)
        self.txtHistApptID.grid(row=1, column=1, padx=5, pady= 5)
        self.lblDiagnosis = Label(SubjectFrame2, font=('arial',12,'bold'), text="Diagnosis", bd=7)
        self.lblDiagnosis.grid(row=2, column=0, sticky = W, padx=5, pady= 5)
        self.txtDiagnosis= Entry(SubjectFrame2, font=('arial',12,'bold'), bd=5,width=20, textvariable=self.Diagnosis)
        self.txtDiagnosis.grid(row=2, column=1, padx=5, pady= 5)
        self.lblHistDate = Label(SubjectFrame2, font=('arial',12,'bold'), text="Date", bd=7)
        self.lblHistDate.grid(row=3, column=0, sticky = W, padx=5, pady= 5)
        self.txtHistDate= Entry(SubjectFrame2, font=('arial',12,'bold'), bd=5,width=20, textvariable=self.Date)
        self.txtHistDate.grid(row=3, column=1, padx=5, pady= 5)


#Doctor
        self.lblDoctorInfo = Label(DoctorFrame, font=('arial',12,'bold'), text="Doctor Info", bd=7)
        self.lblDoctorInfo.grid(row=0, column=1, padx=5, pady= 5)
        self.lblDoctorID = Label(DoctorFrame, font=('arial',12,'bold'), text="Doctor ID", bd=7)
        self.lblDoctorID.grid(row=1, column=0, sticky = W, padx=5, pady= 5)
        self.txtDoctorID = Entry(DoctorFrame, font=('arial',12,'bold'), bd=5,width=20, textvariable=self.DoctorID)
        self.txtDoctorID.grid(row=1, column=1, padx=5, pady= 5)
        self.lblDoctorName = Label(DoctorFrame, font=('arial',12,'bold'), text="Name", bd=7)
        self.lblDoctorName.grid(row=2, column=0, sticky = W, padx=5, pady= 5)
        self.txtDoctorName = Entry(DoctorFrame, font=('arial',12,'bold'), bd=5,width=20, textvariable=self.DoctorName)
        self.txtDoctorName.grid(row=2, column=1, padx=5, pady= 5)
        
        self.lblDoctorAge = Label(DoctorFrame, font=('arial',12,'bold'), text="Age", bd=7)
        self.lblDoctorAge.grid(row=3, column=0, sticky = W, padx=5, pady= 5)
        self.txtDoctorAge = Entry(DoctorFrame, font=('arial',12,'bold'), bd=5,width=20, textvariable=self.DoctorAge)
        self.txtDoctorAge.grid(row=3, column=1, padx=5, pady= 5)
        


#Buttons
        self.btnAddNew= Button(ButtonsFrame, pady=1, bd=4, font=('arial', 14, 'bold'), width = 9, text = "Add New", command = lambda:[self.add_patient(),self.add_doctor(),self.add_appointment(),self.add_medicalhistory()])
        self.btnAddNew.grid(row=0, column=0)
        self.btnAddNew= Button(ButtonsFrame, pady=1, bd=4, font=('arial', 14, 'bold'), width = 9, text = "Update", command = self.update)
        self.btnAddNew.grid(row=1, column=0)
        self.btnAddNew= Button(ButtonsFrame, pady=1, bd=4, font=('arial', 14, 'bold'), width = 9, text = "Delete", command = self.deleteDB)
        self.btnAddNew.grid(row=2, column=0)
        self.btnAddNew= Button(ButtonsFrame, pady=1, bd=4, font=('arial', 14, 'bold'), width = 9, text = "Reset", command = self.Reset)
        self.btnAddNew.grid(row=3, column=0)
        self.btnAddNew= Button(ButtonsFrame, pady=1, bd=4, font=('arial', 14, 'bold'), width = 9, text = "Exit", command = self.iExit)
        self.btnAddNew.grid(row=4, column=0)

        
#functions
    def add_patient(self):
        if self.PatientID.get() =="" or self.FirstName.get() == "" or self.LastName.get() == "":
                tkinter.messagebox.showerror("Enter correct patient details")
        else:
                sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
                cur = sqlCon.cursor()
                cur.execute("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.PatientID.get(),self.FirstName.get(),self.LastName.get(),self.Age.get(),self.Gender.get(),self.BloodGroop.get(),self.Address.get(),self.Mobile.get(),self.Email.get(),self.RoomNumber.get()))
               
                sqlCon.commit()
                sqlCon.close()
                self.view_data()
                tkinter.messagebox.showinfo("Success","Record entered successfully")


    def add_doctor(self):
        if self.DoctorID.get() =="" or self.DoctorName.get() == "" or self.DoctorAge.get() == "":
                tkinter.messagebox.showerror("Enter correct doctor details")
        else:
                sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
                cur = sqlCon.cursor()
               
                cur.execute("insert into doctor values(%s,%s,%s)",(self.DoctorID.get(),self.DoctorName.get(),self.DoctorAge.get()))
               
                
                sqlCon.commit()
                sqlCon.close()
                self.view_data()
                tkinter.messagebox.showinfo("Success","Record entered successfully")


    def add_appointment(self):
        if self.apptID.get() =="" or self.date.get() == "":
                tkinter.messagebox.showerror("Enter correct appointment details")
        else:
                sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
                cur = sqlCon.cursor()
               
                cur.execute("insert into appointment values(%s,%s,%s,%s)",(self.PatientID.get(),self.DoctorID.get(),self.Date.get(),self.ApptID.get()))
                
                sqlCon.commit()
                sqlCon.close()
                self.view_data()
                tkinter.messagebox.showinfo("Success","Record entered successfully")


    def add_medicalhistory(self):
        
                sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
                cur = sqlCon.cursor()
               
                cur.execute("insert into medicalhistory values(%s,%s,%s)",(self.ApptID.get(),self.Diagnosis.get(),self.Date.get()))
                #cur.execute("insert into doctor values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.DoctorID.get(),self.DoctorName.get(),self.DoctorAge.get()))
                sqlCon.commit()
                sqlCon.close()
                self.view_data()
                tkinter.messagebox.showinfo("Success","Record entered successfully")
                        

    def view_data(self):
        sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
        cur = sqlCon.cursor()
        cur.execute("select * from patient")
        rows = cur.fetchall()
        if len(rows)!=0:
                self.student_records.delete(*self.student_records.get_children())
                for row in rows:
                        self.student_records.insert('', END, values = row)
                sqlCon.commit()
        sqlCon.close()

        """sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
        cur = sqlCon.cursor()
        cur.execute("select * from appointment")
        rows = cur.fetchall()
        if len(rows)!=0:
                self.student_records.delete(*self.student_records.get_children())
                for row in rows:
                        self.student_records.insert('', END, values = row)
                sqlCon.commit()
        sqlCon.close()

        sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
        cur = sqlCon.cursor()
        cur.execute("select * from medicalhistory")
        rows = cur.fetchall()
        if len(rows)!=0:
                self.student_records.delete(*self.student_records.get_children())
                for row in rows:
                        self.student_records.insert('', END, values = row)
                sqlCon.commit()
        sqlCon.close()

        sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
        cur = sqlCon.cursor()
        cur.execute("select * from doctor")
        rows = cur.fetchall()
        if len(rows)!=0:
                self.student_records.delete(*self.student_records.get_children())
                for row in rows:
                        self.student_records.insert('', END, values = row)
                sqlCon.commit()
        sqlCon.close()"""

    def Reset(self):
        self.PatientID.set("")
        self.FirstName.set("")
        self.LastName.set("")
        self.Age.set("")
        self.Gender.set("")
        self.BloodGroop.set("")
        self.Address.set("")
        self.Mobile.set("")
        self.Email.set("")
        self.RoomNumber.set("")
        self.DoctorID.set("")
        self.DoctorAge.set("")
        self.DoctorName.set("")
        self.Date.set("")
        self.ApptID.set("")
        self.Diagnosis.set("")


        

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Hospital Management System", "Confirm if you want to exit")
        if iExit>0:
                root.destroy()
                return

    def LearnersInfo(self,ev):
        viewInfo = self.student_records.focus()
        learnerData = self.student_records.item(viewInfo)
        row = learnerData['values']
        self.PatientID.set(row[0])
        self.FirstName.set(row[1])
        self.LastName.set(row[2])
        self.Age.set(row[3])
        self.Gender.set(row[4])
        self.BloodGroop.set(row[5])
        self.Address.set(row[6])
        self.Mobile.set(row[7])
        self.Email.set(row[8])
        self.RoomNumber.set(row[9])

        sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
        cur = sqlCon.cursor()
        cur.execute(("select * from appointment where patientID = %s"),(self.PatientID))
        rowA = cur.fetchall()
        #if len(rowA) == 1:
        self.ApptID = rowA[1]
        self.Date = rowA[2]
        self.DoctorID = rowA[3]
        #else:
        #        tkinter.messagebox.showerror("Multiple appointments of same patient")

        sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
        cur = sqlCon.cursor()
        cur.execute(("select * from doctor where DoctorID = %s"),(self.DoctorID))
        rowB = cur.fetchall()
        if len(rowB) == 1:
                self.DoctorName = rowB[1]
                self.DoctorAge = rowB[2]
        
        sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
        cur = sqlCon.cursor()
        cur.execute(("select * from medicalhistory where apptID = %s"),(self.ApptID))
        rowC = cur.fetchall()
        if len(rowC) == 1:
                self.Diagnosis = rowC[1]
                
     

        
         

        

    def update(self):
        sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
        cur = sqlCon.cursor()
        cur.execute(("update patient set FirstName = %s, LastName = %s, Age = %s, Gender=%s, BloodGroup = %s, Address = %s, Mobile = %s, Email = %s, RoomNumber = %s where PatientID=%s"),(self.FirstName.get(),self.LastName.get(),self.Age.get(),self.Gender.get(),self.BloodGroop.get(),self.Address.get(),self.Mobile.get(),self.Email.get(),self.RoomNumber.get(),self.PatientID.get()))
        cur.execute(("update appointment set patientID = %s, date = %s, doctorID=%s where apptID = %s"),(self.PatientID.get(),self.Date.get(),self.DoctorID.get(),self.ApptID.get()))
        cur.execute(("update doctor set Name = %s, Age = %s where DoctorID = %s"),(self.DoctorName.get(),self.DoctorAge.get(),self.DoctorID.get()))
        cur.execute(("update medicalhistory set diagnosis = %s, date = %s where apptID = %s"),(self.Diagnosis.get(),self.Date.get(),self.ApptID.get()))

        sqlCon.commit()
        self.view_data()
        sqlCon.close()
        self.Reset()
        tkinter.messagebox.showinfo("Success", "Record Successfully Updated")

    def deleteDB(self):
        sqlCon = pymysql.connect(host= "localhost", user="root", password = "Malaygiri13@", database = "hospitaldb")
        cur = sqlCon.cursor()
        cur.execute(("delete from appointment where apptID = %s"), self.ApptID.get())
        cur.execute(("delete from doctor where DoctorID = %s"), self.DoctorID.get())
        cur.execute(("delete from medicalhistory where apptID = %s"), self.ApptID.get())
        cur.execute(("delete from patient where patientID = %s"), self.PatientID.get())

        sqlCon.commit()
        self.view_data()
        sqlCon.close()
        self.Reset()
        tkinter.messagebox.showinfo("Delete", "Record Successfully Deleted")

 








if __name__=='__main__':
    root =Tk()
    application = School(root)
    root.mainloop()
