import math
from math import factorial, exp

class ErlangCalculations:
    def __init__(self):
        self.improdutividade = 1 - 0.18

    def erlang_c(self, A, N):
        N = int(N)
        L = (A**N / factorial(N)) * (N / (N - A))
        sum_ = sum((A**i) / factorial(i) for i in range(N))
        return L / (sum_ + L)

    def erlang_b(self, n, a):
        if n < 1:
            raise ValueError("O número de canais deve ser maior ou igual a 1.")
        if a < 0:
            raise ValueError("A taxa de chegada não pode ser negativa.")

        x = math.ceil(a / n)
        sum_ = sum((a ** i) / factorial(i) for i in range(x))
        return ((a ** n) / factorial(n)) / ((a ** n) / factorial(n) + sum_)

    def service_level(self, erlang_c, N, A, TME, TMA):
        return 1 - (erlang_c * exp(-((N - A) * (TME / TMA))))

    def agents(self, erlangs, SL, TME, TMA):
        N = erlangs + 1
        while True:
            A = erlangs
            erlang_c = self.erlang_c(A, N)
            if self.service_level(erlang_c, N, A, TME, TMA) < SL / 100.0:
                N += 1
            else:
                break
        return N
