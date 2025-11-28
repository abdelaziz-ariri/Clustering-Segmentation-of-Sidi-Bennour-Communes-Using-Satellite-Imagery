import streamlit as st
import pandas as pd

# Titre du dashboard
st.set_page_config(page_title="Dashboard Communes Sidi Bennour", layout="wide")
st.title("Segmentation et Population des Communes de Sidi Bennour")

# Charger le fichier CSV
file_path = "communes_population.csv"
df = pd.read_csv(file_path)

# Sidebar - filtres interactifs
st.sidebar.header("Filtres")
richesse_filter = st.sidebar.multiselect(
    "Sélectionner le niveau de richesse:",
    options=df['Richesse'].unique(),
    default=df['Richesse'].unique()
)

# Appliquer les filtres
filtered_df = df[df['Richesse'].isin(richesse_filter)]

# Affichage dynamique du DataFrame
st.subheader("Tableau des Communes")
st.dataframe(filtered_df.style.format({"Population totale": "{:,}"}))  # avec formatage des nombres

# Statistiques rapides
st.subheader("Statistiques générales")
col1, col2 = st.columns(2)
col1.metric("Nombre de communes", len(filtered_df))
col2.metric("Population totale filtrée", f"{filtered_df['Population totale'].sum():,}")

# Graphiques
st.subheader("Répartition par Richesse")
import plotly.express as px

fig = px.bar(
    filtered_df,
    x='Commune',
    y='Population totale',
    color='Richesse',
    title="Population par commune",
    labels={'Population totale': 'Population', 'Commune': 'Commune'}
)
st.plotly_chart(fig, use_container_width=True)

# Carte (optionnel si tu as les coordonnées)
# st.map(filtered_df)  # Si le df contient colonnes latitude/longitude
