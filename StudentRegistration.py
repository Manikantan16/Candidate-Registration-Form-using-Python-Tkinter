#pip install PyMySQL
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
import re


root = Tk()
root.title('Student Registration System')
root.geometry('1550x800+0+0')

#Set the Treeview Style
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", font=("Calibri", 14, "bold"),foreground="white",background='darkgreen')
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 12))
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 



def mysqlconnection():
    conn = mysql.connector.connect(host='xxxxxx',user='root',password='xxxxxxx',database ='xxxxxx')
    return conn


def getCourseDetails():
    try:
        conn = mysqlconnection()
        cursor = conn.cursor()
        cursor.execute('select CourseId,CourseName from course order by CourseName')
        CourseDetailsList = cursor.fetchall()
        return [(row[1],row[0]) for row in CourseDetailsList]
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error",f"failed to load Students:{err}")
    finally:
        conn.close()

def on_select(event):
    selected_course = cmbCourse.get()
    for name, course_id in Course_Data:
        if name == selected_course:
            print(f"Selected Course: {name}, Course ID: {course_id}")
            break
        
def add_StudentDetails():
    txtStudentId.config(state="normal")
    _studentId = txtStudentId.get()
    txtStudentId.config(state="disabled")
    if len(_studentId) > 0:
        messagebox.showerror("Input Error", "You have selected the wrong option.Please select Update to modify the student details.")
        return
   
    if not txtStudentName.get() or not txtEmail.get() or not txtMobile.get() or not txtFees.get() or not cmbGender.get() or not cmbCourse.get():
        messagebox.showerror("Error", "Input fields in Student Info cannot be blank.")
        return
   
    if not validate_email(txtEmail.get()):
        messagebox.showerror("Invalid Input", "Invalid Email Format..")
        return                    
    
    if not validate_isdecimal(txtFees.get()):
        messagebox.showerror("Invalid Input", "Enter a decimal value.")
        return 
    try:
        index = cmbCourse.current()
        row = Course_Data[index]
   
        conn = mysqlconnection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO student_registration(Name,Gender,Email,MobileNo,Fee,CourseId,IsActive) VALUES (%s,%s,%s,%s,%s,%s,%s)",(txtStudentName.get(),
                                                                                                                   cmbGender.get(),
                                                                                                                   txtEmail.get(),
                                                                                                                   txtMobile.get(),
                                                                                                                   float(txtFees.get()),
                                                                                                                   row[1],
                                                                                                                   'Y'))
        conn.commit()
        messagebox.showinfo("Success", "Student Details added successfully!")
        Reset_studentDetails();                
        LoadStudentRegDetailsList()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to insert student: {err}")
    finally:
        conn.close() 

def update_StudentDetails():
    selected_StudentItem = Student_Table.selection()
    if not selected_StudentItem:
        messagebox.showerror("Selection Error", "Please select a student to update.")
        return

    txtStudentId.config(state="normal")
    _studentId = txtStudentId.get()
    txtStudentId.config(state="disabled")
      

    if not txtStudentName.get() or not txtEmail.get() or not txtMobile.get() or not txtFees.get() or not cmbGender.get() or not cmbCourse.get():
        messagebox.showerror("Error", "Input fields in Student Info cannot be blank.")
        return
   
    if not validate_email(txtEmail.get()):
        messagebox.showerror("Invalid Input", "Invalid Email Format..")
        return                    
    
   

    try:
        index = cmbCourse.current()
        row = Course_Data[index]
        
        conn = mysqlconnection()
        cursor = conn.cursor()

        sql = "UPDATE Student_Registration SET Name=%s,Email=%s,MobileNo=%s,Fee=%s,Gender=%s,CourseId=%s WHERE Id=%s"
        values = (txtStudentName.get(),txtEmail.get(),txtMobile.get(),txtFees.get(),cmbGender.get(),row[1],_studentId)
        
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Student record updated successfully!")
       
        Reset_studentDetails()
        LoadStudentRegDetailsList()
               
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to update student: {err}")
    finally:
        conn.close()
        
def delete_student():
    if messagebox.askokcancel('Delete', 'Are you sure you want to delete this record?'):
        # Get the student ID from the entry field
        txtStudentId.config(state="normal")
        _studentId = txtStudentId.get()
        txtStudentId.config(state="disabled")

        if not _studentId:
            messagebox.showerror("Selection Error", "Please select a student to delete.")
            return
        
        try:
            conn = mysqlconnection()
            cursor = conn.cursor()

            sql = "Update  student_registration set IsActive = 'N' where id =%s"
            cursor.execute(sql, (_studentId,))
            conn.commit()

            messagebox.showinfo("Success", "Student record deleted successfully!")
            Reset_studentDetails();
            LoadStudentRegDetailsList()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to delete student: {err}")
        finally:
            conn.close()
    pass

def LoadStudentRegDetailsList():
    # Remove all previous entries in the Treeview
    for row in Student_Table.get_children():
        Student_Table.delete(row)

    try:
        conn = mysqlconnection()
        cursor = conn.cursor()

        cursor.execute("SELECT SR.Id,Name,Gender,Email,MobileNo,C.CourseName,Fee FROM student_registration SR left join course C on SR.CourseId = C.CourseId where IsActive = 'Y'") 
        StudDetList = cursor.fetchall()

        for student in StudDetList:
            Student_Table.insert("", "end", values=student)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to load students: {err}")
    finally:
        conn.close()

def Search_byParams():
    
    try:
        conn = mysqlconnection()
        cursor = conn.cursor()
        #strmsg = "SELECT Id,Name,Gender,Email,MobileNo,Course,Fee FROM student_registration where IsActive = 'Y' and " + str(CmbSearch.get()) + " like '" + str(txtsearch.get())+"%'"
        # messagebox.showinfo("",strmsg)
        # return
        cursor.execute("SELECT SR.Id,Name,Gender,Email,MobileNo,C.CourseName,Fee FROM student_registration SR left join course C on SR.CourseId = C.CourseId  where IsActive = 'Y' and " + str(CmbSearch.get()) + " like '" + str(txtsearch.get())+"%'")
        searchlist = cursor.fetchall()
        if len(searchlist) > 0:
         # Remove all previous entries in the Treeview
            for row in Student_Table.get_children():
             Student_Table.delete(row)
            for row in searchlist:
                Student_Table.insert("", "end", values=row)
        pass
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to load students: {err}")
    finally:
        conn.close()


def On_Student_TrVw_Select(event):
    selected_item = Student_Table.selection()
    if selected_item:
        student = Student_Table.item(selected_item)
        StudentId,StudentName,Gender,Email,MobileNo,Course,Fee = student['values']
        
        # Populate the entry fields with the selected student's data
        txtStudentId.config(state="normal")  # Make the ID entry editable to update
        txtStudentId.delete(0, tk.END)
        txtStudentId.insert(0, StudentId)  # Set the student ID for deletion or update
        txtStudentId.config(state="disabled")

        txtStudentName.delete(0, tk.END)
        txtStudentName.insert(0, StudentName)   
        
        txtMobile.delete(0, tk.END)
        txtMobile.insert(0, MobileNo) 
                
        txtEmail.delete(0, tk.END)
        txtEmail.insert(0, Email)   
        
        txtFees.delete(0, tk.END)
        txtFees.insert(0, Fee)   
        
        cmbGender.delete(0,tk.END)
        cmbGender.insert(0,Gender)
        
        cmbCourse.delete(0,tk.END)
        cmbCourse.insert(0,Course)

def Reset_studentDetails():
     txtStudentId.config(state="normal")  # Make the ID entry editable to update
     txtStudentId.delete(0, tk.END)
     txtStudentId.config(state="disabled")
    
     txtStudentName.delete(0, tk.END)
     txtEmail.delete(0, tk.END)
     txtMobile.delete(0, tk.END)
     txtFees.delete(0, tk.END)
     cmbGender.set('')
     cmbCourse.set('')


#Related to Courses     
def On_Course_TrVw_Select(event):
    selected_item = course_table.selection()
    if selected_item:
        course = course_table.item(selected_item)
        courseid, coursename = course['values']
        
        # Populate the entry fields with the selected student's data
        txtCourseId.config(state="normal")  # Make the ID entry editable to update
        txtCourseId.delete(0, tk.END)
        txtCourseId.insert(0, courseid)  # Set the student ID for deletion or update
        txtCourseId.config(state="disabled")

        txtCourseName.delete(0, tk.END)
        txtCourseName.insert(0, coursename)

def LoadCourseDetailsList():
    # Remove all previous entries in the Treeview
    for row in course_table.get_children():
        course_table.delete(row)

    try:
        conn = mysqlconnection()
        cursor = conn.cursor()

        cursor.execute("SELECT CourseId,CourseName FROM Course")
        CourseList = cursor.fetchall()

        for course in CourseList:
            course_table.insert("", "end", values=course)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to load Course: {err}")
    finally:
        conn.close()
 
def add_CourseDetails():
    _coursename = txtCourseName.get()
    txtCourseId.config(state="normal")
    _courseId = txtCourseId.get()
    txtCourseId.config(state="disabled")
    if len(_courseId) > 0:
        messagebox.showerror("Input Error", "You have selected the wrong option.Please select Update to modify the record.")
        return
   
    if not _coursename:
        messagebox.showerror("Input Error", "Course Name cannot be blank.")
        return
    
    try:
        conn = mysqlconnection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO course(coursename) VALUES (%s)",(_coursename,))
        conn.commit()
        
        messagebox.showinfo("Success", "Course Details added successfully!")
        txtCourseName.delete(0, tk.END)
                       
        LoadCourseDetailsList()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to insert student: {err}")
    finally:
        conn.close() 
            
# Function to update Course record
def update_Course():
    selected_CourseItem = course_table.selection()
    if not selected_CourseItem:
        messagebox.showerror("Selection Error", "Please select a Course to update.")
        return

    txtCourseId.config(state="normal")
    _courseId = txtCourseId.get()
    txtCourseId.config(state="disabled")
    _coursename = txtCourseName.get()   

    if not _coursename:
        messagebox.showerror("Input Error", "All fields must be filled.")
        return

    try:
        conn = mysqlconnection()
        cursor = conn.cursor()

        sql = "UPDATE Course SET CourseName=%s WHERE CourseId=%s"
        values = (_coursename, _courseId)
        
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Student record updated successfully!")
       
        Reset_CourseDetails()
        LoadCourseDetailsList()
        LoadStudentRegDetailsList()
        
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to update student: {err}")
    finally:
        conn.close()
    
def Reset_CourseDetails():
     txtCourseId.config(state="normal")  # Make the ID entry editable to update
     txtCourseId.delete(0, tk.END)
     txtCourseId.config(state="disabled")
     txtCourseName.delete(0, tk.END)
     
     
def Exit():
    if messagebox.askokcancel('Close', 'Are you sure you want to close the page?'):
        root.quit()
    pass

def Validate_Numeric(new_value):
    if new_value.isdigit() or new_value == "":
        return True
    return False

def validate_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(email_pattern, email):
        return True
    return False

def validate_isdecimal(new_value):
    if new_value.isdecimal():
        return True
    return False



  
lbltitle = Label(root,text='STUDENT REGISTRATION SYSTEM',relief=RIDGE,background='darkgreen',foreground='white',font=('Arial',25,"bold"),padx=2,pady=4)
lbltitle.pack(side=TOP,fill=X)
            
#===============DataFrame============================                 
DataFrame = Frame(root,bd=10,relief=RIDGE,padx=20)
DataFrame.place(x=0,y=60,width=1530,height=340)


DataFrameLeft = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text='Student Information',fg='darkgreen',
                           font=('times new roman',14,"bold"))
DataFrameLeft.place(x=0,y=10,width=790,height=300)

lblStudentId = Label(DataFrameLeft,text='Student Id:',font=('arial',13,"bold"),padx=0,pady=6)
lblStudentId.grid(row=3,column=0,sticky=W)

txtStudentId = Entry(DataFrameLeft,font=('arial',11),bg='white',bd=2,relief=RIDGE,width=10,state=DISABLED)
txtStudentId.grid(row=3,column=1,sticky=W)

lblStudentName= Label(DataFrameLeft,text='Student Name:',font=('arial',13,"bold"),padx=2,pady=6)
lblStudentName.grid(row=4,column=0,sticky=W)

txtStudentName = Entry(DataFrameLeft,font=('arial',11),bg='white',bd=2,relief=RIDGE,width=29)
txtStudentName.grid(row=4,column=1)

gender_options = ['Male','Female','Others']
lblGender= Label(DataFrameLeft,text='Gender:',font=('arial',13,"bold"),padx=2,pady=6)
lblGender.grid(row=5,column=0,sticky=W)

cmbGender = ttk.Combobox(DataFrameLeft,font=('arial',11),width=10,values=gender_options)
cmbGender.grid(row=5,column=1,sticky=W)

lblEmail= Label(DataFrameLeft,text='Email Id:',font=('arial',13,"bold"),padx=2,pady=6)
lblEmail.grid(row=6,column=0,sticky=W)

txtEmail = Entry(DataFrameLeft,font=('arial',11),bg='white',bd=2,relief=RIDGE,width=29)
txtEmail.grid(row=6,column=1)

lblMobile= Label(DataFrameLeft,text='Mobile:',font=('arial',13,"bold"),padx=2,pady=6)
lblMobile.grid(row=7,column=0,sticky=W)

txtMobile = Entry(DataFrameLeft,font=('arial',11),bg='white',bd=2,relief=RIDGE,width=29,validate='key',validatecommand=(root.register(Validate_Numeric), '%P'))
txtMobile.grid(row=7,column=1)

lblCourse= Label(DataFrameLeft,text='Course:',font=('arial',13,"bold"),padx=2,pady=6)
lblCourse.grid(row=8,column=0,sticky=W)

Course_Data = getCourseDetails()

cmbCourse = ttk.Combobox(DataFrameLeft,font=('arial',11),width=27, values=[row[0] for row in Course_Data])
cmbCourse.grid(row=8,column=1,sticky=W)
cmbCourse.current(0)
cmbCourse.bind("<<ComboboxSelected>>", on_select)
#cmbCourse.current(0)


lblFees= Label(DataFrameLeft,text='Fees:',font=('arial',13,"bold"),padx=2,pady=6)
lblFees.grid(row=9,column=0,sticky=W)

txtFees = Entry(DataFrameLeft,font=('arial',11),bg='white',bd=2,relief=RIDGE,width=29)
txtFees.grid(row=9,column=1)

img1 = Image.open(r"D:\Python_Code\VSCode_Python\PythonWithMySql\Images\SIS_2.jpg")
img1 = img1.resize((335,270))
photoimg1 = ImageTk.PhotoImage(img1)
btnImg1 = Button(root,image=photoimg1,borderwidth=0)
btnImg1.place(x=470,y=97)


DataFrameRight = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text='Course Information',fg='darkgreen',
                           font=('times new roman',14,"bold"))
DataFrameRight.place(x=830,y=10,width=640,height=300)

    
img2 = Image.open(r"D:\Python_Code\VSCode_Python\PythonWithMySql\Images\Our_Courses.jpg")
img2 = img2.resize((225,75))
photoimg2 = ImageTk.PhotoImage(img2)
btnImg2 = Button(root,image=photoimg2,borderwidth=0)
btnImg2.place(x=870,y=100)

img3 = Image.open(r"D:\Python_Code\VSCode_Python\PythonWithMySql\Images\Courses_Offered.jpg")
img3 = img3.resize((220,79))
photoimg3 = ImageTk.PhotoImage(img3)
btnImg3 = Button(root,image=photoimg3,borderwidth=0)
btnImg3.place(x=1082,y=97)

img4 = Image.open(r"D:\Python_Code\VSCode_Python\PythonWithMySql\Images\IT_Courses.jpg")
img4 = img4.resize((188,144))
photoimg4 = ImageTk.PhotoImage(img4)
btnImg4 = Button(root,image=photoimg4,borderwidth=0)
btnImg4.place(x=1300,y=97)

# img5 = Image.open(r"D:\Python_Code\VSCode_Python\PythonWithMySql\Images\Courses.png")
# img5 = img5.resize((183,135))
# photoimg5 = ImageTk.PhotoImage(img5)
# btnImg5 = Button(root,image=photoimg5,borderwidth=0)
# btnImg5.place(x=1300,y=255)

lblCourseId = Label(DataFrameRight,text='Course Id:',font=('arial',13,"bold"))
lblCourseId.place(x=0,y=80)

txtCourseId = Entry(DataFrameRight,font=('arial',11),bg='white',bd=2,relief=RIDGE,width=8,state=DISABLED)
txtCourseId.place(x=125,y=80)

lblCourseName = Label(DataFrameRight,text='Course Name:',font=('arial',13,"bold"))
lblCourseName.place(x=0,y=110)

txtCourseName = Entry(DataFrameRight,font=('arial',11),bg='white',bd=2,relief=RIDGE,width=30)
txtCourseName.place(x=125,y=110)

#=============================Side Frame======================================================
side_frame = Frame(DataFrameRight,bd=4,relief=RIDGE,bg='white')
side_frame.place(x=0,y=140,width=420,height=120)

sc_x = ttk.Scrollbar(side_frame,orient=HORIZONTAL)
sc_x.pack(side=BOTTOM,fill=X)
sc_y = ttk.Scrollbar(side_frame,orient=VERTICAL)
sc_y.pack(side=RIGHT,fill=Y)

course_table = ttk.Treeview(side_frame,columns=("Course Id","Course Name"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
sc_x.config(command=course_table.xview)
sc_y.config(command=course_table.yview)

course_table.heading("Course Id",text="Course Id")
course_table.heading("Course Name",text="Course Name")
course_table["show"] = "headings"
course_table.pack(fill=BOTH,expand=1)
course_table.column("Course Id",width=4,anchor=W)
course_table.column("Course Name",width=130,anchor=W)



#===========RHS Button Frame===================================
side_right_frame = Frame(DataFrameRight,bd=0,relief=RIDGE)
side_right_frame.place(x=422,y=140,width=135,height=120)

btnCourseAdd = Button(side_right_frame,text="Add",font=('arial',12,"bold"),bg='purple',fg='white',width=12,pady=6,bd=0,command=add_CourseDetails)
btnCourseAdd.grid(row=0,column=0)

btnCourseUpdate = Button(side_right_frame,text="Update",font=('arial',12,"bold"),bg='darkgreen',fg='white',width=12,pady=6,bd=0,command=update_Course)
btnCourseUpdate.grid(row=1,column=0)

btnCourseReset = Button(side_right_frame,text="Reset",font=('arial',12,"bold"),bg='orange',fg='white',width=12,pady=6,bd=0,command=Reset_CourseDetails)
btnCourseReset.grid(row=2,column=0)


#=================Bottom Button Frame===========================================================================
ButtonFrame = Frame(root,bd=10,relief=RIDGE,padx=5)
ButtonFrame.place(x=0,y=410,width=1530,height=55)

#=================Main Button============================================================================
btnAdd = Button(ButtonFrame,text='Add Student',width=14,font=('arial',12,"bold"),bg='darkgreen',fg='white',command=add_StudentDetails)
btnAdd.grid(row=0,column=0)

btnUpdate = Button(ButtonFrame,text='UPDATE',font=('arial',13,"bold"),bg='darkgreen',fg='white',width=14,command=update_StudentDetails)
btnUpdate.grid(row=0,column=1)

btnDelete = Button(ButtonFrame,text='DELETE',font=('arial',13,"bold"),bg='red',fg='white',width=14,command=delete_student)
btnDelete.grid(row=0,column=2)

btnReset = Button(ButtonFrame,text='RESET',font=('arial',13,"bold"),bg='darkgreen',fg='white',width=14,command=Reset_studentDetails)
btnReset.grid(row=0,column=3)

btnExit = Button(ButtonFrame,text='EXIT',font=('arial',13,"bold"),bg='darkgreen',fg='white',width=14,command=Exit)
btnExit.grid(row=0,column=4)

lblSearchBy = Label(ButtonFrame,text="Search By",width=12,font=('arial',17,"bold"),padx=2,bg='red',fg='white')
lblSearchBy.grid(row=0,column=5,sticky=W)

CmbSearch = ttk.Combobox(ButtonFrame,width=10,font=('arial',17,"bold"),state='readonly')
CmbSearch['values']=("MobileNo","Name")
CmbSearch.grid(row=0,column=6)
CmbSearch.current(0)

txtsearch = Entry(ButtonFrame,bd=3,relief=RIDGE,width=15,font=('arial',17,"bold"))
txtsearch.grid(row=0,column=7)

btnSearch =Button(ButtonFrame,text='SEARCH',width=10,font=('arial',13,"bold"),bg='darkgreen',fg='white',command=Search_byParams)
btnSearch.grid(row=0,column=8)

btnShowAll =Button(ButtonFrame,text='SHOW ALL',width=10,font=('arial',13,"bold"),bg='darkgreen',fg='white',command=LoadStudentRegDetailsList)
btnShowAll.grid(row=0,column=9)


#==========================MAIN TABLE================================================================================
Details_Frame = Frame(root,bd=10,relief=RIDGE)
Details_Frame.place(x=0,y=470,width=1530,height=310)

Student_Table = ttk.Treeview(Details_Frame,columns=("StudentId","StudentName","Gender","Email","MobileNo","Course Name","Fees"))

Student_Table.heading("StudentId",text="StudentId")
Student_Table.heading("StudentName",text="StudentName")
Student_Table.heading("Gender",text="Gender")
Student_Table.heading("Email",text="Email")
Student_Table.heading("MobileNo",text="MobileNo")
Student_Table.heading("Course Name",text="Course Name")
Student_Table.heading("Fees",text="Fees")
Student_Table["show"] = "headings"
Student_Table.pack(fill=BOTH,expand=1)
Student_Table.column("StudentId",width=10)
Student_Table.column("StudentName",width=120)
Student_Table.column("Gender",width=20)
Student_Table.column("Email",width=70)
Student_Table.column("MobileNo",width=70)
Student_Table.column("Course Name",width=120)
Student_Table.column("Fees",width=70)

Reset_studentDetails()
LoadStudentRegDetailsList()
LoadCourseDetailsList()

Student_Table.bind("<ButtonRelease-1>", On_Student_TrVw_Select)
course_table.bind("<ButtonRelease-1>", On_Course_TrVw_Select)
root.mainloop()