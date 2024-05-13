from fastapi import FastAPI
import uvicorn

from myfunctions import prime_number, generate_password, decimal_to_binary

app = FastAPI()

# http://127.0.0.1:8000/docs


@app.get("/prime_number")
def get_prime_number(number: int):
    try:
        return {
            "number": number,
            "is_prime": prime_number(number),
        }
    except TypeError as e:
        return {
            "number": number,
            "error": str(e),
        }


@app.get("/generate_password")
def get_generate_password(leng: int):
    try:
        return {
            "password": generate_password(leng),
        }
    except ValueError as e:
        return {
            "error": str(e),
        }


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
