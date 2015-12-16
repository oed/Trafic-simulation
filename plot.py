import matplotlib.pyplot as plt
import pickle


data = []

def LoadDataFromFile():
	f = open('exit_data.data')
	data = pickle.load(f)
	f.close()
	return data

def FunctionDensity():
	data = LoadDataFromFile()
	time_interval = 10

	toPlot = [0]
	current_time_interval = 0

	for i in range(0,len(data),1):

		right_interval = False

		while not right_interval:

			if data[i] > (current_time_interval + 1)*time_interval:
				current_time_interval+=1
				toPlot.append(0)
			else:
				right_interval = True

		toPlot[current_time_interval] = toPlot[current_time_interval] + 1
	return toPlot



plt.plot(FunctionDensity())
plt.ylabel('Cars per hour')
plt.xlabel('t/hour')
plt.show()