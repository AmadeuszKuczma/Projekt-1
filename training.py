import os
import numpy as np
from scipy import signal as sgl
import copy as cp
import math
import warnings

import soundfile as sf

warnings.filterwarnings("ignore")


def findHighestMale(result):
    result = result[:300]
    maxSum = 0
    newLearnValue = 0
    for i in range(80,270):
        localSum = sum(result[i:i+30])
        if localSum > maxSum:
            maxSum = localSum
            newLearnValue = i
    return newLearnValue

def findHighestFemale(result):
    result = result[0:300]
    maxSum = 0
    newLearnValue = 0
    for i in range(160, 240):
        localSum = sum(result[i:i+60])
        if localSum > maxSum:
            maxSum = localSum
            newLearnValue = i
    return newLearnValue

def splitIntoParts(data,rate):
    numberOfParts = len(data) / rate
    partSize = int(rate)
    parts = []
    for i in range(int(numberOfParts)):
        parts.append(data[i * partSize:(i + 1) * partSize])
    return parts

def decimateAndMultiply(parts):
    decimatedParts = []
    for part in parts:
        partKaiser = part * np.kaiser(len(part), 100)
        fft_data = np.fft.fft(partKaiser)
        fft_abs = np.abs(fft_data)
        result = fft_abs
        for i in range(2, 4):
            pick = cp.copy(fft_abs)
            d = sgl.decimate(fft_abs, int(i))
            pick[:len(d)] = d
            result *= pick
        decimatedParts.append(result)
    return decimatedParts


def highestPickSearch(file):
    data, rate = sf.read(file)
    try:
        data = data[:, 0]
    except:
        pass
    parts = splitIntoParts(data,rate)
    decimatedParts = decimateAndMultiply(parts)
    result = [0] * rate
    for part in decimatedParts:
        result += part

    return result


files = os.listdir("train")
sumForMales = 0
sumForFemales = 0
numOfMales = 0
numOfFemales = 0
for file in files:
    if file.split('_')[1]=="M.wav" :
        sumForMales += findHighestMale(highestPickSearch("train/"+file))
        numOfMales += 1
    else:
        sumForFemales += findHighestMale(highestPickSearch("train/"+file))
        numOfFemales += 1
avgForMales = math.floor(sumForMales / numOfMales)
avgForFemales = math.floor(sumForFemales / numOfFemales)

f= open("learnedValues.txt","w+")
f.write(str(avgForMales) + "\n")
f.write(str(avgForFemales)+ "\n")

print("Training is done")








