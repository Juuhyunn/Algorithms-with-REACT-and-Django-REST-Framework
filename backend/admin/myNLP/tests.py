from collections import defaultdict

from django.test import TestCase

# Create your tests here.
from admin.myNLP.models import NaverMovie

if __name__ == '__main__':
    n = NaverMovie()
    n.model_fit()
    n.classify('')
    dc1 = {}
    dc2 = {}
    dc3 = {}
    dc4 = defaultdict(lambda: [0, 0, 0])
    ls1 = ['10', '20', '30', '40', '50']
    ls2 = [10, 20, 30, 40, 50]
    # 방법 1. range()
    # for i in range(len(ls1)):
    #     dc1[ls1[i]] = ls2[i]
    [dc1.update({ls1[i]: ls2[i]}) for i in range(len(ls1))]
    # dc1.update({ls1[i]: ls2[i] for i in range(len(ls1)) for i in range(len(ls1))})

    # 방법 2. zip()
    # for i, j in zip(ls1, ls2):
    #     dc2[i] = j
    [dc2.update({i: j}) for i, j in zip(ls1, ls2)]

    # 방법 3. enumerate()
    # for i, j in enumerate(ls1):
    #     dc3[j] = ls2[i]
    [dc3.update({j: ls2[i]}) for i, j in enumerate(ls1)]
    print(f'{"*"*20} dc1 {"*"*25}')
    print(dc1)
    print(f'{"*"*20} dc2 {"*"*25}')
    print(dc2)
    print(f'{"*"*20} dc3 {"*"*25}')
    print(dc3)
    for i, j in enumerate(ls1):
        dc4[j][2] = ls2[i]
    print(f'{"*" * 20} dc4 {"*" * 25}')
    print(dc4)
