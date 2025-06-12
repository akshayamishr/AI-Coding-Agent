from google import genai
from google.genai import types
from pydantic import BaseModel
import json
from systemPrompt import prompt
from tools import *
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))

available_tool = {
    "write_in_file": write_in_file,
    "change_dir_and_write_code": change_dir_and_write_code,
    "run_command": run_command
}

class responseStruture(BaseModel):
    step: str
    content : str
    wait_for_user_response : bool
    tool_name : str
    tool_attribute1 : str
    tool_attribute2 : str
    code : list[str]
    model_query: str


config = types.GenerateContentConfig(
    system_instruction = prompt,
    response_mime_type="application/json",
    response_schema=responseStruture
)

messages = []



def getResponse():
    response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents = messages,
    config = config
)
    return response

def chat():

    while(True):
        userInput = input("You : ")
        messages.append(types.Content(
            role="user", 
            parts=[types.Part(text = userInput)]))

        while(True):
            response = getResponse()
            messages.append(response.candidates[0].content)
            parsed_response = json.loads(response.text)

            print('Agent : ' + parsed_response.get('content') + '\n')

            if(parsed_response.get('step') == 'analyze'):
                if(parsed_response.get('wait_for_user_response')):
                    print("     " + parsed_response.get("model_query") + "\n")
                    userResponse = input('You : ')
                    messages.append(types.Content(
                        role="user", 
                        parts=[types.Part(text = userResponse)])
                        )
                continue

            if(parsed_response.get('step') == 'plan'):
                continue

            if(parsed_response.get('step') == 'execute'):
                function = parsed_response.get("tool_name")

                if(available_tool.get(function) != False):
                    att1 = parsed_response.get("tool_attribute1")
                    att2 = parsed_response.get('tool_attribute2')
                    code = parsed_response.get("code")

                    if(len(code) > 0):
                        available_tool[function](att1,att2,code)
                    elif(att2):
                        available_tool[function](att1,att2)
                    elif(att1):
                        available_tool[function](att1)
                    
                continue

            if(parsed_response.get('step') == 'finish'):
                break         
        
chat()