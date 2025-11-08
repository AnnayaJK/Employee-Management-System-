from customtkinter import *
from PIL import Image
from tkinter import messagebox
import database  # Import database functions

class IntegratedApp:  # New: Wrap everything in a class for better management
    def __init__(self):
        self.root = CTk()
        self.root.geometry('1000x600')
        self.root.resizable(0, 0)
        self.root.title('Login Page')
        self.show_login()  # Start with login
        self.root.mainloop()
    
    def show_login(self):  # Original login setup, now as a method
        # Clear any existing widgets (for transition from EMS if needed)
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(fg_color='white')  # Reset background
        image = CTkImage(Image.open("image.jpg"), size=(1000, 600))
        imageLabel = CTkLabel(self.root, image=image, text="")
        imageLabel.place(x=0, y=0)
        
        headinglabel = CTkLabel(self.root, text='Employee Management System', bg_color='white', font=('Goudy Old Style', 20, 'bold'), text_color='dark blue')
        headinglabel.place(x=20, y=100)
        
        self.usernameEntry = CTkEntry(self.root, placeholder_text='Enter Your Username', width=180)
        self.usernameEntry.place(x=50, y=150)
        
        self.passwordEntry = CTkEntry(self.root, placeholder_text="Enter Your Password", width=180, show="*")
        self.passwordEntry.place(x=50, y=200)
        
        loginButton = CTkButton(self.root, text="Login", cursor="hand2", command=self.login)
        loginButton.place(x=70, y=250)
    
    def login(self):  # Modified: On success, show EMS instead of destroy/import
        if self.usernameEntry.get() == "" or self.passwordEntry.get() == "":
            messagebox.showerror('Error', 'Fields Cannot be Empty')
        elif self.usernameEntry.get() == 'Jyoti' and self.passwordEntry.get() == '123456':
            messagebox.showinfo('Success', 'Logged in Successfully')
            self.show_ems()  # New: Transition to EMS
        else:
            messagebox.showerror('Error', 'Wrong Credentials')
    
    # New: EMS methods integrated from ems.py
    def show_ems(self):
        # Clear login widgets and set up EMS (adapted from your ems.py)
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.title("Employee Management System")
        self.root.configure(fg_color='#161C30')
        
        logo = CTkImage(Image.open("image5.jpg"), size=(1000, 150))
        logoLabel = CTkLabel(self.root, image=logo, text="")
        logoLabel.grid(row=0, column=0, columnspan=2)
        
        # Left Frame
        leftFrame = CTkFrame(self.root, fg_color='#161C30')
        leftFrame.grid(row=1, column=0)
        
        idLabel = CTkLabel(leftFrame, text='Id', font=('arial', 18, 'bold'), text_color='white')
        idLabel.grid(row=0, column=0, padx=20, pady=15, sticky='w')
        self.idEntry = CTkEntry(leftFrame, width=180)
        self.idEntry.grid(row=0, column=1)
        
        nameLabel = CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'), text_color='white')
        nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky='w')
        self.nameEntry = CTkEntry(leftFrame, width=180)
        self.nameEntry.grid(row=1, column=1)
        
        phoneLabel = CTkLabel(leftFrame, text='Phone Number', font=('arial', 18, 'bold'), text_color='white')
        phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky='w')
        self.phoneEntry = CTkEntry(leftFrame, width=180)
        self.phoneEntry.grid(row=2, column=1)
        
        roleLabel = CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'), text_color='white')
        roleLabel.grid(row=3, column=0, padx=20, pady=15, sticky='w')
        role_options = ['Web Developer', 'Cloud Architect', 'Technical Writer', 'Network Engineer', 'Data Scientist', 'Business Analyst', 'IT Consultant', 'UX/UI Designer']
        self.roleBox = CTkComboBox(leftFrame, values=role_options, width=180, font=('arial', 18, 'bold'), state='readonly')
        self.roleBox.set('Select Role')
        self.roleBox.grid(row=3, column=1)
        
        genderLabel = CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'), text_color='white')
        genderLabel.grid(row=4, column=0, padx=20, pady=15, sticky='w')
        genderOptions = ['Male', 'Female', 'Others']
        self.genderBox = CTkComboBox(leftFrame, values=genderOptions, width=180, font=('arial', 18, 'bold'), state='readonly')
        self.genderBox.set('Select Gender')
        self.genderBox.grid(row=4, column=1)
        
        salaryLabel = CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'), text_color='white')
        salaryLabel.grid(row=5, column=0, padx=20, pady=15, sticky='w')
        self.salaryEntry = CTkEntry(leftFrame, width=180)
        self.salaryEntry.grid(row=5, column=1)
        
        # Right Frame
        rightFrame = CTkFrame(self.root)
        rightFrame.grid(row=1, column=1)
        
        search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
        self.searchBox = CTkComboBox(rightFrame, values=search_options, width=180, font=('arial', 18, 'bold'), state='readonly')
        self.searchBox.set('Search By')
        self.searchBox.grid(row=0, column=0)
        
        self.searchEntry = CTkEntry(rightFrame)
        self.searchEntry.grid(row=0, column=1)
        
        searchButton = CTkButton(rightFrame, text='Search', width=100, command=self.search_employee)
        searchButton.grid(row=0, column=2)
        
        showallButton = CTkButton(rightFrame, text='Show All', width=100, command=self.show_all)
        showallButton.grid(row=0, column=3, pady=5)
        
        from tkinter import ttk  # Import here if not at top
        self.tree = ttk.Treeview(rightFrame, height=13)
        self.tree.grid(row=1, column=0, columnspan=4)
        
        self.tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')
        self.tree.heading('Id', text='Id')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Phone', text='Phone')
        self.tree.heading('Role', text='Role')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Salary', text='Salary')
        self.tree.config(show='headings')
        
        self.tree.column('Id', width=80)
        self.tree.column('Name', width=160)
        self.tree.column('Phone', width=160)
        self.tree.column('Role', width=160)
        self.tree.column('Gender', width=100)
        self.tree.column('Salary', width=120)
        
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('arial', 18, 'bold'))
        style.configure('Treeview', font=('arial', 12, 'bold'), rowheight=30, background='#161C30', foreground='white')
        
        scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=1, column=4, sticky='ns')
        self.tree.config(yscrollcommand=scrollbar.set)
        
        # Button Frame
        buttonFrame = CTkFrame(self.root, fg_color='#161C30')
        buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)
        
        newButton = CTkButton(buttonFrame, text='New Employee', font=('arial', 18, 'bold'), width=160, corner_radius=15, command=lambda: self.clear(True))
        newButton.grid(row=0, column=0, pady=5, padx=5)
        
        addButton = CTkButton(buttonFrame, text='Add Employee', font=('arial', 18, 'bold'), width=160, corner_radius=15, command=self.add_employee)
        addButton.grid(row=0, column=1, pady=5, padx=5)
        
        updateButton = CTkButton(buttonFrame, text='Update Employee', font=('arial', 18, 'bold'), width=160, corner_radius=15, command=self.update_employee)
        updateButton.grid(row=0, column=2, pady=5, padx=5)
        
        deleteButton = CTkButton(buttonFrame, text='Delete Employee', font=('arial', 18, 'bold'), width=160, corner_radius=15, command=self.delete_employee)
        deleteButton.grid(row=0, column=3, pady=5, padx=5)
        
        deleteallButton = CTkButton(buttonFrame, text='Delete All Employee', font=('arial', 18, 'bold'), width=160, corner_radius=15, command=self.delete_all)
        deleteallButton.grid(row=0, column=4, pady=5, padx=5)
        
        self.treeview_data()
        self.root.bind('<ButtonRelease>', self.selection)
    
    # EMS functions (adapted from your ems.py, with self. prefixes)
    def delete_all(self):
        result = messagebox.askyesno('Confirm', 'Do you really want to delete all the records?')
        if result:
            database.deleteall_records()
            self.treeview_data()
            self.searchEntry.delete(0, END)
            self.searchBox.set('Search By')
    
    def show_all(self):
        self.treeview_data()
        self.searchEntry.delete(0, END)
        self.searchBox.set('Search By')
    
    def search_employee(self):
        if self.searchEntry.get() == '':
            messagebox.showerror('Error', 'Enter value to search')
        elif self.searchBox.get() == 'Search By':
            messagebox.showerror('Error', 'Please select an option')
        else:
            searched_data = database.search(self.searchBox.get(), self.searchEntry.get())
            self.tree.delete(*self.tree.get_children())
            for employee in searched_data:
                self.tree.insert('', END, values=employee)
    
    def delete_employee(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror('Error', 'Select data to delete')
        else:
            database.delete(self.idEntry.get())
            self.treeview_data()
            self.clear()
            messagebox.showinfo('Success', 'Data Deleted Successfully')  # Fixed: Was error, now success
    
    def update_employee(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror('Error', 'Select data to update')
        else:
            database.update(self.idEntry.get(), self.nameEntry.get(), self.phoneEntry.get(), self.roleBox.get(), self.genderBox.get(), self.salaryEntry.get())
            self.treeview_data()
            self.clear()
            messagebox.showinfo('Success', 'Updated successfully')
    
    def selection(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear()
            self.idEntry.insert(0, row[0])
            self.nameEntry.insert(0, row[1])
            self.phoneEntry.insert(0, row[2])
            self.roleBox.set(row[3])
            self.genderBox.set(row[4])
            self.salaryEntry.insert(0, row[5])
    
    def clear(self, value=False):
        if value:
            self.tree.selection_remove(self.tree.focus())
        self.idEntry.delete(0, END)
        self.nameEntry.delete(0, END)
        self.phoneEntry.delete(0, END)
        self.roleBox.set('Select Role')
        self.genderBox.set('Select Gender')
        self.salaryEntry.delete(0, END)
    
    def treeview_data(self):
        employees = database.fetch_employees()
        self.tree.delete(*self.tree.get_children())
        for employee in employees:
            self.tree.insert('', END, values=employee)
    
    def add_employee(self):
        if self.idEntry.get() == '' or self.phoneEntry.get() == '' or self.nameEntry.get() == '' or self.salaryEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        elif database.id_exists(self.idEntry.get()):
            messagebox.showerror('Error', 'ID Already Exists')
        elif not self.idEntry.get().startswith('EMP'):
            messagebox.showerror('Error', "Invalid ID format. Use 'EMP' followed by a number (e.g. 'EMP1').")
        else:
            database.insert(self.idEntry.get(), self.nameEntry.get(), self.phoneEntry.get(), self.roleBox.get(), self.genderBox.get(), self.salaryEntry.get())
            self.treeview_data()
            self.clear()
            messagebox.showinfo('Success', 'Data Added Successfully')

# Run the app
if __name__ == "__main__":
    IntegratedApp()