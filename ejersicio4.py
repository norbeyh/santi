import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

# Cargar CSV
df = pd.read_csv("usuarios2.csv")

# Eliminar valores nulos en edad 
df = df.dropna(subset=['edad'])

df = df.drop_duplicates(subset=['nombre','edad','pais','tiempo sesion','estado'])

# Gráfico de boxplot (edad por país)
sns.boxplot(x="pais", y="edad", data=df, palette="pastel")
plt.title("Distribución de edades por país")
plt.xlabel("País")
plt.ylabel("Edad")
plt.show()