import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .form import MyForm
import os
from django.conf import settings
from django.http import HttpResponse
from .form import TeacherRegistrationForm, studentmakeform
from django.shortcuts import render
from .models import StudentMark
from .form import EditStudentForm

# Your view logic


student_file_path = os.path.join(settings.BASE_DIR, 'students.csv')
teacher_file_path = os.path.join(settings.BASE_DIR, 'teachers.csv')

def submit_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            submit_type = request.POST.get('submitType')
            user_type = form.cleaned_data['user_type']
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            student_id = form.cleaned_data['student_id']
            cohort = form.cleaned_data['cohort']
            subjects = form.cleaned_data.get('subjects', '')  # New field for subjects
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            if submit_type == 'student':
                # Check for duplicate student
                student_exists = False
                try:
                    with open(student_file_path, 'r') as csvfile:
                        reader = csv.reader(csvfile)
                        for row in reader:
                            if row[2] == student_id:
                                student_exists = True
                                break
                except FileNotFoundError:
                    pass  # If the file doesn't exist, we can proceed to create it
                
                if student_exists:
                    messages.error(request, "Student is already registered.")
                    return redirect('/view/')
                
                # Save student data to CSV
                with open(student_file_path, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([name, last_name, student_id, cohort, subjects])  # Include subjects
                messages.success(request, "Student registered successfully!")
                return redirect('/view/')

            
            elif submit_type == 'teacher':
                # Check for duplicate teacher
                teacher_exists = False
                try:
                    with open(teacher_file_path, 'r') as csvfile:
                        reader = csv.reader(csvfile)
                        for row in reader:
                            if row[0] == username:
                                teacher_exists = True
                                break
                except FileNotFoundError:
                    pass  # If the file doesn't exist, we can proceed to create it
                
                if teacher_exists:
                    messages.error(request, "Teacher is already registered.")
                    return redirect('/teachers/')
                
                # Save teacher data to CSV
                with open(teacher_file_path, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([username, password])
                messages.success(request, "Teacher registered successfully!")
                return redirect('/teachers/')
            
    else:
        form = MyForm()
    return render(request, 'login.html', {'form': form})

def view_csv(request):
    data = []
    try:
        with open(student_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)  # Convert the reader object to a list of rows
    except FileNotFoundError:
        messages.error(request, "CSV file not found.")
    except IOError:
        messages.error(request, "Error reading the file.")
    
    return render(request, 'view.html', {'data': data})

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Check for duplicate teacher
            teacher_exists = False
            try:
                with open(teacher_file_path, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if row[0] == username:
                            teacher_exists = True
                            break
            except FileNotFoundError:
                pass  # If the file doesn't exist, we can proceed to create it
            
            if teacher_exists:
                messages.error(request, "Teacher is already registered.")
                return redirect('/login/')
            
            # Save teacher data to CSV
            with open(teacher_file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([username, password])
            messages.success(request, "Teacher registered successfully!")
            
            return redirect('teachers_page')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'register_teacher.html', {'form': form})
def teachers_page(request):
    return render(request, 'teachers.html')

def home_page(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contract.html')

def log_in_out(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        studentid = request.POST.get('studentid')
        module = request.POST.get('module')
        
        # Check if a user with the provided student ID already exists
        if User.objects.filter(username=studentid).exists():
            messages.info(request, "Student is already registered.")
            return redirect('/register/')
        
        # Create a new User object
        try:
            user = User.objects.create_user(
                username=studentid,  # Use studentid as username
                first_name=first_name,
                last_name=last_name,
                password=None  # Set password to None or handle it as needed
            )
            user.save()
        except Exception as e:
            messages.error(request, f"Error creating user: {e}")
            return redirect('/register/')
        
        # Append the new user data to a CSV file
        with open(student_file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([first_name, last_name, studentid, module])
        
        messages.info(request, "Account created successfully!")
        return redirect('/register/')
    
    return render(request, 'resgis.html')

def mark(request):
    data = []
    try:
        with open(student_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)  # Convert the reader object to a list of rows
    except FileNotFoundError:
        messages.error(request, "CSV file not found.")
    except IOError:
        messages.error(request, "Error reading the file.")
    
    return render(request, 'marking.html', {'data': data})

def studentmark(request):
    
    if request.method == 'POST':
        form = studentmakeform(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            student_id = form.cleaned_data['student_id']
            cohort = form.cleaned_data['cohort']
            Computer_Arquitecture = form.cleaned_data['Computer_Arquitecture']
            Networking = form.cleaned_data['Networking']
            R_Programming = form.cleaned_data['R_Programming']
            
            # Save student data to CSV
            with open(student_file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, last_name, student_id, cohort, Computer_Arquitecture, Networking, R_Programming])
            messages.success(request, "Student registered successfully!")
            return redirect('/mark/')
    else:
        form = studentmakeform()
            
    return render(request, 'studentmake.html', {'form': form})
 # Update with your actual path

def teachers_page(request):
    student_count = 0
    cohort_count = 0
    students = []
    cohorts = set()  # Use a set to collect unique cohorts

    try:
        with open(student_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            students = list(reader)
            student_count = len(students)
            for row in students:
                if len(row) > 3:  # Assuming cohort is in the 4th column
                    cohorts.add(row[3])
            cohort_count = len(cohorts)  # Count the number of unique cohorts
    except FileNotFoundError:
        messages.error(request, "CSV file not found.")
    except IOError:
        messages.error(request, "Error reading the file.")
    
    return render(request, 'teachers.html', {'student_count': student_count, 'students': students, 'cohort_count': cohort_count, 'cohorts': list(cohorts)})







def edit_student(request, student_id):
    student_data = None
    try:
        with open(student_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[2] == student_id:
                    student_data = row
                    break
    except FileNotFoundError:
        messages.error(request, "CSV file not found.")
        return redirect('teachers')
    except IOError:
        messages.error(request, "Error reading the file.")
        return redirect('teachers')

    if not student_data:
        messages.error(request, "Student not found.")
        return redirect('teachers')

    if request.method == 'POST':
        form = EditStudentForm(request.POST)
        if form.is_valid():
            updated_data = [
                form.cleaned_data['name'],
                form.cleaned_data['last_name'],
                form.cleaned_data['student_id'],
                form.cleaned_data['cohort'],
                form.cleaned_data['Computer_Arquitecture'],
                form.cleaned_data['Networking'],
                form.cleaned_data['R_Programming']
            ]

            # Update CSV
            all_students = []
            with open(student_file_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[2] == student_id:
                        all_students.append(updated_data)
                    else:
                        all_students.append(row)

            with open(student_file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(all_students)

            messages.success(request, "Student information updated successfully!")
            return redirect('teachers')
    else:
        form = EditStudentForm(initial={
            'name': student_data[0],
            'last_name': student_data[1],
            'student_id': student_data[2],
            'cohort': student_data[3],
            'Computer_Arquitecture': student_data[4],
            'Networking': student_data[5],
            'R_Programming': student_data[6]
        })

    return render(request, 'edit_student.html', {'form': form, 'student_id': student_id})



def search_csv(request):
    query = request.GET.get('q', '').strip()  # Get and strip the search query
    results = []

    try:
        with open(student_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            if query:
                results = [row for row in data if (query.lower() in row[0].lower() or query.lower() in row[2].lower())]
            # If no query, `results` will remain empty
    except FileNotFoundError:
        messages.error(request, "CSV file not found.")
    except IOError:
        messages.error(request, "Error reading the file.")

    return render(request, 'marking.html', {'query': query, 'results': results})

                                                        
def searchs(request):
    query = request.GET.get('q', '').strip()  # Get and strip the search query
    results = []

    try:
        with open(student_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            if query:
                results = [row for row in data if (query.lower() in row[0].lower() or query.lower() in row[2].lower())]
             # If no query, `results` will remain empty
    except FileNotFoundError:
        messages.error(request, "CSV file not found.")
    except IOError:
        messages.error(request, "Error reading the file.")

    return render(request, 'view.html', {'query': query, 'results': results})

                  