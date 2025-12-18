# Evolución de las Tendencias Musicales (2000–2022)

## 1. Pregunta de investigación

Este proyecto busca responder:  

> ¿Ha cambiado estructuralmente la música popular en los últimos 20 años, o solo es una percepción individual de que la música nueva es diferente?

Se analizan métricas musicales como danceability, energy, loudness (dB), tempo (BPM), valence, duration, acousticness, speechiness y liveness para evaluar cambios en el estilo y la composición de la música popular a lo largo del tiempo.

---

## 2. Fuentes de datos

- Dataset: Best Songs on Spotify from 2000-2023 (Kaggle)  
- Contiene información de canciones:
  1. Título, artista y género
  2. Año de lanzamiento
  3. Métricas musicales: danceability, energy, bpm, loudness, valence, duration, acousticness, speechiness, liveness
  4. Popularidad de cada canción  

---

## 3. Proceso de limpieza y transformación de los datos

1. **Lectura y limpieza inicial**
   - Se importan los datos usando pandas.
   - Se normalizan los nombres de columnas (minúsculas, sin espacios, con guiones bajos).

2. **Filtrado de años**
   - Se consideran solo canciones entre 2000 y 2022, dejando fuera 2023 por datos incompletos.

3. **Selección de variables**
   - Métricas de interés: danceability, energy, bpm, loudness, valence, duration, acousticness, speechiness, liveness, popularity.

4. **Agregación de datos**
   - Se calculan promedios anuales por cada variable para permitir comparaciones consistentes.

5. **Transformación a formato largo**
   - Se utiliza melt para generar un dataset en formato long (tidy):
     - Columnas: year, variable, value
     - Facilita crear gráficos de tendencias y filtrar por variable en Power BI.

6. **Exportación**
   - Se generan dos hojas en Excel:
     - yearly_summary: datos en formato largo para Power BI
     - yearly_categorias: datos agregados en formato wide

---

## 4. Decisiones de diseño del panel

1. Filtro por variable: permite seleccionar la métrica musical a visualizar.
2. Eje X: año para mostrar la evolución temporal.
3. Eje Y: valor promedio de la métrica seleccionada.
4. Formato long: unifica todas las métricas en un único gráfico interactivo.
5. Promedios de métricas: muestran tendencias generales evitando ruido de canciones individuales.

---

## 5. Resultados esperados

- Visualización de la evolución de las métricas musicales a lo largo del tiempo.
- Posibles insights:
  1. Cambios en tempo, loudness, duración, danceability, energía y valence.
  2. Identificación de tendencias estructurales en la música popular.
- Permite responder a la pregunta de investigación sobre la percepción de cambios en la música.

---

## 6. Requisitos

- Python 3.x
- Pandas
- Openpyxl

Instalación:

```bash
pip install pandas openpyxl
