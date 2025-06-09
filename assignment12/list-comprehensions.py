import pandas as pd

# 1 df
df = pd.read_csv("../csv/employees.csv")

# 2 list comprehension
full_names = [row['first_name'] + " " + row['last_name']
              for _, row in df.iterrows()]

print("All names:")
print(full_names)

# 3 "E"

names_with_e = [name for name in full_names if 'e' in name.lower()]
print(names_with_e)
