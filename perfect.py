
def plot_cosinus():
    import numpy as np
    import matplotlib.pyplot as plt

    angle = np.arange(360)
    cosinus = np.cos(2 * np.pi * angle /360)

    plt.plot(angle, cosinus)
    