import unittest
from models_oop import Calculator, Contacts, Grade, GradeWithName, Person

class TestCalculator(unittest.TestCase):
    def test_add(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 7
        res = instance.add()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 17)

    def test_subtract(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 7
        res = instance.subtract()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 3)

    def test_multiple(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 7
        res = instance.multiple()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 70)

    def test_divide(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 2
        res = instance.divide()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 5)

class TestContacts(unittest.TestCase):
    def test_contacts(self):
        ls = []
        c = Contacts()
        ls.append(c.set_contact('name1', 'phone1', 'email1', 'address1'))
        ls.append(c.set_contact('name2', 'phone2', 'email2', 'address2'))
        c.get_contact(ls)
        c.del_contact(ls, 'name2')
        self.assertEqual(ls[0].name, 'name1')


class TestGrade(unittest.TestCase):
    def test_sum(self):
        grade = Grade(1,2,3)
        res = grade.sum()
        self.assertEqual(res,6)

    def test_avg(self):
        grade = Grade(1,2,3)
        res = grade.avg()
        self.assertEqual(res, 2)


class TestGradeWithName(unittest.TestCase):
    def test_GradeWithName(self):
        gwn = GradeWithName()
        ls = []
        ls.append(gwn.scores(100))
        ls.append(gwn.scores(20))
        res = gwn.avg(ls)
        self.assertEqual(res, 60)

if __name__ == '__main__':
    unittest.main()