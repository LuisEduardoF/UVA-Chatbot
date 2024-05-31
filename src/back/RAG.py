from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_pinecone import PineconeVectorStore

class RAG():
    def __init__(self, index_name):
        self.index_name = index_name

    def get_docsearch(self):
        embeddings = OpenAIEmbeddings()
        return PineconeVectorStore(index_name=self.index_name, embedding=embeddings)

    def _split_text(self):
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name="gpt-4",
            chunk_size=100,
            chunk_overlap=0,
        )
        return text_splitter.split_documents(self.documents)

if __name__ == "__main__":
    rag = RAG("cp3")
    query = "Give me questions about graphs"
    docs = rag.get_docsearch().similarity_search(query)
    print(docs[1])