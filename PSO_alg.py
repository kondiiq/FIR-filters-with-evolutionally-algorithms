import numpy as np


def transfer_func(size: int, population):
    vz = 0

    for m in range(0, population):
        vz += population[m] * 1 ** (-1)
    pass


def initialize_single_solution(size: int):
    """
    :param size: Represent order of designed filter
    :return: Random pseudo-numbers list of solution
    """

    return np.random.random_sample(size)


def omega_n(coeff_list, m):
    for n in coeff_list:
        omegan.append((2 * np.pi * n) / (m + 1))

    return omegan


def vvomega(order, omega_n, coeff_list):
    vomega = []

    for m in range(0, order):
        element = (coeff_list[m] * np.exp(- 1j * omega_n[m] * m))
        vomega.append(element)

    return vomega


def fitness_func(size: int, vomega, band_pass, band_stop):
    lst = []

    for iterate in range(0, size):
        f1 = (np.abs(np.abs(vomega[iterate]) - 1) - band_pass) ** 2
        f2 = (np.abs(np.abs(vomega[iterate]) - 1) - band_stop) ** 2
        fsum = f1 + f2
        lst.append(fsum)
    return lst


def wk(wmax: float, wmin: float, k: int, itu: int):  # rownanie 10
    return wmax - (k / itu) * (wmax - wmin)


def generate_r_1_r_2(min_val: float, max_val: float):
    return np.random.uniform(low=min_val, high=max_val, size=1)


if __name__ == "__main__":
    number_of_solution = 150
    population = []
    M = 40
    numbers_of_iterations = 400
    min_r = 0.1
    max_r = 6.17
    alpha_1 = 1.9
    alpha_2 = 1.8
    for i in range(0, number_of_solution):
        genotype = initialize_single_solution(M)
        # print(population)
        omegan = omega_n(genotype, M)
        vomeg = vvomega(M, omegan, genotype)
        this_solution = fitness_func(M, vomeg, 0.6554, 0.7257)  # wartosci zabrane z Dystrybuanta Φ(x) standardowego
        # rozkładu normalnego N (0, 1) dla 0.4 (dwa pasma 0.2) i 0.6
        population.append(this_solution)

    for i in range(0, number_of_solution):
        print(f'Population #number{i} {population[i]}\n')

    ###     START PSO ALGORITHM

    for iteration in range(0, numbers_of_iterations):
        for genes in range(0, M):
            wk(0.9, 0.4, iteration, numbers_of_iterations)
            # eq8 uk_plus_one
            # eq9 pk_plus_one
        pass
