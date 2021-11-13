import random
import pandas
import matplotlib
from scipy import signal
import numpy as np


def create_sample():
    """
    Funkcja generująca pojedynczą próbkę

    Function which generating single sample
    :param
    ":return float sample
    """
    sample = np.random.random_sample()
    return sample


def create_starting_population(number_of_sample: int = 200):
    """
    Funkcja generująca zadaną populację wykorzystującą funkcje create_sample

    Function which generating population using create_sample()
    :parameter number_of_sample
    :return array of samples
    """
    samples = []

    if number_of_sample <= 0:
        raise ValueError('Array should have more than 0 samples and must not have negative numbers of index!!')

    else:
        for number in range(0, number_of_sample):
            create_sample()
            samples.append(create_sample())
    print(samples)
    return samples


def choose_best_samples():  # potrzebuje listy !!!
    """
    Funkcja sortująca wszystkie próbki oraz wyszukująca najlepsze próbki z przekazanej tablicy próbek
    Function which sort samples and finding best samples from common array
    :parameter array, number of needed samples
    :return: best n samples of array
    """
    pass


def cross_samples():
    """
    Funkcja wyszukująca najlepsze według algorytmu próbki i dodające je do nowej listy
    Function which find
    :return array of samples
    """
    choose_best_samples()


if __name__ == "__main__":
    numbers_of_samples = int(257)
    population = create_starting_population(numbers_of_samples)



