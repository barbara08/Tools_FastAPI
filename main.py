from fastapi import FastAPI
import uvicorn

from myfunctions import prime_number

app = FastAPI()

# http://127.0.0.1:8000/docs


@app.get("/")
def get_prime_number(number: int):
    return {
        "number": number,
        "is_prime": prime_number(number),
    }







""" devolver estructura
{
numero: 8
esprimo = true/false
}
"""

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)