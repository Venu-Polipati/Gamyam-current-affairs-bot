import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_facts(current_affairs):
    
    prompt = f"""
You are a UPSC/APPSC Fact Extractor.

Extract only verifiable facts from the provided current affairs notes.

Rules:

- Use only information present in the text.
- Do not add outside knowledge.
- Do not explain.
- Do not summarize.
- Do not invent facts.
- Extract 3 to 8 facts per topic.
- Keep facts short and precise.
- Start directly with extracted facts.
- Do not ask for input.
- Do not provide examples.
- Do not explain the task.
- Output Format:
- Do not use markdown.
- Do not use ###.
- Use plain text only.
- Extract only factual statements.
- Ignore opinions, importance and conclusions.

- Extract only objective facts.

Do not extract:
- Importance
- Significance
- Exam Perspective
- Conclusions
- Key Takeaways
- Opinions

- Only extract verifiable factual statements.

- If no current affairs text is provided,
- return only:

NO_INPUT

Topic: Topic Name

Facts:
- Fact 1
- Fact 2
- Fact 3

Topic: Topic Name

Facts:
- Fact 1
- Fact 2
- Fact 3

Current Affairs:

{current_affairs}
"""
    print("Prompt Length:", len(prompt))
    print(prompt[:500])

    response = model.generate_content(prompt)

    return response.text
