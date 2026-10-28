
def display_menu():
    print("\n" + "=" * 40)
    print("      STUDENT ASSIGNMENT TRACKER")
    print("=" * 40)
    print("1. Add New Assignment")
    print("2. View All Assignments")
    print("3. Update Assignment")
    print("4. Mark Assignment as Completed")
    print("5. Exit")
    print("=" * 40)

def add_assignment(assignments):
    print("\n--- Add New Assignment ---")
    title = input("Enter Assignment Title: ").strip()
    subject = input("Enter Subject Name: ").strip()
    deadline = input("Enter Deadline (e.g., 15 Nov): ").strip()
    
    if title == "" or subject == "":
        print("Error: Title and Subject cannot be blank!")
        return
        
    assignment = {
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "status": "Pending"
    }
    assignments.append(assignment)
    print(f"Success: Assignment '{title}' added successfully!")

def view_assignments(assignments):
    print("\n--- List of Assignments ---")
    if len(assignments) == 0:
        print("No assignments found. Your list is empty!")
        return
        
    print(f"{'No.':<4} | {'Title':<20} | {'Subject':<15} | {'Deadline':<12} | {'Status'}")
    print("-" * 65)
    for index, task in enumerate(assignments, start=1):
        print(f"{index:<4} | {task['title']:<20} | {task['subject']:<15} | {task['deadline']:<12} | [{task['status']}]")

def update_assignment(assignments):
    print("\n--- Update Assignment ---")
    if len(assignments) == 0:
        print("No assignments available to update.")
        return
        
    view_assignments(assignments)
    try:
        choice = int(input("\nEnter Assignment Number to Update: "))
        if 1 <= choice <= len(assignments):
            task = assignments[choice - 1]
            print(f"Updating '{task['title']}' (Press Enter to keep current value):")
            
            new_title = input(f"New Title [{task['title']}]: ").strip()
            new_subject = input(f"New Subject [{task['subject']}]: ").strip()
            new_deadline = input(f"New Deadline [{task['deadline']}]: ").strip()
            
            if new_title:
                task['title'] = new_title
            if new_subject:
                task['subject'] = new_subject
            if new_deadline:
                task['deadline'] = new_deadline
                
            print("Success: Assignment updated successfully!")
        else:
            print("Error: Invalid assignment number!")
    except ValueError:
        print("Error: Please enter a valid number!")

def mark_completed(assignments):
    print("\n--- Mark Assignment as Completed ---")
    if len(assignments) == 0:
        print("No assignments available.")
        return
        
    view_assignments(assignments)
    try:
        choice = int(input("\nEnter Assignment Number to Mark as Completed: "))
        if 1 <= choice <= len(assignments):
            assignments[choice - 1]['status'] = "Completed"
            print(f"Success: '{assignments[choice - 1]['title']}' marked as Completed!")
        else:
            print("Error: Invalid assignment number!")
    except ValueError:
        print("Error: Please enter a valid number!")

def main():
    assignments = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_assignment(assignments)
        elif choice == '2':
            view_assignments(assignments)
        elif choice == '3':
            update_assignment(assignments)
        elif choice == '4':
            mark_completed(assignments)
        elif choice == '5':
            print("\nThank you for using Student Assignment Tracker. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
