class Employee:
    def __init__(self, name, id, title, dept):
        self.name = name
        self.id = id
        self.title = title
        self.dept = dept

    def display_employee_details(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.dept}")

    def __str__(self):
        return f"{self.name} - ID: {self.id}"