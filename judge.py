import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def is_upsc_relevant(news):

    prompt = f"""
You are a UPSC/APPSC current affairs expert.

Reply ONLY YES or NO.

Relevant:
- Governance
- Economy
- Science & Technology
- Environment
- International Relations
- Judiciary
- Government Schemes
- Andhra Pradesh
- Social Issues

Not Relevant:
- Celebrities
- Influencers
- Entertainment
- Sports
- Gossip
- Crime without policy significance

News:
{news}
"""

    response = model.generate_content(prompt)

    answer = response.text.strip().upper()

    return "YES" in answer