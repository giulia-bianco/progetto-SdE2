import streamlit as st
import polars as pl
import altair as alt
import geopandas as gpd

url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/isoc_ci_in_h?format=TSV&compressed=true"

url_edu = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/t_educ.t_educ_outc?format=TSV&compressed=true"

st.write(""" # Utilizzo di Internet nei paesi dell'Unione Europea """)

# pulizia dei dati con polars
data = (
    pl
    .read_csv(url, separator="\t", null_values=["", ":", ": "])
    .select(
        pl.col("freq,unit,hhtyp,geo\\TIME_PERIOD")
            .str.split(",")
            .list.to_struct(fields=["freq", "unit", "hhtype", "state"])
            .alias("orig_col"),
        pl.col("*").exclude("freq,unit,hhtyp,geo\\TIME_PERIOD"))   
    .unnest("orig_col")
    .unpivot(index=["freq", "unit", "hhtype", "state"], value_name="internet_use",variable_name="year")
    .with_columns(year = pl.col("year")
        .str.replace(" ", "")
        .str.replace_all(r'\D', '')
        .str.replace_all("", "0")
        .cast(pl.Int64),
        internet_use = pl.col("internet_use")
.str.replace(" ", "")
.str.replace_all(r'\D', '')
.str.replace_all("", "0")
.cast(pl.Float64),
    )   
.pivot(on="unit", values="internet_use")
.filter(pl.col("hhtype") == "TOTAL")
)

data.drop("hhtype")
data.drop("freq")
st.write(data)

