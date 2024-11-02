import google.generativeai as genai
genai.configure(api_key="AIzaSyCrS86qv4pF6mZHsTNyuVEWuyuDJU5KVyE")
model = genai.GenerativeModel('gemini-1.5-flash')
text = model.generate_content("Tell me about girl named Ananya who likes cats and dog named MI")
candidate = text.candidates[0]
content = candidate.content.parts[0].text
print(content, "Have a nice day")
