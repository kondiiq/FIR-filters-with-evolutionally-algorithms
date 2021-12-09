import numpy as np
import random


def generation_single_solution(filter_order: int):
    single_solution = []
    for i in range(0, filter_order):
        single_solution.append(random.uniform(-1, 1))
    return single_solution


def v_omega(filter_order: int, solution):
    omega = 0
    for m in range(0, filter_order):
        o_calc = (2 * np.pi * m) / (filter_order + 1)
        omega = solution[m] * np.exp(-1j * o_calc * m)
    return omega


def fitness_function(v_omega_solution, filter_order: int, band_pass: float, band_stop: float):
    f1 = 0
    f2 = 0
    suma = 0
    for omega in range(0, filter_order):
        f1 += ((np.abs(np.abs(v_omega_solution) - 1)) - band_pass) ** 2
        f2 += (np.abs(v_omega_solution) - band_stop) ** 2
        suma += f1 + f2
    return suma


def current_w(w_max, w_min, iterations: int, current_iteration: int):
    return w_max - (current_iteration / iterations) * (w_max - w_min)


def priv_plus_one(priv_currently, u_k_plus_one):
    return priv_currently + u_k_plus_one


def u_k_plus_one(w_k, u_k, alpha_1, alpha_2, r_1, r_2, g_best, p_best, p_currently):
    return w_k * u_k + alpha_1 * r_1 * (p_best - p_currently) + alpha_2 * r_2 * (g_best - p_currently)


def generate_r():
    return random.uniform(0, 1)


def mutation(w1, pop1, pop2, pop3, pop4):
    return w1 * ((pop1 - pop2) + (pop3 - pop4)) / 2

def offspring(mutate, population):
    return population + mutate

def trial_vetor():
    pass


if __name__ == "__main__":
    filter_order = 56
    search_space = filter_order / (2 + 1)
    cycles = 400
    population_size = 150
    alpha_1 = 1.9
    alpha_2 = 1.8
    u_min = 0.01
    u_max = 1.0
    w_1 = 0.4
    CR = 0.5
    w_min = 0.4
    w_max = 0.9
    beta = 1.8
    lmbda = 1.1
    band_pass = 0.0319
    band_stop = 0.0319
    g_best = 0
    p_best = 0
    g_best_vector = 0
    p_best_vector = []
    population_vector = []
    fitness_vector = []
    omega_vector = []
    for solution in range(0, population_size):
        single_sol = generation_single_solution(filter_order)
        population_vector.append(single_sol)
        single_omega = v_omega(filter_order, single_sol)
        single_fitness = fitness_function(single_omega, filter_order, band_pass, band_stop)
        fitness_vector.append(single_fitness)
        pass
    g_best = min(fitness_vector)
    print(g_best)

    for cycle in range(0, cycles):
        r1 = generate_r()
        r2 = generate_r()
        w_k = current_w(w_max, w_min, cycles, cycle)
        u_k_plus_one(w_k, 0, alpha_1, alpha_2, r1, r2, g_best, 0, 0)

        pass
