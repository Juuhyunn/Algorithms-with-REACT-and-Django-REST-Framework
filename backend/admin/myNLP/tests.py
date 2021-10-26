from django.test import TestCase

# Create your tests here.
if __name__ == '__main__':
    dc1 = {}
    dc2 = {}
    dc3 = {}
    ls1 = ['10', '20', '30', '40', '50']
    ls2 = [10, 20, 30, 40, 50]
    # 방법 1. range()
    for i in range(len(ls1)):
        dc1[ls1[i]] = ls2[i]
    # 방법 2. zip()
    for i, j in zip(ls1, ls2):
        dc2[i] = j
    # 방법 3. enumerate()
    for i, j in enumerate(ls1):
        dc3[j] = ls2[i]
    print(f'{"*"*20} dc1 {"*"*25}')
    print(dc1)
    print(f'{"*"*20} dc2 {"*"*25}')
    print(dc2)
    print(f'{"*"*20} dc3 {"*"*25}')
    print(dc3)
