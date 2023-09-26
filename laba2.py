from fastapi import FastAPI
from pydantic import BaseModel
import pyjokes
import wikipedia

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


class Article(BaseModel):
    title: str


@app.get("/article/{title}")
def search_by_path(title: str):
    try:
        data = wikipedia.summary(title, sentences=4)
    except wikipedia.exceptions.DisambiguationError as e:
        data = e.options
    return data


@app.get("/query_search/")
def search_by_query(title: str):
    articles = wikipedia.search(title)
    data = {
        "articles": articles
    }
    return data


@app.post("/post_search/")
def search_by_body(article: Article):
    try:
        data = wikipedia.summary(article.title, sentences=4)
    except wikipedia.exceptions.DisambiguationError as e:
        data = e.options
    return data
