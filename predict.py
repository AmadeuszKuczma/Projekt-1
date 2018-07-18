import numpy as np
from scipy import signal as sgl
import copy as cp
import warnings
import sys

import soundfile as sf
warnings.filterwarnings("ignore")

def predict():
    try:
        gender = highestPickSearch(sys.argv[1])

        # gender = highestPickSearch("test/081_K.wav")
        if gender == 1:
            print("Mezczyzna")
        else:
            print("Kobieta")
    except:
        print("exception")
        return

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

def checkGender(result):
    file = open("learnedValues.txt", "r")
    avgForMales = int(file.readline())
    avgForFemales = int(file.readline())
    if (sum(result[avgForMales:avgForMales+30]) > (sum(result[avgForFemales:avgForFemales+60]))):
        return 1
    else:
        return 0

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

    return checkGender(result)

predict()
