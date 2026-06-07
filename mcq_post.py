import asyncio
from telegram_sender import send_message
from fact_extractor import extract_facts
from mcq_generator import generate_mcqs

filename = "current_affairs.txt"

with open(
    filename,
    "r",
    encoding="utf-8"
) as f:
    current_affairs = f.read()

facts = extract_facts(current_affairs)

print("FACTS READY")

mcq_output = generate_mcqs(facts)

if "###ANSWER_KEY###" in mcq_output:

    questions, answers = mcq_output.split(
        "###ANSWER_KEY###",
        1
    )

    with open(
        "daily_mcqs.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(questions)

    with open(
        "daily_answers.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(answers)

    # Telegram lo MCQs post cheyyi
    asyncio.run(
        send_message(questions)
    )

    print("MCQs Saved")
    print("Answers Saved")
    print("MCQs Posted")

else:

    with open(
        "daily_mcqs.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(mcq_output)

    asyncio.run(
        send_message(mcq_output)
    )

    print("Answer Key section not found")

print("=" * 50)
print(mcq_output)
print("=" * 50)
