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

categories = []
for i in all_att:
    if i not in categories:
        categories.append(i)

new_blue = []
for i in blue:
    if i in ["yes", "has", "Yes", "Has", "YES", "1"]:
        new_blue.append("Yes")
    else:
        new_blue.append("No")

new_dual_sim = []
for i in dual_sim:
    if i in ["yes", "has", "Yes", "Has", "YES", "1"]:
        new_dual_sim.append("Yes")
    else:
        new_dual_sim.append("No")

new_four_g = []
for i in four_g:
    if i in ["yes", "has", "Yes", "Has", "YES", "1"]:
        new_four_g.append("Yes")
    else:
        new_four_g.append("No")

new_three_g = []
for i in three_g:
    if i in ["yes", "has", "Yes", "Has", "YES", "1"]:
        new_three_g.append("Yes")
    else:
        new_three_g.append("No")

new_touch_screen = []
for i in touch_screen:
    if i in ["yes", "has", "Yes", "Has", "YES", "1"]:
        new_touch_screen.append("Yes")
    else:
        new_touch_screen.append("No")

new_wifi = []
for i in wifi:
    if i in ["yes", "has", "Yes", "Has", "YES", "1"]:
        new_wifi.append("Yes")
    else:
        new_wifi.append("No")

new_price_category = []
for i in price_category:
    if i in ["yes", "has", "Yes", "Has", "YES", "1"]:
        new_price_category.append("Yes")
    else:
        new_price_category.append("No")

info[1:,2] = new_blue
info[1:,4] = new_dual_sim
info[1:,6] = new_four_g
info[1:,18] = new_three_g
info[1:,19] = new_touch_screen
info[1:,20] = new_wifi
info[1:,21] = new_price_category

infopd = pd.DataFrame(info)
infopd.to_csv("cleaned_mobile_price.csv", index = False)