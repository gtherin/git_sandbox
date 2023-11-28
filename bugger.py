
def plot_sinus():
    import numpy as np
    import matplotlib.pyplot as plt

    angle = np.arange(360)
    sinus = np.sin(2 * np.pi * angle /360)  # Corrected sinus to sin

    plt.plot(angle, sinus)
