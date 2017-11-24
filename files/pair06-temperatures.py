# find the city with the
# - lowest average annual temperature, display city and temp
# - highest record temperature,        display city, temp, & date

# field separator is ':'
# [0] City:
# [1] Avg Annual Temp:
# [2] Record High Temperature :
# [3] Record Low Temperature :
# [4] Record Hottest Month / Avg Temp:
# [5] Record Coldest Month / Avg Temp:
# [6] Record Hottest Summer (Jun, Jul, Aug):
# [7] Record Coldest Winter (Dec, Jan, Feb):
# [8] Record Hottest Year / Avg Temp:
# [9] Record Coldest Year / Avg Temp

f = open("TexasTemperatures.csv")

lowestAveAnnTemp = ('city', 999)
highestRecHighTemp = ('city', 0, 'date')

for row in f:
    cityData = row.split(':')

    # get past the header row
    if cityData[0] == 'City':
        continue

    aveAnnTemp = float(cityData[1])
    if aveAnnTemp < lowestAveAnnTemp[1]:
        lowestAveAnnTemp = cityData[0], aveAnnTemp # ('city', aveAnnTemp)

    recHighTemp = cityData[2].split(',')
    recHighTemp = float(recHighTemp[0]), recHighTemp[1] # (recHighTemp, 'date')
    if recHighTemp[0] > highestRecHighTemp[1]:
        highestRecHighTemp = cityData[0], recHighTemp[0], recHighTemp[1] # ('city', recHighTemp, 'date')
        
f.close()

print()
print("The Texas city with the lowest average annual temperature is {} with an average annual temperature of {}.".
      format(lowestAveAnnTemp[0], lowestAveAnnTemp[1]))
print()
print("The Texas city with the highest record temperature is {} with a temperature of {} on {}.".
      format(highestRecHighTemp[0], highestRecHighTemp[1], highestRecHighTemp[2]))
print()
