
# 1. Library Book Tracker
library = []
def add_book(title="",author="",page=""):
    books=[title,author,page]
    library.extend(books)
    return library
add_book("1984", "George Orwell", 328)
   
def find_book(search=""):
    for x in library:
        if x == search:
            print(f"Book Found= {library}")
            return 
        else:
            return print("Book not found.")    
find_book("1984")
    
def show_books():
    
    return print(library)
show_books()

# 2. Student Grade Manager
grades = []
def add_student(name=""):
    grades.append(name)
    return grades
add_student("Alicia")  
    
def add_grade(name="",note1=0):
    
    grades.append(note1)
    return grades         
add_grade(add_student,80)


def get_average(name="",note=0):
    
    for x in grades:
        if x in name:
            print(f"x = {x}")
            if x == 80:
                print(x)


get_average("Alicia")
          
# 3. Restaurant Menu Editor
def add_dish(): pass
def change_availability(): pass
def total_available_price(): pass

# 4. Warehouse Box Counter
def add_box(): pass
def update_quantity(): pass
def has_enough(): pass

# 5. Movie Rating System
def add_movie(): pass
def rate_movie(): pass
def average_rating(): pass

# 6. Online Course Tracker
def add_course(): pass
def update_enrollment(): pass
def filter_by_hours(): pass

# 7. To-Do List Organizer
def add_task(): pass
def complete_task(): pass
def filter_tasks(): pass

# 8. Digital Wallet
def add_expense(): pass
def total_spent(): pass
def expense_percentages(): pass

# 9. Pet Adoption Center
def add_pet(): pass
def find_by_species(): pass
def older_than(): pass

# 10. Gym Membership System
def register_member(): pass
def change_plan(): pass
def unpaid_members(): pass
