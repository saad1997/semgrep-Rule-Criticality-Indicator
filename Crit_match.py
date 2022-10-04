import pandas as pd
import sys

# Arguments passed
print("\nID Provided", sys.argv[1])


High_rules = pd.read_pickle(r'C:\Users\IS Lab\Downloads\semgrep-rules-develop\High.pkl')
Medium_rules = pd.read_pickle(r'C:\Users\IS Lab\Downloads\semgrep-rules-develop\Medium.pkl')
Low_rules = pd.read_pickle(r'C:\Users\IS Lab\Downloads\semgrep-rules-develop\Low.pkl')

for ids in High_rules:
    if sys.argv[1] == ids:
        print("High")
for ids in Medium_rules:
    if sys.argv[1] == ids:
        print("Medium")
for ids in Low_rules:
    if sys.argv[1] == ids:
        print("Low")




