class info():
    def __init__(self, name, age, NationalID, StudentID, Edu):
        
        self.name = name
        self.age = age
        self.NationalID = NationalID
        self.StudentID = StudentID
        self.Edu = Edu

    def infos(self):

        general_information = {
            "name" : self.name,
            "age": self.age,
            "NationalID" : self.NationalID,
            "StudentID" : self.StudentID,
            "Edu" : self.Edu
        }

        return general_information

class courses():
    def __init__(self, math_grd, phisics_grd, history_grd, computer_science_grd):

        self.math_grd = math_grd
        self.phisics_grd = phisics_grd
        self.history_grd = history_grd
        self.computer_science_grd = computer_science_grd
    
    def infos(self):

        courses_information = {
            "math grade" : self.math_grd,
            "phisics grade" : self.phisics_grd,
            "history grade" : self.history_grd,
            "computer_science_grade" : self.computer_science_grd
        }
        return courses_information
