import json

# File to store the todos
TODOS_FILE = "todos.json"

def load_todos():
    try:
        with open(TODOS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open(TODOS_FILE, "w") as f:
        json.dump(todos, f)

def show_todos(todos):
    if not todos:
        print("No todos found.")
    else:
        for i, todo in enumerate(todos, 1):
            status = "Done" if todo["completed"] else "Not Done"
            print(f"{i}. {todo['task']} - {status}")

def add_todo(todos, task):
    todos.append({"task": task, "completed": False})
    save_todos(todos)
    print(f"Added: {task}")

def complete_todo(todos, index):
    if 1 <= index <= len(todos):
        todos[index-1]["completed"] = True
        save_todos(todos)
        print(f"Marked as complete: {todos[index-1]['task']}")
    else:
        print("Invalid todo number.")

def delete_todo(todos, index):
    if 1 <= index <= len(todos):
        task = todos.pop(index-1)
        save_todos(todos)
        print(f"Deleted: {task['task']}")
    else:
        print("Invalid todo number.")

def main():
    todos = load_todos()
    
    while True:
        print("\n--- Todo List Application ---")
        print("1. Show todos")
        print("2. Add todo")
        print("3. Complete todo")
        print("4. Delete todo")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            task = input("Enter the task: ")
            add_todo(todos, task)
        elif choice == "3":
            index = int(input("Enter the todo number to mark as complete: "))
            complete_todo(todos, index)
        elif choice == "4":
            index = int(input("Enter the todo number to delete: "))
            delete_todo(todos, index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()