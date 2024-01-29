#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 12:08
# @Author  : ppj
# @File    : langchain-demo.py
# @Software: PyCharm

# Import libraries
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import transformer

# Initialize OpenAI LLM model
llm = OpenAI(temperature=0)

llm =

# Load tools that the agent can decide to use
# serpapi allows the agent to search the web
# llm-math allows the agent to use a calculator
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Initialize the LLM agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Run the LLM Agent
agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

