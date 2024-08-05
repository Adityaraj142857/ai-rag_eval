import os 
import getpass
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from metrices.factual_similarity import FactualSimilarity
from metrices.readability import Readibility
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

class Retriver():
    def reply(self,text):  
        embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key="AIzaSyBdOi80WvlmzgBYoGCUWoir3EAnJKri9pw")
        llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", temperature=0.2,google_api_key="AIzaSyBdOi80WvlmzgBYoGCUWoir3EAnJKri9pw")

        prompt_template = """
        Use the following pieces of information to answer the user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Context: {context}
        Question: {question}
        Only return the helpful answer below and nothing else.
        Helpful answer:
        """
        # Get the path of the parent directory
        parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        # Specify the relative path to the folder in the parent directory
        folder_path = os.path.join(parent_directory, "db")
        
        db3 = Chroma(persist_directory=folder_path, embedding_function=embedding)
        db3.get
        retriever = db3.as_retriever()

        PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        chain_type_kwargs={"prompt": PROMPT}
        
        qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True,chain_type_kwargs=chain_type_kwargs)
        result = qa_chain({"query": text})
        # print(result['source_documents'])
        page_contents = [docs.page_content for docs in retriever.get_relevant_documents(text)]
        # print(page_contents)
        return page_contents,result["result"]

retriver = Retriver()