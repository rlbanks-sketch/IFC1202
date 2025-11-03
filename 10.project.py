from typing import List

class Student:
    def __init__(self, firstname: str, lastname: str, tnumber: str, scores: List[str]):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores  # list of string scores, may contain blanks

    def RunningAverage(self) -> float:
        # Calculate average of non-blank scores
        non_blank_scores = [float(score) for score in self.Grades if score.strip() != '']
        if len(non_blank_scores) == 0:
            return 0.0
        return sum(non_blank_scores) / len(non_blank_scores)

    def TotalAverage(self) -> float:
        # Treat missing (blank) scores as zero
        scores_with_zero = [float(score) if score.strip() != '' else 0.0 for score in self.Grades]
        if len(scores_with_zero) == 0:
            return 0.0
        return sum(scores_with_zero) / len(scores_with_zero)

    def LetterGrade(self) -> str:
        avg = self.TotalAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

def main():
    students = []
    try:
        with open('StudentScores.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) < 3:
                    # Skip malformed lines
                    continue
                firstname, lastname, tnumber = parts[:3]
                scores = parts[3:]  # Remaining are scores, may be empty strings

                student = Student(firstname, lastname, tnumber, scores)
                students.append(student)
    except FileNotFoundError:
        print("Error: 'StudentScores.txt' not found.")
        return

    # Print header
    print(f"{'First':>12} {'Last':>12} {'ID':>12} {'Running':>12} {'Semester':>12} {'Letter':>12}")
    print(f"{'Name':>12} {'Name':>12} {'Number':>12} {'Average':>12} {'Average':>12} {'Grade':>12}")
    print(f"{'-'*12} {'-'*12} {'-'*12} {'-'*12} {'-'*12} {'-'*12}")

    for s in students:
        running_avg = s.RunningAverage()
        semester_avg = s.TotalAverage()
        letter = s.LetterGrade()
        print(f"{s.FirstName:>12} {s.LastName:>12} {s.TNumber:>12} {running_avg:12.2f} {semester_avg:12.2f} {letter:12}")

if __name__ == "__main__":
    main()
