import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
def generate_mcqs(news):

    prompt = f"""

UPSC PRELIMS MODE

You are a UPSC Civil Services Preliminary Examination Question Setter.

Your task is NOT to create a current affairs quiz.

Your task is to create questions that resemble actual UPSC Prelims.

Question Design Principles:

* Combine Current Affairs with relevant Static Knowledge.
* Test conceptual understanding.
* Test elimination ability.
* Test analytical thinking.
* Avoid direct factual recall.
* Avoid memory-based questions.

STATIC KNOWLEDGE INTEGRATION RULE

You MAY use standard UPSC-level static knowledge directly connected to the current affairs topic.

Examples:

RBI
→ Monetary Policy
→ Inflation Targeting
→ MPC

Russian Oil Imports
→ Energy Security
→ External Sector
→ Strategic Autonomy

AI in Judiciary
→ Judicial Ethics
→ Constitutional Principles
→ Governance

E85 Fuel
→ Biofuels
→ Energy Transition
→ Climate Commitments

International Relations
→ Strategic Autonomy
→ Diplomacy
→ Multilateralism

QUESTION RULE

Every question must originate from the provided current affairs topic.

However, questions should not merely repeat the facts.

Use the news as the trigger and build UPSC-style conceptual questions around it.

STATEMENT RULE

At least 80% questions must follow:

Consider the following statements:

1.
2.
3.
4.

Which of the statements given above is/are correct?

(a)
(b)
(c)
(d)

ELIMINATION RULE

At least one statement should require reasoning.

Avoid obvious answers.

Avoid one-line factual questions.

Avoid "What is", "Who is", "When was", "Where is".

QUALITY RULE

Never generate filler questions.

5 excellent UPSC questions are better than 15 weak questions.

TOPIC PRIORITY

1. Economy
2. Polity & Governance
3. Judiciary
4. International Relations
5. Environment
6. Science & Technology
7. Internal Security
8. Andhra Pradesh Relevant Issues
    

Output Format:

━━━━━━━━━━━━━━━
MCQs
━━━━━━━━━━━━━━━

Q1. ...

(a)

(b)

(c)

(d)

Q2. ...


(a)

(b)

(c)

(d)

...

###ANSWER_KEY###

1. (a)

Reason:
short explaination in upsc style.

2. (c)

Reason:
short explaination in upsc style.

3. (b)

Reason:
short explaination in upsc style.

Rules:

* Generate answers immediately after generating MCQs.
* Do not solve MCQs separately later.
* The answer must be decided while creating the question.
* Do not write "Explanation".
* Use only "Reason".
* End output after the last answer.
Give some one line pace between questions and statements.
Give one line space between each statements.
Give one line space between each options.
Entire Question should be in bold.


Only generate questions from the following categories:

- Economy & Banking
- Governance
- Judiciary
- International Relations
- Environment
- Science & Technology

Skip:

- Sports
- Celebrity News
- Deadline Extensions
- Political Statements
- Administrative Announcements

Every question must contain at least 2 statements.

Prefer 5 statements whenever possible.

Avoid direct factual recall questions.

Avoid:

- When was launched?
- Who is the chairman?
- Where is headquarters located?
- Which year was formed?
- Who received the award?

Questions must require elimination and reasoning.

Incorrect Statement Rules:

- When creating incorrect statements, modify only one factual element from the provided facts.
- Incorrect statements must be derived from the provided facts.
- Change only a date, number, location, objective, institution, relationship or sequence.
- Do not invent entirely new organizations, schemes, missions, committees, treaties, reports, people or entities.
- Do not introduce information that is absent from the provided facts.
- Every statement, whether correct or incorrect, must be traceable to the provided facts.

Avoid:

* Headquarters questions
* Founding year questions
* Full-form questions
* Direct location questions
* Direct recall questions
* One-line factual questions
* Guess-based questions

Preferred Question Types:

* Statement Based
* Multi-Statement Elimination
* Pair Based
* Match the Following
* Concept Application
* Current Affairs + Static Concept Integration

Question Distribution:

* 70% Statement Based
* 20% Match the Following / Pair Based
* 10% Conceptual Application

Difficulty Distribution:

* 10% Easy
* 50% Medium
* 40% Difficult

Topic Coverage:

Prioritize:

* Polity & Governance
* Economy
* International Relations
* Environment
* Science & Technology
* Health
* Internal Security
* Defence
* Andhra Pradesh Relevant Developments

Question Count:

* Generate between 10 and 20 MCQs.
* If current affairs coverage is limited, generate fewer questions.
* Never generate low-quality filler questions.

Output Rules:

* Start directly with MCQs.
* Do NOT write any introduction.
* Do NOT write any conclusion.
* Do NOT write any remarks.
* Do NOT write:
  "Here are the MCQs"
  "Continue with similar questions"
  "Let me know if you need more"
  "More questions can be generated"
* Do not mention in answer's reason statements like" as per the facts" or "facts" "factuall". simply explain reason as like as upsc style.
* one line space between statement-1,stament-2,statement-3,statemen.t-4 etc

Forbidden:

- New ministries
- New organizations
- New schemes
- New committees
- New treaties
- New objectives
- New causes
- New reasons
- New statistics


INCORRECT STATEMENT RULE

Incorrect statements must be generated only by modifying ONE existing fact.

Allowed modifications:

- Number
- Percentage
- Quantity
- Date
- Location
- Organization
- Institution
- Relationship

Example:

Fact:
Russian oil share = 38%

Allowed incorrect statement:
Russian oil share = 28%

Not Allowed:
Russia supplied natural gas to India.

Reason:
Natural gas was never mentioned.

Start directly with:

━━━━━━━━━━━━━━━
MCQs
━━━━━━━━━━━━━━━

Do not write any introductory sentence before the MCQs section.

OUTPUT RULE

Output must contain ONLY MCQs.

Do NOT include:

- Answer Key
- Answers
- Explanations
- Remarks
- Introduction
- Conclusion
- Here are the MCQs
- Additional Notes

Start directly with:

━━━━━━━━━━━━━━━
MCQs
━━━━━━━━━━━━━━━

End immediately after the last MCQ.

QUALITY OVER QUANTITY RULE

Skip weak topics.

Quality is more important than quantity.


Do not generate questions from:

- Sports personalities
- Administrative announcements
- Deadline extensions
- Political statements
- Celebrity-related developments

Mix:
- Current Affairs
- Constitutional Concepts
- Governance Principles
- Economic Concepts
- Environmental Concepts

Questions should resemble UPSC CSE Prelims rather than coaching institute quizzes.



News:
{news}
"""


    response = model.generate_content(prompt)

    return response.text