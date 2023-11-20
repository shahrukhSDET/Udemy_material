class Student:
    def __init__(self):(self, name, height, test_score):
        self.name = name
        self.height = height
        self._test_score = test_score  # protected attribute

    def get_test_score(self):
        return self._test_score

student1 = Student("Alice", 20, 95)

print(f'student : {student1.name}, height : {student1.height}')
print(f"student test score is : {student1.get_test_score()}")