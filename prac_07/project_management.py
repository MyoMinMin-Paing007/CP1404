from project import Project

FILENAME = "projects.txt"

def main():
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
    print(menu)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'd':
            display_projects(projects)
        choice = input(">>> ").lower()

def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)  # Skip header
        for line in file:
            name, start_date, priority, cost, percent = line.strip().split("\t")
            projects.append(Project(name, start_date, priority, cost, percent))
    return projects

def display_projects(projects):
    print("Incomplete projects:")
    for p in sorted([p for p in projects if not p.is_complete()]):
        print(f"  {p}")
    print("Completed projects:")
    for p in sorted([p for p in projects if p.is_complete()]):
        print(f"  {p}")

if __name__ == '__main__':
    main()
