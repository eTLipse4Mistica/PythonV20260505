from langchain_community.document_loaders import (
    WebBaseLoader,
    YoutubeLoader,
    CSVLoader,
    PyPDFLoader,
    TextLoader
)

from fake_useragent import UserAgent
import os
import streamlit as st
from time import sleep

url = 'https://www.linkedin.com/in/joeldiniz/' # Usage example
def loadSite(url):
    documents = ''
    for i in range(5):
        try:
            os.environ['USER_AGENT'] = UserAgent().random
            loader = WebBaseLoader(url, raise_for_status = True)
            documentList = loader.load()
            documents = '\n\n'.join([doc.page_content for doc in documentList])
            break
        except:
            print(f'Erro ao carregar o site {i+1}')
            sleep(3)
    if documents == '':
        st.error('Não foi possível carregar o site')
        st.stop()
    # print(documents)
    return documents

videoID = 'CVXsLyRC1bY' # Usage example
def loadYoutube(videoID):
    loader = YoutubeLoader(videoID, add_video_info = False, language = ['pt'])
    documentList = loader.load()
    documents = '\n\n'.join([doc.page_content for doc in documentList])
    # print(documents)
    return documents

filePath = 'Models/DataBase/ImoveisVendasSaoLuisMA20250305.csv' # Usage example
def loadCSV(filePath):
    loader = CSVLoader(filePath)
    documentList = loader.load()
    documents = '\n\n'.join([doc.page_content for doc in documentList])
    # print(documents)
    return documents

filePath = 'Data/RoteiroViagemEgito.pdf' # Usage example
def loadPDF(filePath):
    loader = PyPDFLoader(filePath)
    documentList = loader.load()
    documents = '\n\n'.join([doc.page_content for doc in documentList])
    # print(documents)
    return documents

filePath = 'Data/knowledge_base.txt' # Usage example
def loadTxt(filePath):
    loader = TextLoader(filePath)
    documentList = loader.load()
    documents = '\n\n'.join([doc.page_content for doc in documentList])
    # print(documents)
    return documents

# loadTxt(filePath)