from fastapi import FastAPI
import uvicorn

from myfunctions import (
    prime_number,
    generate_password,
    decimal_to_binary,
    binary_to_decimal,
    is_palindrome
)

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


@app.get("/decimal_to_binary")
def get_decimal_to_binary(decimal: int):
    try:
        return {
            "decimal": decimal,
            "binary": decimal_to_binary(decimal),
        }
    except TypeError as e:
        return {
            "error": str(e),
        }
    except ValueError as e:
        return {
            "error": str(e),
        }


@app.get("/binary_to_decimal")
def get_binary_to_decimal(binary: int):
    try:
        return {
            "binary": binary,
            "decimal": binary_to_decimal(binary),
        }
    except ValueError as e:
        return {
            "error": str(e),
        }


@app.get("/is_ palindorme")
def get_is_palindrome(str_word: str):
    try:
        return {
            "word": str_word,
            "result": is_palindrome(str_word),
        }
    except ValueError as e:
        return {
            "error": str_word(e)
        }


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
