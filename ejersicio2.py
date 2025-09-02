import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

# Cargar CSV
df = pd.read_csv("usuarios2.csv")

# Convertir edad y tiempo sesion a números, y eliminar los no válidos
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
df["tiempo sesion"] = pd.to_numeric(df["tiempo sesion"], errors="coerce")
df = df.dropna(subset=["edad", "tiempo sesion"])

# Eliminar duplicados
df = df.drop_duplicates(subset=["nombre","edad","pais","tiempo sesion","estado"])

# 🔹 Filtrar solo usuarios activos
df = df[df["estado"] == "activo"]

# Generar colores (tantos como puntos válidos)
colores = sns.color_palette("pastel", len(df))

# Graficar
plt.figure(figsize=(8,6))
plt.scatter(df["edad"], df["tiempo sesion"], c=colores, s=100)
plt.title("Tiempo de sesión por edad (solo usuarios activos)")
plt.xlabel("Edad")
plt.ylabel("Tiempo de sesión")
plt.show()
