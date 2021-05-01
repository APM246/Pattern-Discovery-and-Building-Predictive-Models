import pandas as pd
import numpy as np
import re

DATA = "mobile_price.csv"
info = np.genfromtxt(DATA, dtype = "U", delimiter = ",")
blue = list(info[1:,2])
dual_sim = list(info[1:,4])
four_g = list(info[1:,6])
three_g = list(info[1:,18])
touch_screen = list(info[1:,19])
wifi = list(info[1:,20])
price_category = list(info[1:,21])
all_att = blue + dual_sim + four_g + three_g + touch_screen + wifi + price_category


def change_attribute(data):
    new_att = []
    for i in data:
        if i in ["yes", "has", "Yes", "Has", "YES", "1"]:
            new_att.append("Yes")
        else:
            new_att.append("No")
    return(new_att)

new_blue = change_attribute(blue)
new_dual_sim = change_attribute(dual_sim)
new_four_g = change_attribute(four_g)
new_three_g = change_attribute(three_g)
new_touch_screen = change_attribute(touch_screen)
new_wifi = change_attribute(wifi)
new_price_category = change_attribute(price_category)

info[1:,2] = new_blue
info[1:,4] = new_dual_sim
info[1:,6] = new_four_g
info[1:,18] = new_three_g
info[1:,19] = new_touch_screen
info[1:,20] = new_wifi
info[1:,21] = new_price_category

infopd = pd.DataFrame(info)
infopd.to_csv("cleaned_mobile_price.csv", index = False)
