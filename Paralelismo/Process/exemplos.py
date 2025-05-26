import time


def tarefa_pesada(n):
    total = 0
    for i in range(10**7):
        total += i * n
    return total


inicio = time.time()
for i in range(4):
    print(tarefa_pesada(i))
print("Tempo total (sequencial):", time.time() - inicio)
