from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root() -> str:
    return 'string'


@app.post('/post')
def post():
    return post_db[0]


@app.get('/dog')
def get_dogs(kind: str):
    list_dogs = []
    for i in range(len(dogs_db)):
        if kind == dogs_db.get(i).kind:
            list_dogs.append(dogs_db.get(i))
    return list_dogs


@app.post('/dog')
def create_dogs(dog: Dog) -> Dog:
    pk_ = len(dogs_db)
    for i in range(len(dogs_db)):
        if dog.pk == dogs_db.get(i).pk:
            dog.pk = pk_
    dogs_db[dog.pk] = dog
    return dog


@app.get('/dog/{pk}')
def get_dog_pk(pk: int):
    for i in range(len(dogs_db)):
        if pk == dogs_db.get(i).pk:
            return dogs_db.get(i)
    return 'Dog does not exist'


@app.patch('/dog/{pk}')
def update_dog(pk: int, dog: Dog):
    for i in range(len(dogs_db)):
        if pk == dogs_db.get(i).pk:
            dogs_db[dog.pk] = dog
            return dogs_db[dog.pk]
    return 'Dog does not exist'


@app.get('/dog/{kind}')
def get_dog_pk(kind: str):
    for i in range(len(dogs_db)):
        if kind == dogs_db.get(i).kind:
            return dogs_db.get(i)
    return 'Dog does not exist'
