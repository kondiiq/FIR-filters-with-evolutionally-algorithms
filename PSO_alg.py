import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sc
import geneal as gea


def transfer_func(size:int, population):
    vz = 0

    for m in range(0, population):
        vz += population[m] * 1 ** (-1)
    pass

def initialize_single_solution(size: int):
    '''
    :param size: Represent order of designed filter
    :return: Random pseudo-numbers list of solution
    '''

    return np.random.random_sample(size)


def omega_n(coeff_list, M):
    omegaN = []

    for n in coeff_list:
        omegaN.append((2 * np.pi * n) / (M + 1))

    return omegaN

def vvomega(M, omega_n, coeff_list):
    vomega = []

    for m in range(0, M):
            element = ( coeff_list[m] * np.exp(- 1j * omega_n[m] * m))
            vomega.append(element)

    return vomega


def fitness_func(size: int, vomega, band_pass, band_stop):
    lst = []
    f1 = 0
    f2 = 0

    for iterate in range(0, size):
        f1 = ( np.abs( np.abs ( vomega[iterate]) -1) - band_pass) ** 2
        f2 = ( np.abs( np.abs( vomega[iterate])-1) - band_stop) ** 2
        fsum = f1 + f2
        lst.append(fsum)

    return lst


if __name__ == "__main__":
    number_of_solution = 150
    population = []
    M = 40
    numbers_of_iterations = 400
    for i in range(0, number_of_solution):
        genotype = initialize_single_solution(M)
    # print(population)
        omegan = omega_n(genotype, M)
        vomeg = vvomega(M, omegan, genotype)
        this_solution = fitness_func(M, vomeg, 0.6554, 0.7257) # wartosci zabrane z Dystrybuanta Φ(x) standardowego rozkładu normalnego N (0, 1) dla 0.4 (dwa pasma 0.2) i 0.6
        population.append(this_solution)


    for i in range(0, number_of_solution):
        print(f'Population #number{i} {population[i]}\n')
