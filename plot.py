import matplotlib.pyplot as plt


def LoadDataFromFile():
	f = open('exit_data.data')
    roads = pickle.load(f)
    f.close()
    

plt.plot([1,2,3,4])
plt.ylabel('Cars per hour')
plt.xlabel('t/hour')
plt.show()