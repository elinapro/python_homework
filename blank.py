import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'Score': [85, 92, 88, 76]}

df = pd.DataFrame(data)

print(df.iloc[:2])