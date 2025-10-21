import ollama

# Initialise the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "gemma3:1b"
prompt = "What is LLM?"

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from Gemma3")
print(response.response)