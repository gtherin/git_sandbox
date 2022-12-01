
def plot_sinus():
    import numpy as np
    import matplotlib.pyplot as plt

    angle = np.arange(360)
    sinus = np.sin(2 * np.pi * angle /360)

    plt.plot(angle, sinus) 
