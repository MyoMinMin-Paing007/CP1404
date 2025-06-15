"""
CP1404/CP5632 Practical
Data file -> lists program
"""

def main():
    """Read subject data and display subject details."""
    filename = "subject_data.txt"
    data = load_data(filename)
    display_subject_details(data)

def load_data(filename):
    """Read data from file and return a list of [subject, lecturer, students]."""
    data = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            parts = line.split(',')
            subject = parts[0]
            lecturer = parts[1]
            student_count = int(parts[2])
            data.append([subject, lecturer, student_count])
    return data

def display_subject_details(subjects):
    """Display details about each subject."""
    for subject in subjects:
        code = subject[0]
        lecturer = subject[1]
        students = subject[2]
        print(f"{code} is taught by {lecturer} and has {students:3} students")

if __name__ == "__main__":
    main()