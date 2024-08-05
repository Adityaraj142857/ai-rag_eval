import os
from getpass import getpass
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing_extensions import Concatenate
# Load environment variables from .env file



from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

print("Libraries loaded successfully")


# Configure your embedding model and vector store
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))


pdfreader = PdfReader(os.path.join(parent_directory, "data\AI.pdf"))

# read text from pdf
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

# We need to split the text using Character Text Split such that it sshould not increse token size
seperator =[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        ""
    ]
text_splitter = RecursiveCharacterTextSplitter(
    separators = seperator,
    chunk_size = 600,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)
