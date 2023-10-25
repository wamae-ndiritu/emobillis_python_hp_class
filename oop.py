class Student:
	def __init__(self, name, course, gender, age):
		self.name=name
		self.course=course
		self.gender=gender
		self.age=age
	def call(self):
		print("Name: %s \nCourse: %s \nGender: %s Age: %d" % (self.name, self.course, self.gender, self.age))

student_1 = Student("Wamae", "hp", "male", 20)
student_1.call()
