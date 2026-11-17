import random
import time
import math

PI_REAL = 3.14159
R = 0.5  


def punto_aleatorio():
    """Genera un punto uniforme en el cuadrado [-0.5, 0.5] x [-0.5, 0.5]."""
    x = random.uniform(-0.5, 0.5)
    y = random.uniform(-0.5, 0.5)
    return x, y


def dentro_del_circulo(x, y, r=R):
    """Condición del enunciado: x*x + y*y < r*r"""
    return x * x + y * y < r * r



def monte_carlo_pi(n):
    dentro = 0
    for _ in range(n):
        x, y = punto_aleatorio()
        if dentro_del_circulo(x, y):
            dentro += 1
    return 4 * (dentro / n), dentro


def las_vegas_pi(k):
    dentro = 0
    total = 0
    while dentro < k:
        x, y = punto_aleatorio()
        total += 1
        if dentro_del_circulo(x, y):
            dentro += 1
    return 4 * (dentro / total), total



def comparar(valores_n, valores_k, repeticiones=5):
    print("=" * 78)
    print("MONTE CARLO (N puntos fijos)")
    print("=" * 78)
    print(f"{'N':>12} {'pi estimado':>14} {'error abs.':>12} {'tiempo (s)':>12}")
    print("-" * 78)
    for n in valores_n:
        estimaciones, tiempos = [], []
        for _ in range(repeticiones):
            t0 = time.perf_counter()
            est, _ = monte_carlo_pi(n)
            tiempos.append(time.perf_counter() - t0)
            estimaciones.append(est)
        prom_est = sum(estimaciones) / repeticiones
        prom_t = sum(tiempos) / repeticiones
        print(f"{n:>12,} {prom_est:>14.6f} {abs(PI_REAL - prom_est):>12.6f} {prom_t:>12.4f}")

    print()
    print("=" * 78)
    print("LAS VEGAS (K puntos dentro exactos, total de intentos aleatorio)")
    print("=" * 78)
    print(f"{'K':>12} {'pi estimado':>14} {'error abs.':>12} {'tiempo (s)':>12} {'intentos prom.':>16}")
    print("-" * 78)
    for k in valores_k:
        estimaciones, tiempos, intentos = [], [], []
        for _ in range(repeticiones):
            t0 = time.perf_counter()
            est, total = las_vegas_pi(k)
            tiempos.append(time.perf_counter() - t0)
            estimaciones.append(est)
            intentos.append(total)
        prom_est = sum(estimaciones) / repeticiones
        prom_t = sum(tiempos) / repeticiones
        prom_int = sum(intentos) / repeticiones
        print(f"{k:>12,} {prom_est:>14.6f} {abs(PI_REAL - prom_est):>12.6f} "
              f"{prom_t:>12.4f} {prom_int:>16,.0f}")


def mostrar_variabilidad_las_vegas(k, corridas=8):
    """Muestra que Las Vegas siempre logra K dentro, pero el tiempo/intentos varía."""
    print()
    print("=" * 78)
    print(f"VARIABILIDAD DE LAS VEGAS (K = {k:,}, {corridas} corridas)")
    print("=" * 78)
    print(f"{'corrida':>8} {'intentos':>12} {'tiempo (s)':>12} {'pi estimado':>14}")
    print("-" * 78)
    for i in range(1, corridas + 1):
        t0 = time.perf_counter()
        est, total = las_vegas_pi(k)
        t = time.perf_counter() - t0
        print(f"{i:>8} {total:>12,} {t:>12.4f} {est:>14.6f}")


if __name__ == "__main__":
    random.seed()  
    valores_n = [100, 1_000, 10_000, 100_000, 1_000_000]
    valores_k = [78, 785, 7_854, 78_540, 785_398]  

    comparar(valores_n, valores_k)
    mostrar_variabilidad_las_vegas(10_000)

    print()
    print("Esperado teórico de intentos en Las Vegas: K / (pi/4) = K * 1.2732")
    print(f"Ejemplo K=10,000 -> {10_000 * 4 / math.pi:,.0f} intentos aprox.")