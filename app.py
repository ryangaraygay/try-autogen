import os
import autogen
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

llm_config = { "model": "gpt-4", "api_key": os.getenv("OPENAI_API_KEY")}

assistant = AssistantAgent("assistant1", llm_config=llm_config)

user_proxy = UserProxyAgent(
    "userproxy1", 
    human_input_mode="NEVER", 
    llm_config=False,
    code_execution_config={
        "executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="output")
    })

user_proxy.initiate_chat(
    assistant,
    message='''
        Generate a word cloud PNG image based on the contents of this URL:
        https://ryangaraygay.com/describe-design-decide-develop-a-framework-for-building-things/
        Exclude common words like "the", "and", "is", etc.
        Remove all html tags, css, js, and words that are less than 4 characters long.
        Save the image as "dddd-wordcloud.png".
    '''
)