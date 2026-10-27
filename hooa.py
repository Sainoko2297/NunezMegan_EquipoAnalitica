import pandas as pd

print("INICIANDO EXTRACCIÓN")

games_df = pd.read_csv(r"C:\Users\david\OneDrive\Desktop\STEAMDATA02\games.csv", on_bad_lines='skip')
reviews_df = pd.read_csv(r"C:\Users\david\OneDrive\Desktop\STEAMDATA02\reviews.csv", on_bad_lines='skip', low_memory=False)
tags_df = pd.read_csv(r"C:\Users\david\OneDrive\Desktop\STEAMDATA02\tags.csv", on_bad_lines='skip')
categories_df = pd.read_csv(r"C:\Users\david\OneDrive\Desktop\STEAMDATA02\categories.csv", on_bad_lines='skip')
descriptions_df = pd.read_csv(r"C:\Users\david\OneDrive\Desktop\STEAMDATA02\descriptions.csv", on_bad_lines='skip')
promotional_df = pd.read_csv(r"C:\Users\david\OneDrive\Desktop\STEAMDATA02\promotional.csv", on_bad_lines='skip')
steamspy_df = pd.read_csv(r"C:\Users\david\OneDrive\Desktop\STEAMDATA02\steamspy_insights.csv", on_bad_lines='skip')

print(f"Registros cargados {len(games_df)}")
