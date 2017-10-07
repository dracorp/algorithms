#!/usr/bin/env python
"""
Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.


Write a function that takes an integer n and return all possible combinations
of its factors.Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.

Examples:
input: 1
output:
[]


input: 37
output:
[]

input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
"""


def get_factors(n):
    def factor(n, i, combi, res):
        while i * i <= n:
            if n % i == 0:
                res += combi + [i, int(n/i)],
                factor(n/i, i, combi+[i], res)
            i += 1
        return res
    return factor(n, 2, [], [])


def get_factors_iterative1(self, n):
    todo, res = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                res += combi + [i, n/i],
                todo += (n/i, i, combi+[i]),
            i += 1
    return res


def get_factors_iterative2(n):
    ans, stack, x = [], [], 2
    while True:
        if x > n / x:
            if not stack:
                return ans
            ans.append(stack + [n])
            x = stack.pop()
            n *= x
            x += 1
        elif n % x == 0:
            stack.append(x)
            n /= x
        else:
            x += 1


if __name__ == "__main__":
    print(get_factors(32))
