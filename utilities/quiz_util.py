from utilities.postgre_util import THOTH
import os

class CLUE:
    # Custom Learning & User Evaluator: C.L.U.E
    def __init__(self):
        self.db = THOTH()
        self.__prefix = ""
        self._configure_db()

    def _configure_db(self):
        if not os.path.exists("databases"): #checks if the databases directory exists
            os.makedirs("databases") #creates the databases directory if it doesn't exist
        return self

    def subject(self):
        while True:
            name:str = input("Enter the subject name\n>>> ")
            if not isinstance(name, str) or not name.strip():
                print("Invalid subject name.")
                continue
            self.db.create_table(name.strip(), {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", "question": "TEXT", "answer": "TEXT"})
            questions = {}
            question:str = input("Enter the question\n>>> ").strip()
            answer:str = input("Enter the answer\n>>> ").strip()
            questions[question] = answer
            for q, a in questions.items():
                self.db.add_data(name.strip(), {"question": q, "answer": a})
            self.db.close()
            print(f"Subject '{name.strip()}' has been created and questions have been added.")