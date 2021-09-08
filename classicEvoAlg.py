import random


def create_sample():
    sample = random.random()
    return sample


def create_starting_population(number_of_sample: int):
    samples = []
    for number in range(0, number_of_sample):
        create_sample()
        samples.append(create_sample())
    print(samples)
    return samples


if __name__ == "__main__":
    numbers_of_samples = int(256)
    population = create_starting_population(numbers_of_samples)
