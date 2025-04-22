import pandas as pd

csv_path = r"C:\Users\cdm1\OneDrive - University of Tasmania\Documents\tasmanian_seasons\edible\edible_plant_app\seasonal_bounty_database.csv"
json_path = csv_path.replace(".csv", ".json")

df = pd.read_csv(csv_path)
df.to_json(json_path, orient="records", indent=2)
