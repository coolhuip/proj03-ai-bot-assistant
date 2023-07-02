import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Give me your best dad joke!"}]
)
print(completion.choices[0].message.content)
