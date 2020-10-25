import matplotlib.pyplot as plt
import numpy as np

def r_cos(a,b):
    # r is a random number ranged from 1 - 10
    r = np.random.randint(10)   # start,stop,step
    print(r)

    x = np.arange(float(a),float(b)*np.pi,0.1)

    y = np.cos(x)
    return r*y

def draw_graph(graph_eq):
    plt.plot(graph_eq)

    # the title of the graph
    plt.title('f(x) = r ∗ cos(x)')

    # this is x label which is in this case refer to the random values of r from 1 - 10.
    plt.xlabel('r, values from 1 - 10')  # string must be enclosed with quotes '  '

    # y label which is in this case cos(x)
    plt.ylabel('cos(x)')

    plt.legend(['sin(x)', 'cos(x)'])      # legend entries as seperate strings in a list

    plt.show()

draw_graph(r_cos(2, 10))