from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def format_news(news):

    prompt = f"""
You are a UPSC Current Affairs Faculty.

Create concise UPSC-style current affairs notes.

Formatting Rules:

- Do NOT use ###, ##, # headings.
- Do NOT use markdown symbols like ** or *.
- Use plain text only.
- Leave one blank line after every heading.
- Leave one blank line between each section.
- Use ONLY the emojis shown below.
- Do not add introductions.
- Do not add explanations before the first topic.
- Start directly with Topic 1.


Format exactly like this:

━━━━━━━━━━━━━━━
<b>1️⃣ Topic Name</b>
━━━━━━━━━━━━━━━

<b>📰 Why in News?</b>

Content

<b>📚 Background</b>

Content

<b>🎯 Importance</b>

Content

<b>📝 Exam Perspective</b>

Content

<b>🔑 Key Takeaway</b>

Content


Content Rules:

- Maximum 80 words per topic.
- No conclusion.
- No suggested reading.
- No extra commentary.
- Keep it exam-oriented.
- Use simple and clear language.
Selection Rules:

- Include only UPSC/APPSC relevant topics.
- Prioritize Indian national affairs, governance, economy, science & technology, environment, judiciary and Andhra Pradesh developments.
- Include international news only if it affects India, global geopolitics, economy, climate or international organizations.
- Ignore celebrities, influencers, YouTubers, streamers, entertainment, gossip, viral news and social media controversies.
- Ignore crime news unless it has legal, constitutional, governance or policy significance.
- Ignore sports news unless it has major national significance.
- If a topic is not relevant for UPSC/APPSC, do not include it in the final notes.
- Include important prelims facts such as countries, organizations, reports, treaties, years, locations, institutions, indices and committees wherever relevant.
- Highlight important facts likely to be asked in UPSC Prelims.
- Create separate sections for each topic.
- Each section should contain 2-3 informative points wherever relevant.
- Include important dates, organizations, locations, reports and treaties wherever applicable.
- Avoid one-line answers.
- Exclude topics related to influencers, streamers, content creators, celebrities and social media personalities.
- Exclude entertainment and pop-culture news.
- Maintain concise but informative UPSC-style notes.
- Merge similar news into a single topic.
- Avoid duplicate topics covering the same event.
- Group related developments under one heading.
- Give priority to Indian national affairs, governance, economy, science & technology, environment and important state developments.
- International news should be included only if it has significant impact on India, global geopolitics, economy or UPSC relevance.
News:
{news}
"""


    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content