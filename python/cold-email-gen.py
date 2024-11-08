import google.generativeai as genai


genai.configure(api_key="your-api-key")
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_cold_email(jd_text):
    prompt = (
        f"Write a concise and professional cold email (within 150 words) to a recruiter, "
        f"based on the following job description:\n\n{jd_text}\n\n"
        f"Introduce yourself, express enthusiasm for the position, and briefly highlight relevant skills."
    )
    response = model.generate_content(prompt).candidates[0].content.parts[0].text
    if response:
        return response
    else:
        return "Unable to generate email."


jd_text = input("Paste the job description here:\n")


if jd_text:
    cold_email = generate_cold_email(jd_text)
    print("\nGenerated Cold Email:\n", cold_email)
else:
    print("Please provide a valid job description.")
