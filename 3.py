# N учеников поровну делят K яблок, оставив оставшиеся яблоки в корзине. Сколько яблок получит каждый ученик?
N = 0
K = 0
while N == 0 or N > 10000:
    N = int(input())
while K == 0 or K > 10000:
    K = int(input())
print(K // N)