import google.generativeai as genai
import PIL.Image
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
img = PIL.Image.open('path/to/image.png')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(["What is in this photo?", img])
print(response.text)
