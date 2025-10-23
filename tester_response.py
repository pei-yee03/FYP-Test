import ollama

# Initialise the Ollama client
client = ollama.Client()

# Create a customised model
model = "tester"
# Prompt customised to test the new model
# prompt = "I want to create a function that takes in two integers, adds the two integers and returns an integer value, resulting from the addition. Write the unit tests required in Test Driven Development. Please generate a Python file that contains the unit tests for this function. Include all necessary imports and test cases. Do not include any explanations, only the code. Format your response as a code block starting with ``` and ending with ```."
prompt = "What is your role?"
            

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from tester")
print(response.thinking)