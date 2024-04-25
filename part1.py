# Add OpenAI library
from openai import AzureOpenAI 

API_KEY = ''
ENDPOINT = ''
API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-35-turbo"

# Initialize the Azure OpenAI client
client = AzureOpenAI(
        azure_endpoint = ENDPOINT, 
        api_key=API_KEY,  
        api_version=API_VERSION #  Target version of the API, such as 2024-02-15-preview
        )

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"}
    ]
)
generated_text = response.choices[0].message.content

# Print the response
print("Response: " + generated_text + "\n")
