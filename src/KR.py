class MasterStudent(Student):
    def __init__(self, name: str, gpa: float, year: int, thesis_topic: str, supervisor: str):
        super().__init__(name, gpa, year)
        self.thesis_topic = thesis_topic
        self.supervisor = supervisor

    def __str__(self):
        return f"{self._name}, курс {self._year}, GPA: {self._gpa}, тема диплома: {self.thesis_topic}"

    def get_status(self):
        return f"Магистрант: {self._name}, тема: {self.thesis_topic}"



























------------------------
    class Student:
    def __init__(self, name: str, gpa: float, year: int):
        if not name:
            raise ValueError("Имя не может быть пустым")
        if not (0.0 <= gpa <= 5.0):
            raise ValueError("GPA должен быть от 0 до 5")
        self._name = name
        self._gpa = gpa
        self._year = year


    @property
    def name(self): return self._name

    @property
    def gpa(self): return self._gpa

    def __str__(self):
        return f"{self._name}, курс {self._year}, GPA: {self._gpa}"


# Ваш код:
class MasterStudent(Student):
    pass
