from tabulate import tabulate

class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores  # list of strings

    def RunningAverage(self):
        numeric_scores = [float(score) for score in self.Grades if score.strip() != '']
        if numeric_scores:
            return sum(numeric_scores) / len(numeric_scores)
        else:
            return 0.0

    def TotalAverage(self):
        total_scores = []
        for score in self.Grades:
            if score.strip() == '':
                total_scores.append(0.0)
            else:
                total_scores.append(float(score))
        if total_scores:
            return sum(total_scores) / len(total_scores)
        else:
            return 0.0

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


def main():
    filename = "10.Project Student Scores.txt"
    students = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # skip blank lines
            parts = line.split(',')
            if len(parts) < 4:
                print(f"Skipping invalid line (not enough parts): {line}")
                continue
            firstname, lastname, tnumber = parts[:3]
            scores = parts[3:]
            student = Student(firstname, lastname, tnumber, scores)
            students.append(student)

    # Prepare data for tabulate
    table = []
    for s in students:
        table.append([
            s.FirstName,
            s.LastName,
            s.TNumber,
            f"{s.RunningAverage():.2f}",
            f"{s.TotalAverage():.2f}",
            s.LetterGrade()
        ])

    headers = ["First Name", "Last Name", "TNumber", "Running Average", "Total Average", "Letter Grade"]
    print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
