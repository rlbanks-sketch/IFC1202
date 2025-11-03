class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores  # list of strings

    def RunningAverage(self):
        # Calculate average ignoring blank scores
        numeric_scores = [float(score) for score in self.Grades if score.strip() != '']
        if numeric_scores:
            return sum(numeric_scores) / len(numeric_scores)
        else:
            return 0.0

    def TotalAverage(self):
        # Treat blank scores as zero
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

            print(f"Student: {student.FirstName} {student.LastName} ({student.TNumber})")
            print(f"  Running Average: {student.RunningAverage():.2f}")
            print(f"  Total Average: {student.TotalAverage():.2f}")
            print(f"  Letter Grade: {student.LetterGrade()}")
            print()


if __name__ == "__main__":
    main()
