import pandas as pd
data = {}
from_year = 2015
to_year = 2019
final = pd.DataFrame()
for i in range(from_year, to_year+1):
    path = r"D:\Amrita\NT\Cur_Conv_Dat\Exchange_Rate_Report_" + str(i) + '.csv'
    data["year{}".format(i)] = pd.read_csv(path)
    var = 'year' + str(i)
    final = final.append(data[var], ignore_index=True)
print(final)
