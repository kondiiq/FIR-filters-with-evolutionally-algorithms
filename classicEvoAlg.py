import random

'''
Funckja generujca pojedyncza probke

Function which generating single sample
'''


def create_sample():
    sample = random.random()
    return sample


'''
Funkcja generujaca zadana populacje wykorzystujaca funkcje create_sample

Function which generating population using create_sample()
'''


def create_starting_population(number_of_sample: int = 200):
    samples = []
    for number in range(0, number_of_sample):
        create_sample()
        samples.append(create_sample())
    print(samples)
    return samples


if __name__ == "__main__":
    numbers_of_samples = int(256)
    population = create_starting_population(numbers_of_samples)



