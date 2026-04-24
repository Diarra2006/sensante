import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Chargement
df = pd.read_csv('data/patients_dakar.csv')

fig, axes = plt.subplots(2, 2, figsize=(16, 13)) 

sns.set_theme(style="whitegrid", font_scale=1.1)

# Positionnement du titre principal tout en haut, sans toucher
fig.suptitle('Dashboard SénSanté - Analyse Complète', fontsize=24, y=0.98, weight='bold')

# --- Graphiques du cours ---
sns.countplot(ax=axes[0, 0], data=df, x='diagnostic', palette='viridis')
axes[0, 0].set_title("Répartition des Diagnostics", fontsize=16)

sns.histplot(ax=axes[0, 1], data=df, x='temperature', hue='diagnostic', kde=True)
axes[0, 1].set_title("Analyse des Températures", fontsize=16)

# --- Graphique de l'Exercice 1 ---
sns.countplot(ax=axes[1, 0], data=df, x='diagnostic', hue='sexe', palette='pastel')
axes[1, 0].set_title("Exercice 1 : Répartition par Sexe", fontsize=16)
axes[1, 0].tick_params(axis='x', rotation=45) # Rotation des labels pour ne pas qu'ils se touchent

# --- Graphique des Régions ---
top_regions = df['region'].value_counts().head(5)
sns.barplot(ax=axes[1, 1], y=top_regions.index, x=top_regions.values, palette='magma')
axes[1, 1].set_title("Top 5 Régions", fontsize=16)

plt.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.88,     wspace=0.3,   hspace=0.5 )

plt.savefig("figures/dashboard_final.png")
print("Dashboard sauvegardé proprement dans figures !")

plt.show()