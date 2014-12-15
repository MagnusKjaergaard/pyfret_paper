import matplotlib.pyplot as plt
import numpy as np
import matplotlib 
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 18}

matplotlib.rc('font', **font)

def main():
    x = np.arange(0.1, 100, 0.1)
    R0 = 50 
    y = 1.0 / (1 + (x / R0)**6)
    plt.plot(x, y)
    plt.axvline(x=50, ymin=0, ymax=0.5, ls="--", c="k")
    plt.axhline(y=0.5, xmin=0, xmax=0.5, ls="--", c="k")
    plt.ylim(0, 1.01)
    plt.xlim(0, 100)
    plt.xticks([50], ["R0"])
    plt.yticks([0.0, 0.25, 0.50, 0.75, 1.0])
    plt.xlabel("Dye-Dye Distance")
    plt.ylabel("Percentage FRET")
    plt.savefig("ForsterR0.pdf")
    plt.show()   



if __name__ == "__main__":
    main()