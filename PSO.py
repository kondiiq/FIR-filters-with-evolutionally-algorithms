import numpy as np
import random


def generate_solution(filter_order: int):
    solution = []
    for gene in range(0, filter_order):
        solution.append(random.uniform(-1, 1))
    return solution


def v_omega_n(order: int, solution):
    final = 0
    for m in range(0, order):
        omega = ((2 * np.pi * m) / (order + 1))
        final += solution[m] * np.exp(-1j * m * omega)
    return final


def fitness_function(filter_order: int, v_a_omega, band_pass, band_stop):
    fitness = 0
    first_sume = 0
    second_sume = 0
    for gene in range(0, filter_order):
        first_sume += (np.abs(np.abs(v_a_omega) - 1) - band_pass) ** 2
        second_sume += (np.abs(v_a_omega) - band_stop) ** 2
        fitness += first_sume + second_sume
    return fitness


def starting_velocities(u_min, u_max, order: int):
    velocities = []
    for iteration in range(0, order):
        velocities.append(random.uniform(u_min, u_max))
    return velocities


def w_current(w_maximum, w_minimum, current_iteration: int, number_of_iterations: int):
    return w_maximum - (current_iteration - number_of_iterations) * (w_maximum - w_minimum)


def u_ik_plus_one(w_k, u_k, alpha1, alpha2, r1, r2, pbest, pcurrent, g_best_current):
    return w_k * u_k + alpha1 * r1(pbest - pcurrent) + alpha2 * r2 * (g_best_current - pcurrent)


def pi_k_plus_one(p_current, u_k_plus_one):
    return p_current + u_k_plus_one


def new_nest(p_curr, alpha, levy, lamdba):
    return p_curr + alpha * levy(lamdba)


def r_generator():
    return random.uniform(0, 1)


if __name__ == "__main__":
    order = 41
    size = 150
    search_space = int(order / (2 + 1))
    cycles = 400
    alpha = 0.5
    alpha_one = 1.9
    alpha_two = 1.8
    band_pass = 0.6  # 6554 #7257  # aezakm
    band_stop = 0.2  #
    u_min = 0.01
    u_max = 1.00
    w_min = 0.4
    w_max = 0.9
    _lambda = 1.1
    beta = 1.8
    velocity_vec = []
    population = []
    fitness = []

    for i in range(0, size):
        solution = generate_solution(order)
        solution_omega = v_omega_n(order, solution)
        fitness_res = fitness_function(order, solution_omega, band_pass, band_stop)
        population.append(solution)
        fitness.append(fitness_res)
        print(f"Fitness {i} is {fitness_res}")

    g_best = population[fitness.index(min(fitness) - 1)]  #GLOBAL
    p_best = g_best  #LOCAL

    for iteration in range(0, cycles):
        local_fitness = 0
        r1 = r_generator()
        r2 = r_generator()
        w_k = w_current(w_max, w_min, iteration, cycles)
        u_ki = u_ik_plus_one(w_k, velocity_vec, alpha_one, alpha_two, r1, r2, p_best, population, g_best)
        pi_k_plus_one(population, u_ki)
        for solution in range(0, size):
            for gene in range(0, order):
                local_omega = v_omega_n(order, population[solution])
                fitness = fitness_function(order, local_omega, band_pass, band_stop)
        ##Update g_best and p_best
        if min(fitness) < p_best:
            p_best = min(fitness)
        if min(fitness) < g_best:
            g_best = min(fitness)