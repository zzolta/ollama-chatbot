import ollama

MODEL = "gemma4:e2b"
client = ollama.Client(host="http://localhost:11434")

print("Chatbot ready! Type 'quit' to exit.")
print("Enter temperature (0.0 - 1.0) or press Enter to use default [0.7]: ", end="")
temp_input = input().strip()

if temp_input == "":
    temperature = 0.7
else:
    try:
        temperature = float(temp_input)
        temperature = max(0.0, min(1.0, temperature))
    except ValueError:
        print("Invalid input, defaulting to 0.7.")
        temperature = 0.7

if temperature == 0:
    print("Warning: temperature 0 means greedy decoding — responses will be maximally consistent but may feel repetitive.")
elif temperature == 0.5:
    print("Good average, but less creative than default.")
elif temperature == 1:
    print("Warning: temperature 1 uses the raw probability distribution — responses may be more varied or unpredictable.")

print(f"Using temperature: {temperature}\n")

messages = []

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("quit", "exit", "q"):
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat(model=MODEL, messages=messages, options={"temperature": temperature})
    reply = response.message.content

    messages.append({"role": "assistant", "content": reply})
    print(f"Bot: {reply}\n")
