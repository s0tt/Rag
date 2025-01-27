from dotenv import load_dotenv
from pathlib import Path
from poem import Poem, PoemCollection
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
load_dotenv()

# Load all poems from the data folder
all_poems = PoemCollection()
for f in Path("data/").glob("story_*.txt"):
    all_poems.add(Poem.from_file(f))

prompt = """
Schreibe eine lustige Story über Max&Moritz die am Sonntag den Wecker verschlafen haben, weil ihr Hund diesen gegessen hat.
Schreibe 12 Sätze mit Pointe am Ende.
""" 

# Define your system prompt
template = """Du bist ein Gedichte Schreib Assistent der eine PROMPT vom Nutzer erhält und dazu ein Gedicht auf Schwäbisch schreibt." 
            "Mit jeder Anfrage bekommst du eine REFERENCE von bestehenden Beispielgedichten. Imitiere deren Stil und das Reimmuster."
            "Zwei aufeinander folgende Sätze sollen sich stehts wie in den Beispiel Referenzen reimen."
            "Das WICHTIGSTE: Schreibe alles in SCHWÄBISCH und beachte das REIMMUSTER."
            "PROMPT: {prompt} \n nutze den Stil der REFERENCE: {reference}"
            """
chat_template = ChatPromptTemplate.from_template(template)

generate_poem = (
    chat_template 
    | ChatOpenAI(temperature=0) 
    | StrOutputParser()
)
print(generate_poem.invoke({"prompt": prompt, "reference": str(all_poems)}))