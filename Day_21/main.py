
class Person:
      def __init__(self, firstname, lastname, age, country, city, gender):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.gender =gender
          self.skills = []
      def per_info(self):
            return f'{self.firstname} {self.lastname} is {self.age} years of age. {self.gender} lives in {self.city} city of {self.country}'
class Students(Person):
      def __init__(self, firstname='Abubakr', lastname='Abdullah', age=20, country='Nigeria', city='Ilorin', gender='male'):
           self.gender = gender 
           super().__init__(firstname, lastname, age, country, city,gender)
      def student_infor(self):
           gender = 'He' if self.gender == 'male' else "She"
           return f'{self.firstname} {self.lastname} is {self.age} years of age. {gender} lives in {self.city} city of {self.country}'
      def add_skill(self, skill):
           self.skills.append(skill)
           
pers = Person('Moridiyyah', 'Bello', 25, 'Nigeria', 'Ibadan', 'He')
print(pers.per_info()) 

stud = Students('Mutiat', 'Katibi', 27, 'Nigeria', 'Lagos', 'female')
print(stud.student_infor())

# pers.add_skill('PYTHON')

# print(pers.per_info())
# pers.add_skill('HTML')
# print(pers.skills)