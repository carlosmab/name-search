import spacy
import asyncio


nlp = spacy.load("en_core_web_sm")

async def extract_names_from_text(text: str) -> list[str]:
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    return names