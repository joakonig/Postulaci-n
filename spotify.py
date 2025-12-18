# Importo librerías
import pandas as pd

# Cargo df
df = pd.read_csv("Best Songs on Spotify from 2000-2023.csv", sep=";")

# Reviso que se haya cargado correctamente
print(df.head())

# Investigo nombres de columnas
print(df.columns)

# dado que encuentro columnas cocn espacios, las renombro y las limpio
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# me quedo solo con top post año 2000 por mayor cantidad de observaciones, y menor a 2023 ya que no tiene información completa
df = df[(df["year"] >= 2000) & (df["year"] <= 2022)]

# en base a los nombres de columnas me quedo con todas las varaibles a revisar

features_to_avg = [
    "danceability",
    "energy",
    "bpm",
    "db",
    "valence",
    "duration",
    "acousticness",
    "speechiness",
    "liveness",
    "popularity"
]

# Finlamente creo dataset procesado para obtener años, promedios de varaibles de interés

df_yearly = (
    df
    .groupby("year", as_index=False)
    .agg({col: "mean" for col in features_to_avg})
)

# Incorporo modificacion para mejor vissualizacion en powerbi
df_long = df_yearly.melt(
    id_vars="year",
    value_vars=features_to_avg,
    var_name="variable",
    value_name="value"
) 

# exporto a excel
with pd.ExcelWriter("spotify_danceability.xlsx", engine="openpyxl") as writer:
    df_long.to_excel(writer, sheet_name="yearly_summary", index=False)
    df_yearly.to_excel(writer, sheet_name="yearly_categorias", index=False)
