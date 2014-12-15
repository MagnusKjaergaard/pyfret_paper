import matplotlib.pyplot as plt
import matplotlib

# matplotlib customizations
matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 
font = {'family' : 'sans',
        'weight' : 'normal',
        'size'   : 18}

matplotlib.rc('font', **font)

x = [4, 6, 8, 10, 12]

y_FRET = [0.7369800934, 0.6160983862, 0.4184228271, 0.2619622344, 0.1889785295]
y_ALEX = [0.8124350285, 0.6727875414, 0.3939731598, 0.2109953799, 0.1261025875]

plt.scatter(x, y_FRET, s=80)
plt.xlim(2, 14)
plt.ylim(0, 1)
plt.xlabel("Dye-Dye Distance / bp")
plt.ylabel("Proximity Ratio")
plt.savefig("FRET_curve.pdf")
plt.show()
plt.cla()


plt.scatter(x, y_ALEX, s=80)
plt.xlim(2, 14)
plt.ylim(0, 1)
plt.xlabel("Dye-Dye Distance / bp")
plt.ylabel("Proximity Ratio")
plt.savefig("ALEX_curve.pdf")
plt.show()
plt.cla()