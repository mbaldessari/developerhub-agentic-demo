from chromadb.client import ChromaClient

class VectorDB:
    def __init__(self):
        self.client = ChromaClient()

    def retrieve_context(self, query):
        results = self.client.query(query, top_k=5)
        return " ".join([res['text'] for res in results])