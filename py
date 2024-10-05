class Student:
    def __init__(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Registration Number: {self.reg_number}")

# Example usage
student1 = Student("Racheal Rita", "REGS23B13/003")
student1.display_info()

student2 = Student("Sammy Maloba", "REGS23B13/017")
student2.display_info()

student3 = Student("Mukisa Moreen", "REGS23B13/66")
student3.display_info()

student4 = Student("Akello Joy Peace", "REGS23B13/099")
student4.display_info()
