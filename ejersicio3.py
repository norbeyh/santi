import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

# Cargar CSV
df = pd.read_csv("usuarios2.csv")

# Eliminar duplicados
df = df.drop_duplicates(subset=["nombre","edad","pais","tiempo sesion","estado"])

# Convertir edad y tiempo sesion a números, y eliminar los no válidos
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
df["tiempo sesion"] = pd.to_numeric(df["tiempo sesion"], errors="coerce")
df = df.dropna(subset=["edad", "tiempo sesion"])

# Crear experiencia base
df["experiencia"] = df["tiempo sesion"]

# Sumar +10 si el estado es activo
df["experiencias"] = df["estado"].apply(lambda x: 10 if x == "activo" else 0)

# Experiencia final
df["experienciaFinal"] = df["experiencia"] + df["experiencias"]

# Asignar nivel
df["nivel"] = df["experienciaFinal"].apply(
    lambda exp: "novato" if exp < 20 else 
                "Intermedio" if exp <= 39 else 
                "Avanzado" if exp <= 59 else 
                "Experto"
)

# Mostrar tabla final
print(df[["nombre", "edad", "tiempo sesion", "estado", "experienciaFinal", "nivel"]])