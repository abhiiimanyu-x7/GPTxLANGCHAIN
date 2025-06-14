# Install SerpAPI before running: pip install serpapi langchain openai

import os
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

# 🔑 Set your API Keys
os.environ['SERPAPI_API_KEY'] = "your-serpapi-key"
openai_api_key = "your-openai-key"

# 📦 Load SerpAPI tool
tools = load_tools(tool_names=["serpapi"])

# 🤖 Load OpenAI LLM
llm = OpenAI(
    model='gpt-3.5-turbo-instruct',
    temperature=1,
    openai_api_key=openai_api_key
)

# ⚙️ Initialize LangChain agent with tools
agent = initialize_agent(
    llm=llm,
    tools=tools,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 💬 Run query
response = agent.run("recent news of today")
print(response)
