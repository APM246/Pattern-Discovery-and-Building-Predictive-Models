import pandas as pd
import numpy as np

DATA = "data/cleaned_mobile_price.csv"
info = np.genfromtxt(DATA, dtype = "U", delimiter = ",")
primary_camera = info[1:,10]
pixel_height = info[1:,11]
screen_width = info[1:,15]

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

info[1:,10] = new_pc
info[1:,11] = new_ph
info[1:,15] = new_sw

infopd = pd.DataFrame(data=info[1:], columns=info[0, :])
infopd.to_csv("data/cleaned_mobile_price(no 0s).csv", index = False)
