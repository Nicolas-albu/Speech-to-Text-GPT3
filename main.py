#Author Nícolas A. Ramos.

from pocketsphinx import LiveSpeech
from gpt import GPT, Example, add_example
from openai import api_key

api_key = data["API_KEY"]

#Definition of gpt
gpt_ = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

#Trainer
add_example(Example('INPUT_ONE', 'OUTPUT_ONE'))
add_example(Example('INPUT_TWO', 'OUTPUT_TWO'))
add_example(Example('INPUT_TREE', 'OUTPUT_TREE'))
add_example(Example('INPUT_FOUR', 'OUTPUT_FOUR'))
add_example(Example('INPUT_FIVE', 'OUTPUT_FIVE'))

#Capture of Speech while the gpt analyzes the instructions.
for phrase in LiveSpeech(): 
  output = gpt_.submit_request(phrase)
  output.choices[0].text
