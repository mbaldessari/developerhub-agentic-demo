import os

import gradio as gr

from agent_graph import AgentGraph

LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
TOKEN = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

agent = AgentGraph(llm_endpoint=LLM_ENDPOINT, llm_token=TOKEN, model_name=MODEL_NAME)

def run_agent(query, history):
    response = agent.run(query)
    return response.content

def create_ui():
    return gr.ChatInterface(fn=run_agent)
