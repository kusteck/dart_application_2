class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class GradeBook:
    def __init__(self):
        self.students = []
        self.subjects = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def add_subject(self, subject):
        self.subjects.append(subject)
        
    def add_grade(self, student, subject, grade):
        if subject not in self.subjects:
            self.subjects.append(subject)
        student.grades[subject] = grade
        
    def calculate_student_avg(self, student):
        if not student.grades:
            return 0
        return sum(student.grades.values()) / len(student.grades)
    
    def calculate_subject_avg(self, subject):
        grades = [s.grades[subject] for s in self.students if subject in s.grades]
        if not grades:
            return 0
        return sum(grades) / len(grades)
    
    def calculate_total_avg(self):
        all_grades = []
        for student in self.students:
            all_grades.extend(student.grades.values())
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def get_category(self, avg_grade):
        if avg_grade >= 4.5:
            return "Отличник"
        elif avg_grade >= 3.5:
            return "Хорошист"
        else:
            return "Остальные"
    
    def print_summary_table(self):
        print("\n" + "="*80)
        print("СВОДНАЯ ТАБЛИЦА УСПЕВАЕМОСТИ")
        print("="*80)
        
        header = "Студент".ljust(25)
        for subject in self.subjects:
            header += subject.ljust(10)
        header += "Ср.балл".ljust(10)
        print(header)
        print("-"*80)
        
        for student in self.students:
            row = student.full_name().ljust(25)
            for subject in self.subjects:
                grade = student.grades.get(subject, "-")
                row += str(grade).ljust(10)
            avg = self.calculate_student_avg(student)
            row += f"{avg:.2f}".ljust(10)
            print(row)
        
        print("-"*80)
        
        row = "Ср.балл по предмету".ljust(25)
        for subject in self.subjects:
            avg = self.calculate_subject_avg(subject)
            row += f"{avg:.2f}".ljust(10)
        print(row)
        print("="*80)
    
    def search_student(self):
        name = input("\nВведите имя или фамилию студента для поиска: ")
        print(f"\nПОИСК СТУДЕНТА: {name}")
        found = False
        for student in self.students:
            if name.lower() in student.full_name().lower():
                found = True
                print(f"Студент: {student.full_name()}")
                print("Оценки:")
                for subject in self.subjects:
                    grade = student.grades.get(subject, "нет оценки")
                    print(f"  {subject}: {grade}")
                avg = self.calculate_student_avg(student)
                print(f"Средний балл: {avg:.2f}")
                category = self.get_category(avg)
                print(f"Категория: {category}")
                print()
        
        if not found:
            print(f"Студент с именем '{name}' не найден")
    
    def print_unique_grades(self):
        print("\nУНИКАЛЬНЫЕ ОЦЕНКИ")
        all_grades = set()
        for student in self.students:
            all_grades.update(student.grades.values())
        print(f"Встречающиеся оценки: {sorted(all_grades)}")
    
    def print_min_max_grades(self):
        print("\nМИНИМАЛЬНЫЕ И МАКСИМАЛЬНЫЕ ОЦЕНКИ ПО ПРЕДМЕТАМ")
        for subject in self.subjects:
            grades_with_students = [(s.grades[subject], s) for s in self.students if subject in s.grades]
            if not grades_with_students:
                continue
                
            max_grade = max(grades_with_students, key=lambda x: x[0])
            min_grade = min(grades_with_students, key=lambda x: x[0])
            
            print(f"\nПредмет: {subject}")
            print(f"  Максимальная оценка: {max_grade[0]} ({max_grade[1].full_name()})")
            print(f"  Минимальная оценка: {min_grade[0]} ({min_grade[1].full_name()})")
    
    def print_students_with_one_failing_grade(self):
        print("\nСТУДЕНТЫ С РОВНО ОДНОЙ ДВОЙКОЙ")
        found = False
        for student in self.students:
            failing_grades = [(subj, grade) for subj, grade in student.grades.items() if grade == 2]
            if len(failing_grades) == 1:
                found = True
                subj, grade = failing_grades[0]
                print(f"{student.full_name()} - предмет: {subj}, оценка: {grade}")
        
        if not found:
            print("Нет студентов с ровно одной двойкой")
    
    def print_subjects_above_average(self):
        print("\nПРЕДМЕТЫ СО СРЕДНИМ БАЛЛОМ ВЫШЕ ОБЩЕГО")
        total_avg = self.calculate_total_avg()
        print(f"Общий средний балл по группе: {total_avg:.2f}")
        
        above_avg = []
        for subject in self.subjects:
            subject_avg = self.calculate_subject_avg(subject)
            if subject_avg > total_avg:
                above_avg.append((subject, subject_avg))
        
        if above_avg:
            for subject, avg in above_avg:
                print(f"{subject}: {avg:.2f}")
        else:
            print("Нет предметов со средним баллом выше общего")
    
    def print_categories_count(self):
        print("\nКОЛИЧЕСТВО СТУДЕНТОВ ПО КАТЕГОРИЯМ")
        categories = {"Отличник": 0, "Хорошист": 0, "Остальные": 0}
        
        for student in self.students:
            avg = self.calculate_student_avg(student)
            category = self.get_category(avg)
            categories[category] += 1
        
        for category, count in categories.items():
            print(f"{category}: {count}")

def main():
    gradebook = GradeBook()
    
    subjects = ["Математика", "Физика", "Информатика", "Литература", "История"]
    for subject in subjects:
        gradebook.add_subject(subject)
    
    students_data = [
        ("Иван", "Петров"),
        ("Мария", "Иванова"),
        ("Петр", "Сидоров"),
        ("Анна", "Смирнова"),
        ("Дмитрий", "Козлов"),
        ("Елена", "Морозова")
    ]
    
    students = []
    for first, last in students_data:
        student = Student(first, last)
        gradebook.add_student(student)
        students.append(student)
    
    grades_data = [
        (students[0], "Математика", 5),
        (students[0], "Физика", 4),
        (students[0], "Информатика", 5),
        (students[0], "Литература", 3),
        (students[0], "История", 4),
        
        (students[1], "Математика", 5),
        (students[1], "Физика", 5),
        (students[1], "Информатика", 5),
        (students[1], "Литература", 5),
        (students[1], "История", 4),
        
        (students[2], "Математика", 3),
        (students[2], "Физика", 2),
        (students[2], "Информатика", 4),
        (students[2], "Литература", 3),
        (students[2], "История", 3),
        
        (students[3], "Математика", 5),
        (students[3], "Физика", 4),
        (students[3], "Информатика", 4),
        (students[3], "Литература", 5),
        (students[3], "История", 5),
        
        (students[4], "Математика", 2),
        (students[4], "Физика", 3),
        (students[4], "Информатика", 2),
        (students[4], "Литература", 4),
        (students[4], "История", 3),
        
        (students[5], "Математика", 4),
        (students[5], "Физика", 4),
        (students[5], "Информатика", 4),
        (students[5], "Литература", 4),
        (students[5], "История", 4),
    ]
    
    for student, subject, grade in grades_data:
        gradebook.add_grade(student, subject, grade)
    
    gradebook.print_summary_table()
    gradebook.search_student()
    gradebook.print_unique_grades()
    gradebook.print_min_max_grades()
    gradebook.print_students_with_one_failing_grade()
    gradebook.print_subjects_above_average()
    gradebook.print_categories_count()

if __name__ == "__main__":
    main()