#import gradio as gr
import os
from gradio import Interface, Textbox, run_interface

from agent_graph import AgentGraph

LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
TOKEN = os.getenv("API_KEY")

agent = AgentGraph(llm_endpoint=LLM_ENDPOINT, llm_token=TOKEN)

def run_agent(query):
    response = agent.run(query)
    return response

# def create_ui():
#     with gr.Blocks() as ui:
#         gr.Markdown("# Agentic Workflow UI")
#         with gr.Row():
#             query = gr.Textbox(label="Enter your query")
#             response = gr.Textbox(label="Response", interactive=False)
#         submit_button = gr.Button("Submit")
#         submit_button.click(run_agent, inputs=[query], outputs=[response])
#     return ui


def create_ui():
    ui = Interface(fn=run_agent, inputs=Textbox(lines=2, label="Enter your query"),
                   outputs=Textbox(label="Response", value="Your response here", interactive=False),
                   submit_btn = "Send")
    return run_interface(ui)