import json
import boto3

# Create a client for Bedrock
bedrock = boto3.client(service_name="bedrock-runtime")

# Define the prompt
prompt = """
who is the indian prime minister in 2014"
"""

# Create the payload
payload = {
    "prompt": "[INST]" + prompt + "[/INST]",
    "max_gen_len": 512,
    "temperature": 0.2,
    "top_p": 0.9
}

body = json.dumps(payload)

# Define the model ID
model_id = "meta.llama3-70b-instruct-v1:0"

try:
    # Invoke the model
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    
    # Print the response body for debugging
    response_body = response.get("body").read()
    print(f"Response body: {response_body}")
    
    # Parse the response
    response_body = json.loads(response_body)
    response_text = response_body.get("generation", "No generation key found in the response.")
    print(response_text)

except Exception as e:
    print(f"Error: {e}")
