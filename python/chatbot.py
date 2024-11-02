import google.generativeai as genai
genai.configure(api_key="AIzaSyCrS86qv4pF6mZHsTNyuVEWuyuDJU5KVyE")
model = genai.GenerativeModel('gemini-1.5-flash')

chats = []
context = " "

def generate_context(previous_context: str, user_message: str, ai_message: str):
    prompt = f"On the basis of the below context, the message from the userand the reply by the flirt artist, create a summary context of all the information that the flirt artist knows about the user in general\n Context: {previous_context}\n User: {user_message}\n Flirt: {ai_message}"
    response = model.generate_content(prompt)
    if response.candidates:
        candidate = response.candidates[0]
        content = candidate.content
        if content.parts:
            text_content = content.parts[0].text
            return text_content
        else:
            print("Error: No parts in the candidate's content.")
            return previous_context  # Return the previous context if no new content
    else:
        print("Error: No candidates in response.")
        return previous_context

def chat(context: str, user_message: str):
    prompt = f"Context: {context} Act like a professional flirt artist, the above context gives you information about what will you know about the user. On the basis of same information reply to the below conversation\n. User Message: {user_message}"
    response = model.generate_content(prompt)
    if response.candidates:
        candidate = response.candidates[0]
        content = candidate.content
        if content.parts:
            text_content = content.parts[0].text
            return text_content
        else:
            print("Error: No parts in the candidate's content.")
            return "I'm sorry, I didn't quite get that."
    else:
        print("Error: No candidates in response.")
        return "I'm sorry, I didn't quite get that."

while True:
    user_message = input("User :")
    ai_reply = chat(context, user_message)
    print(ai_reply)
    context = generate_context(context, user_message, ai_reply)