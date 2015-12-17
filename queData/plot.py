import matplotlib.pyplot as plt
import pickle


def LoadDataFromFile():
	f = open('que_datatest.data')
	data = pickle.load(f)
	f.close()
	return data

#def queDensity():
#	data = LoadDataFromFile()
#	time_interval = 10

#	toPlot = [0]
#	current_time_interval = 0

#	print data[0][0]
#	print data[6000][0]
#	print len(data[0][0])
#
#	for i in range(0,len(data),1):
#		sum = 0
#		for j in range(0,len(data[0][0]),1):
#			right_interval = False

#			while not right_interval:
#
#				if data[i][0][j] > (current_time_interval + 1)*time_interval:
#					current_time_interval+=1
#					sum = sum + 1
#				else:
#					right_interval = True
#
#			toPlot[current_time_interval] = toPlot[current_time_interval] + 1
#	return toPlot

def queSize():
	data = LoadDataFromFile()

	xData = []
	yData = []

	for i in range(0, len(data),1):
		s = 0.0
		for j in range(0, len(data[0][0]),1):
			s = s + data[i][0][j] 
		xData.append(data[i][1]/3600.0)
		yData.append(s)
	return (xData,yData)

(xData,yData) = queSize()

plt.plot(xData,yData)
plt.xlim([0.0,1.0])
plt.ylim([0.0,100])
plt.ylabel('Traffic jam size')
plt.xlabel('time/T')
plt.show()