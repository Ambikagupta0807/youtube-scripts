from dotenv import load_dotenv
from google import genai
from google.genai import types
import time

from prompts import (
    TOP_10_TOPIC_GENERATION_SYSTEM_PROMPT,
    TOPIC_SELECTION_SYSTEM_PROMPT,
    YOUTUBE_SCRIPTWRITER_SYSTEM_PROMPT,
    YOUTUBE_SCRIPT_ANALYSER_SYSTEM_PROMPT,
)

load_dotenv()

client = genai.Client()
MODEL = "gemini-3.6-flash"


# Helper function: har jagah system instruction + prompt bhejne ka common tareeka
def ask_gemini(system_instruction, user_input, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=user_input,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction
                ),
            )
            return response.text
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Server busy, retrying in 10 seconds... (attempt {attempt + 1})")
                time.sleep(10)
            else:
                raise e


# Step 1: top 10 titles suggest karna
def suggest_titles(topic):
    print('Figuring out the best title options for this topic...')
    return ask_gemini(
        TOP_10_TOPIC_GENERATION_SYSTEM_PROMPT,
        f"The topic is {topic}",
    )


# Step 2: sabse best title select karna
def pick_final_topic(youtube_title_list, topic):
    print(f'Picking the best title to under {topic}...')
    return ask_gemini(
        TOPIC_SELECTION_SYSTEM_PROMPT,
        f"The youtube title list are like this {youtube_title_list}, and the topic I want to teach is {topic}",
    )


# Step 3: script generate karna
def generate_script(youtube_title, topic):
    print('Generating script...')
    return ask_gemini(
        YOUTUBE_SCRIPTWRITER_SYSTEM_PROMPT,
        f"The youtube title is {youtube_title} and topic is {topic}",
    )


# Step 4: script evaluate karna
def evaluate_script(topic, youtube_title, script):
    print('Evaluating the script...')
    return ask_gemini(
        YOUTUBE_SCRIPT_ANALYSER_SYSTEM_PROMPT,
        f"The topic is {topic}, the youtube title is {youtube_title}, and the script is: {script}",
    )


def main():
    topic = input('Enter the topic name for your next youtube video: ')

    top_10_titles = suggest_titles(topic)
    print(f"\nThe selected top 10 topics are:\n{top_10_titles}\n")

    final_youtube_title = pick_final_topic(top_10_titles, topic)
    print(f"\nThe selected topic title is: {final_youtube_title}\n")

    script = generate_script(final_youtube_title, topic)
    print(f'\nScript is ready:\n{script}')

    evaluation = evaluate_script(topic, final_youtube_title, script)
    print(f'\nEvaluation:\n{evaluation}')


if __name__ == "__main__":
    main()