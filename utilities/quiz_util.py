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
        name = input("Enter the subject name\n>>> ")
        self.db.
        