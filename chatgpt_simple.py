from dotenv import load_dotenv
import openai, os

load_dotenv()

# Let's connect our Python script to an OpenAI account.
openai.api_key = os.getenv("OPENAI_API_KEY")

# Now, let's ask the "gpt-3.5-turbo" model to give us a reply to the prompt:
# < messages[0]["content"] >
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Who are your Top 5 rappers of all time?"}]
)
print(completion.choices[0].message.content)

yo = {"what": "up", "peep":"hle"}
