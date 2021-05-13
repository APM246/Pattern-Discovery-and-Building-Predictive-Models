import pandas as pd
import numpy as np
import re

DATA = "cleaned_mobile_price.csv"
info = np.genfromtxt(DATA, dtype = "U", delimiter = ",")
primary_camera = info[1:,11]
pixel_height = info[1:,12]
screen_width = info[1:,16]

columns = info[1]

def check_zeros(columns)
    zeros = []
    for i in range(len(columns)):
        column = info[:,i]
        name = info[0,i]
        zero = 0
        for value in column:
            if value == "0":
                zero += 1
        zeros.append(name)
        zeros.append(zero)
    return(zeros)

def get_av(data):
    count = len(data)
    total = 0
    for i in range(count):
        num = float(data[i])
        total += num
    av = total/count
    return(av)

av_pc = get_av(primary_camera)
av_ph = get_av(pixel_height)
av_sw = get_av(screen_width)

def replace_zero(data, av):
    for i in range(len(data)):
        if data[i] == "0":
            data[i] = av
    return(data)

new_pc = (replace_zero(primary_camera, av_pc))
new_ph = (replace_zero(pixel_height, av_ph))
new_sw = (replace_zero(screen_width, av_sw))

info[1:,11] = new_pc
info[1:,12] = new_ph
info[1:,16] = new_sw

infopd = pd.DataFrame(info)
infopd.to_csv("cleaned_mobile_price1.csv", index = False)
