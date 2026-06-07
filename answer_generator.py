# from openai import OpenAI
# from config import OPENROUTER_API_KEY

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=OPENROUTER_API_KEY,
# )

# def generate_answers(mcqs):

#     prompt = f"""
# You are a UPSC/APPSC faculty.

# For the given MCQs:

# 1. Identify the correct answer.
# 2. Give a short explanation (2-4 lines).
# 3. Keep explanations exam-oriented.
# 4. No introduction.
# 5. No conclusion.

# Format:

# ━━━━━━━━━━━━━━━
# ANSWER KEY & EXPLANATIONS
# ━━━━━━━━━━━━━━━

# 1. Answer: (a)

# Explanation:
# ...

# 2. Answer: (b)

# Explanation:
# ...

# MCQs:

# {mcqs}
# """

#     response = client.chat.completions.create(
#         model="deepseek/deepseek-chat",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return response.choices[0].message.content