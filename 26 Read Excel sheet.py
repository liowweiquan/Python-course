import pandas as pd
file = pd.ExcelFile("/Users/liowweiquan/Documents/Python Course /sales.xlsx")
print(file.sheet_names)
