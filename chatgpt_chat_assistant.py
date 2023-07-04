from dotenv import load_dotenv; load_dotenv()
import openai, os; openai.api_key = os.getenv("OPENAI_API_KEY")

NL = '\n'


messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append(
    {"role": "system",
     "content": system_msg
    }
)
print("Your new assistant is ready!")


while input != "quit()":
    msg = input()
    messages.append(
        {"role": "user",
         "content": msg
        }
    )
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append(
        {"role": "assistant",
         "content": reply
        }
    )
    print(NL + reply + NL)
