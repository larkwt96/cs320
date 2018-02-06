#!/usr/bin/env python3

import random as rnd

"""
Let A and B be sets with equal cardinality

def. match - element a of A mapped to an element b of B
def. unstable match
* a prefers not b in B over b
and
* b prefers prefers a over its pair
"""
class matcher():
    def __init__(self, n=10):
        self.n = n
        self.genA()
        self.genB()
        self.matching = matcher._gen_pref_list() # initial match

    def is_unstable(self, a):
        b = self.matching(a)
        for o in self.A(a):
            if o == b:
                return False
            else:
                if TODO

    def is_unstable(self):
        for i in range(self.n):
            if self.is_unstable(i):
                return False
        return True

    def genA(self):
        self.A = [matcher._gen_pref_list(self.n) for _ in range(self.n)]

    def genB(self):
        self.B = [matcher._gen_pref_list(self.n) for _ in range(self.n)]

    def _gen_pref_list(n):
        return matcher._permute(list(range(n)))
        
    def _permute(s):
        return [matcher._permute_helper(s) for _ in range(len(s))]

    def _permute_helper(s):
        return s.pop(rnd.randrange(0, len(s)))

    def __str__(self):
        return '{}\n{}'.format(self.A,self.B)

if __name__ == '__main__':
    m = matcher(2)
    print(m)
