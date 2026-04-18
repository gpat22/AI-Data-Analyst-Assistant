import json
from fastapi import FastAPI,File, UploadFile
import pandas as pd
import data_store
from LLM import interpret_query

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Data Analyst Assistant Running 🚀"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    data_store.df = pd.read_csv(file.file)

    return {
        "message": "File uploaded successfully",
        "columns": list(data_store.df.columns)
    }

@app.get("/query")
def query(q:str):
    df = data_store.df

    if df is None:
        return {"error":"No data uploaded"}

    q = q.lower()
    columns = list(df.columns)

    parsed = interpret_query(q, columns)
    print("LLM Response",parsed)
    operation = parsed.get("operation")
    column = parsed.get("column")
    print(operation)
    print(column)
    if column is None:
        return {
            "error": "Column not found in query",
            "available_columns": columns
        }

    if operation == "average":
        result = df[column].mean()

    elif operation == "max":
        result = df[column].max()

    elif operation == "min":
        result = df[column].min()

    elif operation == "sum":
        result = df[column].sum()

    elif operation == "count":
        result = df[column].count()

    else:
        return {"error": "Unknown operation"}

    return {
        "query": q,
        "interpreted": parsed,
        "result": result
    }

