import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\mario\OneDrive\Documentos\sena\santiago\16_09\usuarios_segmentados.csv")

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
sns.countplot(data=df, x="segmento_clicks", hue="suscripcion", palette="pastel")
plt.title("Usuarios por segmento de clicks")

plt.subplot(2, 2, 2)
sns.boxplot(data=df, x="suscripcion", y="compras_realizadas", palette="muted")
plt.title("Usuarios por segmento de compras")

plt.subplot(2, 2, 3)
sns.countplot(data=df, x="pais", hue="suscripcion", palette="bright")
plt.title("Usuarios por país y suscripción")
 
plt.subplot(2, 2, 4)
sns.heatmap(df.select_dtypes(include=["int64","float64"]).corr(), annot=True, cmap="coolwarm")
plt.title("Correlación entre edad y clicks")

plt.tight_layout()
plt.show()
