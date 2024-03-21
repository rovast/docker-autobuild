from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# 加载spaCy模型
nlp = spacy.load("en_core_web_sm")

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/extract/")
async def extract_entities(item: Item):
    doc = nlp(item.text)
    entities = [{"label": ent.label_, "text": ent.text} for ent in doc.ents]
    return entities
