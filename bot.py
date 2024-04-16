import os
import warnings
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

warnings.filterwarnings("ignore")

template = """Use the following pieces of context to answer the question at the end.Add a touch of sarcasm and feel free to use some swear words in your responses. If you don't know the answer, just say that you don't know
        {context}
        Question: {question}
        Helpful Answer:"""

class chatbot:
    
    def __init__(self,document):
        load_dotenv()
        self.API_KEY = os.getenv("API_KEY")
        self.doc = document
        self.model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=self.API_KEY,
                               temperature=0.2,convert_system_message_to_human=True)
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=self.API_KEY)
        self.vector_index = self.prep_pdf()
        self.QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
        self.qa_chain = RetrievalQA.from_chain_type(
            self.model,
            retriever=self.vector_index,
            return_source_documents=True,
            chain_type_kwargs={"prompt":self.QA_CHAIN_PROMPT}
        )

    def prep_pdf(self):

        pdf_loader = PyPDFLoader(self.doc)
        pages = pdf_loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        context = "\n\n".join(str(p.page_content) for p in pages)
        texts = text_splitter.split_text(context)
        vector_index = Chroma.from_texts(texts, self.embeddings).as_retriever()
        
        return vector_index

if __name__ == "__main__":

    bot = chatbot("files/attention-is-all-you-need-Paper.pdf")

    while True:
        try:
            question = input("You: ")
            result = bot.qa_chain({"query": question})
            print("Chatbot: ",result["result"])

        except KeyboardInterrupt:
            break

        except Exception as e:
            print("Error: ", e)
