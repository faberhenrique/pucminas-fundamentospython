"""
Desafios do Paralelismo em Python - Exemplos Ilustrativos
Cada bloco abaixo demonstra uma das principais dificuldades encontradas ao trabalhar com concorrência ou paralelismo.
"""

import threading
import multiprocessing
import time
import queue
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# 1. Condição de Corrida (Race Condition)
contador = 0
def incrementar():
    global contador
    for _ in range(100000):
        contador += 1
        time.sleep(0)

def exemplo_race_condition():
    global contador
    contador = 0
    t1 = threading.Thread(target=incrementar)
    t2 = threading.Thread(target=incrementar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("1. Race Condition - Resultado esperado: 200000 | Resultado real:", contador)

# 2. Sincronização e Coordenação
lock = threading.Lock() # Usado para  sincronizar o acesso ao contador
def incrementar_com_lock():
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

def exemplo_sincronizacao():
    global contador
    contador = 0
    t1 = threading.Thread(target=incrementar_com_lock)
    t2 = threading.Thread(target=incrementar_com_lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("2. Com Lock - Resultado com sincronização:", contador)

# 3. Complexidade Cognitiva (erro intermitente)
def tarefa_complexa(i):
    if i == 3:
        raise ValueError("Erro proposital")
    time.sleep(1)
    print(f"Tarefa {i} concluída")

def exemplo_erro_silencioso():
    print("3. Erro silencioso em threads (sem try/except)")
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(tarefa_complexa, i) for i in range(5)]
        for f in as_completed(futures):
            try:
                f.result()
            except Exception as e:
                print(f"Erro capturado: {e}")

# 4. Divisão de Tarefas Ineficiente
def tarefa_lenta(i):
    time.sleep(2 if i == 0 else 0.1)
    print(f"Tarefa {i} concluída")

def exemplo_ineficiencia():
    print("4. Tarefa desequilibrada em pool:")
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(tarefa_lenta, range(6))

# 5. Concorrência sobre Recursos Limitados
def uso_cpu_intensivo(x):
    return sum(i * i for i in range(10**6))

def exemplo_consumo_cpu():
    print("5. Multiprocessamento com uso intenso de CPU")
    with ProcessPoolExecutor() as executor:
        resultados = executor.map(uso_cpu_intensivo, range(6))
        print("Resultados computados.")

# 6. Serialização de Objetos não suportados
def lambda_invalida():
    func = lambda x: x * x
    with ProcessPoolExecutor() as executor:
        try:
            executor.map(func, range(4))
        except Exception as e:
            print("6. Erro ao serializar função lambda:", e)

# 7. Erros silenciosos e pool quebrado
def funcao_com_erro(x):
    if x == 2:
        raise RuntimeError("Erro interno")
    return x * x

def exemplo_pool_quebrado():
    print("7. ProcessPool com erro interno:")
    try:
        with ProcessPoolExecutor() as executor:
            results = executor.map(funcao_com_erro, range(5))
            print(list(results))
    except Exception as e:
        print("Erro capturado:", e)

# 8. Dificuldade em medir ganhos reais
def tarefa_simples(n):
    return n * n

def exemplo_benchmark():
    print("8. Comparando tempo sequencial vs paralelismo")
    inicio = time.time()
    [tarefa_simples(i) for i in range(1000000)]
    print("Sequencial:", time.time() - inicio)

    inicio = time.time()
    with ProcessPoolExecutor() as executor:
        executor.map(tarefa_simples, range(1000000))
    print("Paralelo:", time.time() - inicio)

if __name__ == "__main__":
    exemplo_race_condition()
    exemplo_sincronizacao()
    exemplo_erro_silencioso()
    exemplo_ineficiencia()
    exemplo_consumo_cpu()
    lambda_invalida()
    exemplo_pool_quebrado()
    exemplo_benchmark()
