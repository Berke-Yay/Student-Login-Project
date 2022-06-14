class student:
    name = ""
    surname =""
    password =0
    id =0
    email =""
    level = ""
    population = 0
    def __init__(self, name, surname, id, email, level, password):
        self.name = name
        self.surname = surname
        self.id = id
        self.email = email
        self.level = level
        self.password = password
        student.population+=1