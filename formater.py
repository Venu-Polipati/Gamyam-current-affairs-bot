from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def format_news(news):

    prompt = f"""
You are a UPSC/APPSC Current Affairs Faculty.

Create high-quality UPSC/APPSC Current Affairs Notes.

Formatting Rules:

* Do NOT use #, ##, ### headings.
* Do NOT use markdown symbols like ** or *.
* Use plain text only.
* Start directly from Topic 1.
* Do NOT write any introduction.
* Do NOT write any conclusion.
* Do NOT write any notes, warnings, remarks or explanations.
* Do NOT mention excluded topics.
* Leave one blank line after every heading.
* Leave one blank line between sections.
* Use ONLY the format shown below.
* Avoid creating multiple topics from the same event.
* Merge closely related economic developments into a single topic.
* Maximum one topic per major event.
* Avoid routine cabinet formation, party meetings, political appointments and internal political developments unless they have constitutional significance.


Format:

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

* Generate between 6 and 8 topics.
* Prefer 8 topics whenever sufficient relevant news exists.
* Maximum 80 words per topic.
* Keep content concise but informative.
* Avoid one-line explanations.
* Each section should contain 2-3 meaningful points wherever relevant.
* Merge related news into a single topic.
* Avoid duplicate coverage of the same event.
* Use specific event-based titles.
* Avoid generic titles.
* Topic names should clearly reflect the actual event.
* Do not use phrases such as: "Likely prelims question" , "Useful for", "Could be asked"
* Keep Exam Perspective factual and syllabus-oriented.


Topic Selection Priority:

1. Governance & Polity
2. Economy & Banking
3. International Relations
4. Science & Technology
5. Environment & Climate
6. Health
7. Internal Security
8. Infrastructure & Development
9. Andhra Pradesh Developments
10. Important Judiciary Matters

Include:

* Government policies and schemes
* RBI, SEBI, NABARD and economic developments
* Parliament, Supreme Court and constitutional issues
* International developments affecting India
* Defence and strategic affairs
* Environment and climate developments
* ISRO, DRDO, AI, Quantum, Semiconductor and emerging technologies
* Andhra Pradesh government initiatives and major developments
* Important reports, indices, treaties and international organizations

Exclude:

* Celebrities
* Influencers
* Streamers
* YouTubers
* Entertainment news
* Social media controversies
* Viral stories
* Lifestyle content
* Crime news without governance significance
* Routine political allegations and party conflicts
* Sports news without major national significance

UPSC/APPSC Focus:

* Include important prelims facts wherever relevant.
* Mention years, organizations, headquarters, treaties, reports, indices, committees and locations when useful.
* Highlight facts likely to be asked in prelims.
* Give preference to national importance over sensational news.
* International news should be included only if it impacts India, geopolitics, economy, climate or international organizations.

Output only the final current affairs notes.

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
    formatted = response.choices[0].message.content

    formatted = formatted.replace(
        "Here are the UPSC/APPSC Current Affairs Notes based on the provided news:\n\n",
        ""
    )
    return response.choices[0].message.content
    
