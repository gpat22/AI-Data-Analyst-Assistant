def interpret_query(user_query, columns):
    q = user_query.lower()

    # 🔹 First try rule-based (fallback)
    operation = None
    if "average" in q or "mean" in q:
        operation = "average"
    elif "max" in q or "highest" in q:
        operation = "max"
    elif "min" in q or "lowest" in q:
        operation = "min"
    elif "sum" in q or "total" in q:
        operation = "sum"
    elif "count" in q:
        operation = "count"

    column = None
    for col in columns:
        if col.lower() in q:
            column = col
            break

    # 🔹 If fallback works → return immediately
    if operation and column:
        return {"operation": operation, "column": column}

    # 🔹 Else use Hugging Face
    import requests

    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
    HEADERS = {"Authorization": "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"}

    prompt = prompt = f"""
        You are an AI assistant.

        Extract ONLY:
        - operation: one of [average, max, min, sum, count]
        - column: exactly one column from this list: {columns}

        Return ONLY valid JSON.
        Do NOT explain.

        Example:
        Query: average salary
        Output: {{"operation": "average", "column": "salary"}}

        Query: {user_query}
        """

    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    output = response.json()

    try:
        text = output[0]["generated_text"].lower()
    except:
        return {"operation": None, "column": None}

    # 🔹 Parse output manually
    for op in ["average", "max", "min", "sum", "count"]:
        if op in text:
            operation = op

    for col in columns:
        if col.lower() in text:
            column = col

    return {"operation": operation, "column": column}