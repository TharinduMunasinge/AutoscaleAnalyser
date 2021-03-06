__author__ = 'ridwan'

import csv
import array
import matplotlib.pyplot as plt
import numpy as np

#workload data and reactive, proactive instance details provided via CSV

def plot(actualWorkload, reactiveScaling, proactiveScaling, workloadType):

    workloadTypes = ["CPU Usage", "Memory Consumption","Request in Flight Count"]
    f, (plotArea) = plt.subplots(1, sharex=True)
    f.suptitle("Reactive vs Proactive")

    plotArea.set_xlabel("Time (minutes)")
    plotArea.set_ylabel("VM Count / " + workloadTypes[workloadType])

    plotWorkloadGraph(actualWorkload,plotArea)
    plotVMGraph(reactiveScaling, plotArea, 'r', 1)
    plotVMGraph(proactiveScaling, plotArea, 'g', 2)
    plotArea.legend(["Workload", "Reactive", "Proactive"], loc='upper right')
    plt.show()

def plotWorkloadGraph(filename, plotArea):

    x_coordinates = array.array('d')
    y_coordinates = array.array('d')

    fileData = open(filename,"rb")
    reader = csv.reader(fileData)

    rownum = 0
    for row in reader:
        if rownum == 0:
            rownum += 1
        else:
            x_coordinates.append(float(row[0]))
            y_coordinates.append(float(row[1]))
        rownum += 1
    fileData.close()

    xdata = np.array(x_coordinates)
    ydata = np.array(y_coordinates)

    plotArea.plot(xdata, ydata, color="black")


def plotVMGraph(filename, plotArea, color, linewidth):

    x_coordinates = array.array('d')
    y_coordinates = array.array('d')

    fileData = open(filename,"rb")
    reader = csv.reader(fileData)

    rownum = 0
    for row in reader:
        if rownum == 0:
            rownum += 1
        else:
            x_coordinates.append(float(row[0]))
            y_coordinates.append(float(row[1]))
        rownum += 1
    fileData.close()

    xdata = np.array(x_coordinates)
    ydata = np.array(y_coordinates)

    plotArea.plot(xdata, ydata, color=color, linewidth=linewidth)


# 0 - CPU, 1 - Memory, 2 - RIF
plot("data/actual.csv", "data/reactive_scale.csv", "data/proactive_scale.csv",0)
