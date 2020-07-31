import sqlite3

class Student():

    def __init__(self, fname, lname, slack, cohort):
        self.fname = fname
        self.lname = lname
        self.slack = slack
        self.cohort = cohort

    def __repr__(self):
        return f'Name: {self.fname} {self.lname}, Slack: {self.slack}, Cohort: {self.cohort}'

class Report():

    def __init__(self):
        self.db_path = "/Users/zanebliss/workspace/back-end/exercises/book-2/StudentExercises/student_exercises.db"

    def make_report(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            cursor = conn.cursor()

            cursor.execute("""
            select s.id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.student_cohort,
                c.cohort_name
            from Student s
            join Cohort c on s.student_cohort = c.id
            order by s.student_cohort
            """)
        
            all_students = cursor.fetchall()

            for student in all_students:
                print(student)

reports = Report()
reports.make_report()