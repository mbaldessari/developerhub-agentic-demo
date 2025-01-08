from langgraph import Agent, Node
from langgraph.llms import vLLM
from vector_db import VectorDB
from guardrails import apply_guardrails

class AgentGraph:
    def __init__(self, llm_endpoint, llm_token):
        """
        Initialize the agent graph with vLLM and other components.

        Args:
            llm_endpoint (str): URL of the deployed vLLM endpoint.
            llm_token (str): Authorization token for the vLLM endpoint.
        """
        self.vector_db = VectorDB()
        self.llm = vLLM(endpoint=llm_endpoint, token=llm_token)

        # Define the nodes in the graph
        self.input_guardrails = Node(apply_guardrails)
        self.context_retrieval = Node(self.vector_db.retrieve_context)
        self.llm_node = Node(self.call_llm)
        self.output_guardrails = Node(apply_guardrails)

        # Create the agent with a defined flow
        self.agent = Agent(
            flow=[
                self.input_guardrails,
                self.context_retrieval,
                self.llm_node,
                self.output_guardrails,
            ]
        )

    def call_llm(self, query):
        """
        Use vLLM to process the query with context.

        Args:
            query (str): User query with context.

        Returns:
            str: LLM-generated response.
        """
        return self.llm.generate(query, max_tokens=500)

    def run(self, query):
        """
        Run the agent with the given query.

        Args:
            query (str): Input query from the user.

        Returns:
            str: Processed response from the agent.
        """
        return self.agent.run(query=query)