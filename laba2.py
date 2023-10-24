from fastapi import FastAPI
from pydantic import BaseModel
import pyjokes


app = FastAPI()


class Joke(BaseModel):
    friend: str
    joke: str


class JokeInput(BaseModel):
    friend: str

@app.post("/", response_model=Joke)
def create_joke(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())


@app.get("/{friend}")
def friends_joke(friend: str):
    return friend + " tells his joke: " + pyjokes.get_joke()


@app.get("/multi/{friend}")
def multi_friends_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " "
    return result

from  fastapi import FastAPI
import pyjokes
from pydantic import BaseModel

app = FastAPI()

from  fastapi import FastAPI
import pyjokes
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def kalkulator(value1: int, value2: int, znak: str):
    if (znak == '+'):
        return value1 + value2

    if (znak == '-'):
        return value1 - value2

    if (znak == '*'):
        return value1 * value2

    if (znak == '/') and (value2 == 0):
        return 'АШИБКА'

    if (znak == '/'):
        return value1 / value2

    if (znak == '**'):
        return value1 ** value2

