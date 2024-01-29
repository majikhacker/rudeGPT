
import openai
openai.api_key = "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"

messages = [
    {"role": "system", "content": "Sarcastic yet efficient AI assistant."},
]

while True:
    user_message = input("User: ")
    if user_message: 
        messages.append(
            {"role": "user", "content": user_message},
        )
        chat = openai.ChatCompletion.create(
            model = "gpt-4-1106-preview", messages = messages
        )

    reply = chat.choices[0].message.content
    print(f'ChatGPT: {reply}')
    messages.append({"role": "assistant", "content": reply})