# Tkinter Overview     ![Tkinter](https://github.com/user-attachments/assets/486b5a90-d5f3-472a-9a03-dbf80023003b)

Tkinter is Python's standard interface to the Tk GUI toolkit. It provides a simple way to create graphical user interfaces (GUIs) for your Python applications. 
Tkinter is bundled with Python, so there's no need to install it separately, making it a great choice for building simple desktop apps.

### Key Features:
##### . Simple and Lightweight: Tkinter provides a straightforward API for building basic GUI applications.
##### . Cross-Platform Compatibility: Tkinter applications run on Windows, macOS, and Linux.
##### . Widgets: Tkinter offers a wide range of widgets like buttons, labels, entry fields, text boxes, and more.
##### . Event Handling: Tkinter supports handling events like button clicks, key presses, and window resizing.

### Installation:
##### Since Tkinter comes pre-installed with Python, you don’t need to install it manually. However, if you're using a minimal Python installation, you can install it via:
![image](https://github.com/user-attachments/assets/72cd2464-f9ea-47bb-8db2-d8e3f07a7a08)

### How to Use
##### . Import Tkinter using import tkinter as tk.
##### . Create the main window with tk.Tk().
##### . Add widgets like buttons, labels, and text fields to the window.
##### . Use root.mainloop() to start the GUI event loop.

### Examples:
#### Display Hello World using Tkinter
![image](https://github.com/user-attachments/assets/be9e6585-6035-4f25-841b-f0a66a9e27a2)


### Documentation
##### For more details on how to use Tkinter, check the official Tkinter documentation 

##### https://docs.python.org/3/library/tkinter.html

##### This should give users a clear idea of what Tkinter is and how to get started with it. You can adjust the content depending on the specific context of your project, such as adding details on more advanced features if necessary.

# Candidate Enrollment  

Creating a candidate registration form using Python and Tkinter is a great project to help you learn about GUI development and handling user input. Tkinter is the standard GUI library in Python and provides a simple way to create windows, labels, buttons, text fields, and other interactive components.

###  Here's an overview of the steps involved in creating a candidate registration form using Python and Tkinter:
### 1. Setting up the environment
  This project is developed in Vscode (python + tkinter GUI) and mySql as backend.

### 2. Designing the Registration Form Layout
  The registration form typically includes:

  Labels: to describe the fields (like "Name", "Age", "Gender", etc.).
  
  Entry widgets: to allow the user to input information.
  
  Combobox/Dropdown: for selecting a gender and course.
  
  Buttons: for submitting the form or clearing the fields.

### 3. Implementing the Form using Tkinter

![image](https://github.com/user-attachments/assets/bc9cc76e-4ef0-428e-b5c0-a45faffe6014)

### 4.Explanation:
 Widgets: Label, Entry, comboxbox,Image, treeview, frame and buttons are used to create various parts of the form. 
 
  <b> 1st step: Add the Course Details: </b><br/><br/>
    <b>Add</b> <br/>
          key in the "Course Name" and click "Add" course name will be added and displayed in the list/treeview below.
       
   <b>Update: </b><br/>
       Select the course and update the coursename and click update and the course name will be updated and displayed in the list/treeview below.<br/>
       
   <b>Reset: </b><br/>
       The "Reset" button will clear all the fields.
     
 <b>2nd Step: Enter the Candidate Enrollment Details:</b> <br/>

  <b>Add Candidate:</b> <br/>
          key in the "Candidate Name" <br/>
          Select the "Gender" <br/>
          Enter the "Email Id" <br/>
          Enter the "Mobile" <br/>
          Select the desired "Course" <br/>
          Enter the "Fees" <br/>
    and click "Add" Candidate details will be added and displayed in the list/treeview below.
       
   <b>Update: </b><br/>
       Select a candidate from the list, update the necessary details, and click "Update." The Candidate's information will be updated and reflected in the list/ 
       treeview below.<br/>

   <b>Delete: </b><br/>
       Select a candidate from the list and click "Delete." A confirmation message will appear asking whether you want to delete the record. If you choose "Yes," 
       the candidate's details will be deleted. If you choose "No," the details will remain, and the list/treeview will be displayed again.<br/>
       
   <b>Reset: </b><br/>
       The "Reset" button will clear all the fields.
       
   <b>Exit: </b><br/>
     Clicking "Exit" will prompt a confirmation message asking if you really want to close the window. If you select "Yes," the window will close. If you select 
    "No," it will return to the previous state, and the details will remain displayed in the list/treeview below.

  <b>Search All: </b><br/>
     You can search for a record, and if it exists, it will be displayed; otherwise, no results will be shown.
  
  ![Candidate_Registration](https://github.com/user-attachments/assets/32a540ff-d124-4ae6-87a5-1987011decc1)

  

 ### 5. Storing the Data
In this project, I have used **MySql** database to store the Course Details and Candidate Registration Information. <br/>

<b>Course Table<b>

![image](https://github.com/user-attachments/assets/66cb618c-81eb-479c-a257-34669f09321b)


<b>Student Registration Table </b><br/>

![image](https://github.com/user-attachments/assets/ec6593ed-fcfd-4512-b9ca-b5353a04fad6)



