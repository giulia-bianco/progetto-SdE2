# Sistemi di Elaborazione 2 - Elaborato finale


## Scopo del progetto
Gli obiettivi di questo progetto sono:
1. lo sviluppo di una semplice applicazione web che permetta di visualizzare i dati relativi all'accesso ad Internet nei paesi dell'Unione Europea
2. l'analisi descrittiva dei dati per determinare l'evoluzione dell'utilizzo di Internet dal 2002 al 2024, anche in relazione al livello di istruzione della popolazione


## Metodologia

### Struttura del progetto
Il file "app.py" contiene il codice dell'applicazione streamlit, i file pyproject.toml e uv.lock sono generati dalla libreria uv. Per avviare l'applicazione è necessario eseguire il comando "uv run streamlit run app.py".

### librerie utilizzate
- polars, per la pulizia dei dati
- streamlit, per la generazione dell'applicazione web
- altair, per la visualizzazione dei dati
- geopandas, per la gestione delle mappe

### Fonte dei dati
I dati analizzati provengono da un dataset pubblicato da Eurostat, l'ufficio statistico dell'Unione Europea. Il dataset isoc_ci_in_h raccoglie le ossevazioni di un'indagine sull'utilizzo di Internet da parte delle famiglie svolta annualmente dagli Istituti Statistici Nazionali delle nazioni coinvolte, basandosi sul modello stabilito dall'Eurostat. Una famiglia (*household*) viene definita come un nucleo domestico in cui è presente almeno una persona di età compresa tra i 16 e i 74 anni.


## Conclusioni

