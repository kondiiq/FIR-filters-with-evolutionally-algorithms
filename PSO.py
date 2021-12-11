import numpy as np
import random
import matplotlib.pyplot as plt


def generate_solution(filter_order: int):
    solution = []
    for gene in range(0, filter_order):
        solution.append(random.uniform(-1, 1))
    return solution


def generate_velocities(v_min, v_max, order: int):
    velocities = []
    for i in range(0, order):
        velocities.append(random.uniform(v_min, v_max))
    return velocities


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


def w_current(w_maximum, w_minimum, current_iteration: int, number_of_iterations: int):
    return w_maximum - (current_iteration - number_of_iterations) * (w_maximum - w_minimum)


def u_ik_plus_one(w_k: float, u_k, alpha1, alpha2, r1, r2, p_best, p_current, g_best, size: int, order: int):
    u_k_plus_one = [[0] * order] * size
    for i in range(0, size):
        for j in range(0, order):
            u_k_plus_one[i][j] = w_k * u_k[i][j] + alpha1 * r1 * (p_best[j] - p_current[i][j]) + alpha2 * r2 * (
                    g_best[j] - p_current[i][j])
    return u_k_plus_one


def pi_k_plus_one(p_current, u_k_plus_one, size, order):
    p_current_plus_one = [[0] * order] * size
    for i in range(0, size):
        for j in range(0, order):
            p_current_plus_one[i][j] = p_current[i][j] + u_k_plus_one[i][j]
    return p_current_plus_one


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
    band_pass = 0.6
    band_stop = 0.2
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
        velocity_vec.append(generate_velocities(u_min, u_max, order))
        print(f"Fitness {i} is {fitness_res}")
    g_best_fit = min(fitness)
    g_best = population[fitness.index(min(fitness))]
    p_best = g_best
    for iteration in range(0, cycles):
        local_fitness = 0
        r1 = r_generator()
        r2 = r_generator()
        w_k = w_current(w_max, w_min, iteration, cycles)
        u_ki = u_ik_plus_one(w_k, velocity_vec, alpha_one, alpha_two, r1, r2, p_best, population, g_best, size, order)
        new_pop = pi_k_plus_one(population, u_ki, size, order)
        for solution in range(0, size):
            local_omega = v_omega_n(order, new_pop[solution])
            fitness = fitness_function(order, local_omega, band_pass, band_stop)
        p_best_fitness = min(fitness)
        p_best = new_pop.index(p_best_fitness)  # fitness.index(p_best_fitness)
        if p_best_fitness < g_best_fit:
            g_best_fit = p_best_fitness
    t = np.arange(order)
    plt.plot(t, g_best)
    plt.show()
