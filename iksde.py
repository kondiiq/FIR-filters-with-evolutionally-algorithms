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


def w_current(w_maximum, w_minimum, current_iteration: int, number_of_iterations: int):
    return w_maximum - (current_iteration - number_of_iterations) * (w_maximum - w_minimum)


def u_ik_plus_one(w_k, u_k, alpha1, alpha2, r1, r2, pbest, pcurrent, g_best_current):
    return w_k * u_k + alpha1 * r1(pbest - pcurrent) + alpha2 * r2 * (g_best_current - pcurrent)


def pi_k_plus_one(p_current, u_k_plus_one):
    return p_current + u_k_plus_one


def new_nest(p_curr, alpha, levy, lamdba):
    return p_curr + alpha * levy(lamdba)


def levy_flight(order: int, gamma, best):
    beta = 1.5
    sigma = (gamma(1 + beta) * np.sin(np.pi * beta / 2) / (gamma(1 + beta) / 2) * beta * 2 **
             ((beta - 1) / 2) ** (1 / beta))
    for flight in range(0, order):
        s = np.squeeze(order)
        u = np.randn(len(s) * sigma)
        v = np.rand(len(s))
        step = u[flight] / np.abs(v[flight]) ** (1 / beta)
        stepsize = 0.01 * step[flight] * (s - best)
    """
    function nest=get_cuckoos(nest,best,Lb,Ub)
% Levy flights
n=size(nest,1);
% Levy exponent and coefficient
% For details, see equation (2.21), Page 16 (chapter 2) of the book
% X. S. Yang, Nature-Inspired Metaheuristic Algorithms, 2nd Edition, Luniver Press, (2010).
beta=3/2;
sigma=(gamma(1+beta)*sin(pi*beta/2)/(gamma((1+beta)/2)*beta*2^((beta-1)/2)))^(1/beta);
for j=1:n,
    s=squeeze(nest(j,:,:));


    % This is a simple way of implementing Levy flights
    % For standard random walks, use step=1;
    %% Levy flights by Mantegna's algorithm
    u=randn(size(s))*sigma;
    v=randn(size(s));
    step=u./abs(v).^(1/beta);


    % In the next equation, the difference factor (s-best) means that
    % when the solution is the best solution, it remains unchanged.
    stepsize=0.01*step.*(s-best);
    % Here the factor 0.01 comes from the fact that L/100 should the typical
    % step size of walks/flights where L is the typical lenghtscale;
    % otherwise, Levy flights may become too aggresive/efficient,
    % which makes new solutions (even) jump out side of the design domain
    % (and thus wasting evaluations).
    % Now the actual random walks or flights
    s=s+stepsize.*randn(size(s));
   % Apply simple bounds/limits
   %nest(j,:,:)=simplebounds(s,Lb,Ub);
end
    """


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
    g_best = 0
    g_best_vector =[]
    population = []
    fitness = []

    for i in range(0, size):
        solution = generate_solution(order)
        solution_omega = v_omega_n(order, solution)
        fitness_res = fitness_function(order, solution_omega, band_pass, band_stop)
        population.append(solution)
        fitness.append(fitness_res)
        print(f"Fitness {i} is {fitness_res}")


    g_best = min(fitness)
    print(f"Best value is in index: {fitness.index(g_best)}")
