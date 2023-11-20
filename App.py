# Import the gradio library and rename it as 'gr'
import gradio as gr

# Import the openai library
import openai

# Set the OpenAI API key. Replace 'null' with your actual API key
openai.api_key = 'null'

# Set the base URL for the OpenAI API. In this case, it's set to a local server running on port 1234
openai.api_base = "http://localhost:1234/v1"

# Define a function that takes a prompt as input and returns a response from the OpenAI API
def chatbot(prompt):
    try:
        # Try to create a chat completion using the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the GPT-4 model
            messages=[  # The messages to send to the API
                {"role": "user", "content": prompt}  # The prompt from the user
            ],
            max_tokens=1024,  # The maximum number of tokens to generate
            n=1,  # The number of responses to generate
            stop=None,  # Don't stop generating tokens
            temperature=0.5,  # Use a temperature of 0.5
        )

        # Extract the message from the response
        message = response.choices[0].message.content.strip()
        return message
    except Exception as e:
        # If an error occurs, return an error message
        return f"An error occurred: {str(e)}"

# Create a Gradio interface for the chatbot function
iface = gr.Interface(
    fn=chatbot,  # The function to wrap
    inputs="text",  # The input type is text
    outputs="text",  # The output type is text
    title="Local OpenAI API 0.28 example",  # The title of the interface
    description="Ask anything and the OpenAI Chatbot will respond!"  # The description of the interface
)

# Launch the interface on the local network at port 7860
iface.launch(server_name="0.0.0.0", server_port=7860)
