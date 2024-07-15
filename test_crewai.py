import os
from crewai import Agent, Task, Crew, Process
from langchain.tools import tool
from dotenv import load_dotenv


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("OpenAI API key not found. Make sure you have an .env file with the key defined.")


@tool
def hello_world_tool():
    """This tool prints 'Hello World'."""
    return "Hello World"

agent = Agent(
role='Hello World Printer',
goal='Print Hello World',
backstory='An agent dedicated to printing Hello World.',
tools=[hello_world_tool],
verbose=True
)

task = Task(
description='Use the tool to print "Hello World".',
agent=agent
)

crew = Crew(
agents=[agent],
tasks=[task],
process=Process.sequential,
verbose=True
)

result = crew.kickoff()
print(result)