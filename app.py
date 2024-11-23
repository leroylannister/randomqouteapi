from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random
import os

app = FastAPI()

# Load quotes from environment variable
quotes = os.environ.get('QUOTES', '').split('|')

@app.get('/quote')
def get_random_quote():
    if not quotes:
        return JSONResponse(content={"error": "No quotes available"}, status_code=404)
    return JSONResponse(content={"quote": random.choice(quotes)})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)