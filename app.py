import streamlit as st
import polars as pl
import altair as alt
import geopandas as gpd

url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/isoc_ci_in_h?format=TSV&compressed=true"

st.write(""" # Utilizzo di Internet nei paesi dell'Unione Europea """)

# pulizia dei dati con polars

data = pl.read_csv(url, separator="\t", null_values=["", ":", ": "])
data = data.select(pl.col("freq,unit,hhtyp,geo\\TIME_PERIOD").str.split(",").list.to_struct(fields=["freq", "unit", "hhtype", "state"]))
st.write(data)

