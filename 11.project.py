class Student:
    def __init__(self, firstname: str, lastname: str, tnumber: str):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []  # list of string grades, may be empty initially

    def RunningAverage(self):
        # Calculate average of non-blank scores only
        if not self.Grades:
            return 0.0
        numeric_grades = [float(grade) for grade in self.Grades if grade.strip() != '']
        if not numeric_grades:
            return 0.0
        return sum(numeric_grades)/len(numeric_grades)

    def TotalAverage(self):
        # Calculate average treating missing scores (blank strings) as zero
        if not self.Grades:
            return 0.0
        total_scores = 0.0
        count = len(self.Grades)
        for grade in self.Grades:
            if grade.strip() == '':
                total_scores += 0.0
            else:
                total_scores += float(grade)
        return total_scores / count if count > 0 else 0.0

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

class StudentList:
    def __init__(self):
        self.Studentlist = []  # list of Student objects

    def add_student(self, FirstName: str, LastName: str, TNumber: str):
        student = Student(FirstName, LastName, TNumber)
        self.Studentlist.append(student)

    def find_student(self, TNumber: str):
        for idx, student in enumerate(self.Studentlist):
            if student.TNumber == TNumber:
                return idx
        return -1

    def print_student_list(self):
        # Print headers with alignment like example output
        print("       First         Last           ID      Running     Semester       Letter")
        print("        Name         Name       Number      Average      Average        Grade")
        print("------------ ------------ ------------ ------------ ------------ ------------")
        for student in self.Studentlist:
            print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} "
                  f"{student.RunningAverage():>12.2f} {student.TotalAverage():>12.2f} "
                  f"{student.LetterGrade():>12}")

    def add_student_from_file(self, filename: str):
        """
        File format assumed:
        Each line contains FirstName,LastName,TNumber separated by commas
        """
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line == '':
                    continue
                parts = line.split(',')
                if len(parts) < 3:
                    # malformed line
                    continue
                firstname, lastname, tnumber = parts[0].strip(), parts[1].strip(), parts[2].strip()
                self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename: str):
        """
        File format assumed:
        Each line contains TNumber followed by comma separated grades (strings)
        Example:
        T123456,78,85,90,88, ...
        """
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line == '':
                    continue
                parts = line.split(',')
                if len(parts) < 1:
                    continue
                tnumber = parts[0].strip()
                grades = parts[1:]  # list of string grades; can include blank strings
                idx = self.find_student(tnumber)
                if idx != -1:
                    # append grades to student
                    self.Studentlist[idx].Grades.extend(grades)
                else:
                    # student not found - ignore
                    pass

def main():
    student_list = StudentList()

    # Add students from file
    student_file = '11.Project Students.txt'
    student_list.add_student_from_file(student_file)

    # Add scores from file
    scores_file = '11.Project Scores.txt'
    student_list.add_scores_from_file(scores_file)

    # Print student info
    student_list.print_student_list()

if __name__ == "__main__":
    main()
