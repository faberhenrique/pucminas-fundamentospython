from concurrent.futures import ProcessPoolExecutor
import time

def tarefa_pesada(n):
    total = 0
    for i in range(10**7):
        total += i * n
    return total

if __name__ == "__main__":
    inicio = time.time()

    with ProcessPoolExecutor() as executor:
        resultados = list(executor.map(tarefa_pesada, range(4)))

    for r in resultados:
        print(r)

    print("Tempo total (paralelo):", time.time() - inicio)