import csv
import pandas as pd

rows = []
with open('cleaned_cataset.csv','r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        rows.append(row)

header = rows[0]
header[0] = "row"
planet_data = rows[1:]

masses = []
radii = []

for data in planet_data:
    masses.append(float(data[3])*1.989*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10*10)
    radii.append(float(data[4])*6.957*10*10*10*10*10*10*10*10)

gravity = []
gravity_const = 1/(6.67*10*10*10*10*10*10*10*10*10*10*10)

for i in range(len(masses)-1):
    gravity.append(gravity_const*(masses[i]/(radii[i]*radii[i])))

header.append("gravity")

for i in range(len(planet_data)-1):
    planet_data[i].append(gravity[i])

with open("completed_dataset.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(planet_data)