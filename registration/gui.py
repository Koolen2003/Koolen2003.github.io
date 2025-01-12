import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox
import os.path
Large_Font = ('Verdana', 12)

class RegistrationForm(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (home_page, mark, view):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(home_page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class home_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page", font=Large_Font)
        label.pack(pady=10)
        
        # Frame for buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        button1 = tk.Button(button_frame, text="Input Mark", command=lambda: controller.show_frame(mark))
        button1.pack(side="left", padx=5)
        button2 = tk.Button(button_frame, text="View", command=lambda: controller.show_frame(view))
        button2.pack(side="left", padx=5)

        # Display number of students and cohorts
        self.student_count_label = tk.Label(self, text="", font=Large_Font)
        self.student_count_label.pack(pady=10)
        self.update_student_count()

    def update_student_count(self):
        with open(r"C:\Users\HP\Desktop\monopoly sub\registration\students.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            students = list(csv_reader)
            student_count = len(students)
            cohors_set = set(student[3] for student in students) # Assuming cohors is in the 4th column
            cohors_count = len(cohors_set)
            self.student_count_label.config(text=f"Number of Students: {student_count}, Number of Cohorts: {cohors_count}")

class mark(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Input Mark", font=Large_Font)
        label.pack(pady=10)
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(home_page))
        button1.pack(pady=5)

        # Create a form layout for the fields
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10, padx=10)

        # Adding input fields for student data
        self.label1 = tk.Label(form_frame, text="Student First Name:")
        self.label1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry1 = tk.Entry(form_frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.label2 = tk.Label(form_frame, text="Student Last Name:")
        self.label2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry2 = tk.Entry(form_frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        self.label3 = tk.Label(form_frame, text="Student ID:")
        self.label3.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry3 = tk.Entry(form_frame)
        self.entry3.grid(row=2, column=1, padx=5, pady=5)

        self.label4 = tk.Label(form_frame, text="Cohors:")
        self.label4.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry4 = tk.Entry(form_frame)
        self.entry4.grid(row=3, column=1, padx=5, pady=5)

        self.label5 = tk.Label(form_frame, text="Computer Architecture:")
        self.label5.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry5 = tk.Entry(form_frame)
        self.entry5.grid(row=4, column=1, padx=5, pady=5)

        self.label6 = tk.Label(form_frame, text="Networking:")
        self.label6.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry6 = tk.Entry(form_frame)
        self.entry6.grid(row=5, column=1, padx=5, pady=5)

        self.label7 = tk.Label(form_frame, text="R programming:")
        self.label7.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry7 = tk.Entry(form_frame)
        self.entry7.grid(row=6, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self, text="Save", command=self.save_data)
        self.save_button.pack(pady=10)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_data)
        self.delete_button.pack(pady=10)

    def save_data(self):
        student_first_name = self.entry1.get()
        student_last_name = self.entry2.get()
        student_id = self.entry3.get()
        cohors = self.entry4.get()
        comp_arch = self.entry5.get()
        networking = self.entry6.get()
        r_programming = self.entry7.get()
        name = self.entry1.get()
        last_name = self.entry2.get()
        student_id = self.entry3.get()
        cohors = self.entry4.get()

        message = f"Name: {name} \nLast Name: {last_name} \nStudent ID: {student_id} \nCohors: {cohors}"
        tk.messagebox.showinfo("Student Information have been saved", message)
        # Check for existing student
        existing_student = False
        with open(r"C:\Users\HP\Desktop\monopoly sub\registration\students.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if student_first_name == row[0] and student_last_name == row[1] or student_id == row[2]:
                    existing_student = True
                    break

        if existing_student:
            tk.messagebox.showerror("Error", "Student with the same name or ID already exists.")
        else:
            with open(r"C:\Users\HP\Desktop\monopoly sub\registration\students.csv", mode='a', newline="") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([student_first_name, student_last_name, student_id, cohors, comp_arch, networking, r_programming])
        
            # Update the student count on home page
            self.controller.frames[home_page].update_student_count()

    def delete_data(self):
        student_id = self.entry3.get()

        lines = []
        with open(r"C:\Users\HP\Desktop\monopoly sub\registration\students.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[2] != student_id:
                    lines.append(row)

        with open(r"C:\Users\HP\Desktop\monopoly sub\registration\students.csv", mode='w', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(lines)

        # Update the student count on home page
        self.controller.frames[home_page].update_student_count()

class view(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="View Mark", font=("Arial", 16))
        label.pack(pady=10)
        
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(home_page))
        button1.pack(pady=5)

        self.tree = ttk.Treeview(self, columns=('First Name', 'Last Name', 'Student ID', 'Cohors', 'Computer Architecture', 'Networking', 'R programming'), show='headings')
        self.tree.heading('First Name', text='First Name')
        self.tree.heading('Last Name', text='Last Name')
        self.tree.heading('Student ID', text='Student ID')
        self.tree.heading('Cohors', text='Cohors')
        self.tree.heading('Computer Architecture', text='Computer Architecture')
        self.tree.heading('Networking', text='Networking')
        self.tree.heading('R programming', text='R programming')

        self.tree.column('First Name', width=100)
        self.tree.column('Last Name', width=100)
        self.tree.column('Student ID', width=100)
        self.tree.column('Cohors', width=100)
        self.tree.column('Computer Architecture', width=150)
        self.tree.column('Networking', width=150)
        self.tree.column('R programming', width=150)

        self.tree.pack(fill=tk.BOTH, expand=True)

        open_button = tk.Button(self, text="Open CSV", command=self.open_csv)
        open_button.pack(pady=10)

        search_label = tk.Label(self, text="Search by ID or Name:")
        search_label.pack(pady=5)
        self.search_entry = tk.Entry(self)
        self.search_entry.pack(pady=5)
        search_button = tk.Button(self, text="Search", command=self.search_data)
        search_button.pack(pady=5)

        delete_button = tk.Button(self, text="Delete", command=self.delete_data)
        delete_button.pack(pady=5)

        update_button = tk.Button(self, text="Update", command=self.update_data)
        update_button.pack(pady=5)

    def open_csv(self):
        file_path = "C:/Users/HP/Desktop/monopoly sub/registration/students.csv"
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            self.tree.delete(*self.tree.get_children())
            for row in reader:
                self.tree.insert("", tk.END, values=row)

    def search_data(self):
        search_term = self.search_entry.get()
        file_path = "C:/Users/HP/Desktop/monopoly sub/registration/students.csv"
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            self.tree.delete(*self.tree.get_children())
            for row in reader:
                if search_term in row[0] or search_term in row[1] or search_term == row[2]:
                    self.tree.insert("", tk.END, values=row)

    def delete_data(self):
        selected_items = self.tree.selection()
        if selected_items:
            for selected_item in selected_items:
                values = self.tree.item(selected_item, 'values')
                student_id = values[2]

                lines = []
                with open("C:/Users/HP/Desktop/monopoly sub/registration/students.csv", mode='r') as file:
                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        if row[2] != student_id:
                            lines.append(row)

                with open("C:/Users/HP/Desktop/monopoly sub/registration/students.csv", mode='w', newline="") as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(lines)

                self.tree.delete(selected_item)

            messagebox.showinfo("Info", "Selected student data deleted successfully.")
        else:
            search_term = self.search_entry.get()
            if search_term:
                lines = []
                deleted = False

                file_path = "C:/Users/HP/Desktop/monopoly sub/registration/students.csv"
                with open(file_path, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if search_term in row[0] or search_term in row[1] or search_term == row[2]:
                            deleted = True
                            continue
                        lines.append(row)

                if deleted:
                    with open(file_path, mode='w', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(lines)

                    self.open_csv()
                    messagebox.showinfo("Info", "Student data deleted successfully.")
                else:
                    messagebox.showerror("Error", "No matching student data found.")

    def update_data(self):
        selected_items = self.tree.selection()
        if selected_items:
            item = selected_items[0]
            values = self.tree.item(item, 'values')
            self.show_update_window(values)

    def show_update_window(self, values):
        update_window = tk.Toplevel(self)
        update_window.title("Update Student Information")

        fields = ['First Name', 'Last Name', 'Student ID', 'Cohors', 'Computer Architecture', 'Networking', 'R programming']
        entries = {}

        for idx, field in enumerate(fields):
            label = tk.Label(update_window, text=field)
            label.grid(row=idx, column=0, padx=10, pady=5)
            entry = tk.Entry(update_window)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entry.insert(0, values[idx])
            entries[field] = entry

        def save_changes():
            updated_values = [entries[field].get() for field in fields]
            self.update_csv(values[2], updated_values)
            self.open_csv()
            update_window.destroy()

        save_button = tk.Button(update_window, text="Save", command=save_changes)
        save_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

    def update_csv(self, student_id, updated_values):
        file_path = "C:/Users/HP/Desktop/monopoly sub/registration/students.csv"
        lines = []

        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[2] == student_id:
                    lines.append(updated_values)
                else:
                    lines.append(row)

        with open(file_path, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(lines)

def refresh(student):
    for child in csv_frame.winfo_children():
        child.destroy()

    with open(student) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            label = tk.Label(csv_frame, text=", ".join(row))
            label.pack(side="top", anchor="w")
                
def auto_refresh(student, last_mtime=-1):
    mtime = os.path.getmtime(student)
    if mtime > last_mtime:
        refresh(student)
    root.after(1000, auto_refresh, student, mtime)

root = tk.Tk()
csv_frame = tk.Frame(root)
csv_frame.pack(side="top", fill="both", expand=True)


auto_refresh("C:/Users/HP/Desktop/monopoly sub/registration/students.csv")
    





# Run the application
app = RegistrationForm()
app.geometry("1000x700")
app.mainloop()
