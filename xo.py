import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTune.retrieve(id="ft-AF1WoRqd3aJAHsqc9NY7iL8F")
