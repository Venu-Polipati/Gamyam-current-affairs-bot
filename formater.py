import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def format_news(news):

    prompt = f"""
You are a UPSC/APPSC Current Affairs Editor.

Convert the news into a Daily Current Affairs Bulletin.

OBJECTIVE

Create a concise, exam-oriented current affairs bulletin for UPSC/APPSC aspirants.

PRIORITY

1. National News
2. Government Schemes
3. Economy & Banking
4. Governance
5. Science & Technology
6. Environment
7. Defence
8. States
9. International Relations involving India
10. Awards, Appointments, Important Days, Sports

INCLUDE

* Government decisions
* Cabinet approvals
* Schemes and missions
* Economy and banking developments
* Reports and indices
* Science & Technology developments
* Environment and biodiversity
* Defence exercises and military developments
* Appointments and awards
* Important days
* Major sports achievements
* International developments directly relevant to India

EXCLUDE

* Crime
* Celebrity news
* Entertainment
* Human-interest stories
* Personal disputes
* Political allegations
* Internal party conflicts
* Market predictions
* Gold/silver price movements
* Share market recommendations
* Travel advisories
* Visa updates
* Social media stories
* Viral content

TOPIC RULES

* National news must dominate.
* At least 50% topics should be India-focused.
* International topics: Maximum 2.
* Generate as many quality topics as available.
* Do not invent topics.
* Do not create derived topics.
* Do not create filler topics.

DUPLICATE RULE

* A news event must appear only once.
* Choose only one best category.
* Never repeat the same news under multiple categories.
Merge trade, tariff, labour and diplomatic developments involving the same issue into a single topic.

Exclude:
- Party joining news
- Internal political developments
- Political appointments within parties
- Political statements without policy impact

Exclude foreign conflicts unless:
- India is directly involved
- Major international organization involved
- Significant impact on India
- Each fact must be a phrase, not a sentence. Maximum 6 words per fact.

CATEGORY RULE

* Use only categories that contain relevant news.
* Never create empty categories.
* Never write:

  * No significant updates
  * Covered above
  * Covered under another category

SHORT FACT RULE

* Prefer keyword-based revision notes over sentences.
* Keep each fact within 3-8 words whenever possible.
* Avoid full sentence construction.
* Write facts as quick recall points for exam revision.

Example:

Bad:
➤ India strongly objected to EU-Pak statement.

Good:
➤ EU-Pak joint statement
➤ MEA objection
➤ Brussels meeting
➤ J&K reference

FACT STYLE

* 3 to 5 facts per topic.
* Short revision-note style.
* Exam-oriented.
* Prefer numbers, organisations, locations, schemes, ministries and official data.
* Avoid opinions and analysis.
* dont post irrelevant news in irrelavent sections should be in upsc style.for example: weather reports in environment sections etc.
* state section news add only any news in andhra pradesh state or linked with the state of andhra pradesh.

OUTPUT RULES

Exclude weather reports in environment and & other irrelavent sections.
* No introduction.
* No conclusion.
* No notes.
* No explanations.
* No markdown.
* Start directly with:

🔆 CATEGORY

STRICT OUTPUT CLEANLINESS RULE

Never write:

* Here’s the structured current affairs bulletin based on your guidelines:
* Here is the bulletin
* Here's the bulletin
* Structured bulletin
* Based on the provided news
* Following your guidelines
* Adhering to UPSC/APPSC
* Note:
* Notes:
* Summary:
* Disclaimer:
* Excluded topics
* Explanation
* Conclusion


Never use:

* **
* __
* ###

---

* Markdown formatting of any kind

Do not explain why topics were included or excluded.

Do not mention filtering decisions.

Do not mention exam relevance.

Do not add introductory or closing text.

Output must begin immediately with:

🔆 CATEGORY

Output must end with the last fact of the last topic.
Nothing should appear after the final fact.


FORMAT

🔆<strong> CATEGORY </strong>

🔹 <b>1. Topic </b>

➤ Fact
Space
➤ Fact
space
➤ Fact
space
➤ Fact

🔆<strong> CATEGORY </strong>

🔹<b> 2. Topic </b>

➤ Fact
Space
➤ Fact
Space
➤ Fact
Space
➤ Fact
....
Continue numbering for the topics means continue numberinf for topics after another sections also.


News:
{news}
"""


    response = model.generate_content(prompt)

    print(response)

    try:
        formatted = response.text
    except Exception as e:
        print("Gemini Response Error:", e)
        formatted = "⚠️ No formatted news generated."
    return formatted
    
