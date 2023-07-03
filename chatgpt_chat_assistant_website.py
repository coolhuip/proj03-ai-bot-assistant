import dotenv; dotenv.load_dotenv()
import openai, os; openai.api_key = os.getenv("OPENAI_API_KEY")
import gradio

NL = '\n'

messages = [
    {"role": "user",
     "content": "You are a psychologist."
    }
]

def CustomChatGPT(user_input):
    messages.append(
        {"role": "user",
         "content": user_input
        }
    )
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append(
        {"role": "assistant",
         "content": ChatGPT_reply
        }
    )
    return ChatGPT_reply

demo = gradio.Interface(fn = CustomChatGPT,
                        inputs = "text", outputs = "text",
                        title = "Digital Psychologist"
       )

demo.launch()
