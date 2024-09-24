import os
import google.generativeai as generativeai
from PIL import image
class geminiImg:
  def _init_(self,model_name):
    self.model_name=model_name
    self.api_key = os.getenv("AIzaSyBE7G7SSKozbQNiZ2jhAzwbwBPkp5YgX_8")

    try:
        genai.configure(api_key=self.api_key)
        self.model=genai.generativeModel(self.model_name)
    except Exception as e:
        print(f"Failed to initialize gemini model:{e}")
  def generate_response(self,input_text,input_img): 
    try:
        img = Image.open(input_img)
        response = self.model.generate_content([input_text,img],stream=True) 
        response.resolve()
        return  response.text
    except Exception as e:
        print(f"error generating response:{e}")
        return None 