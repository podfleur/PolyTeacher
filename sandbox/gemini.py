import google.generativeai as genai

API_KEY = "AIzaSyB6S6xFzbAMoZa8PE3thv2govWoBU4TE8g" # To complete
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Translate this text to French: Hello, how are you?")
print(response.text)

