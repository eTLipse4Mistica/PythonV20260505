import streamlit as st
from langchain.memory import ConversationBufferMemory
import tempfile

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from Loaders import *

TiposArquivosValidos = [
    'Site', 'Youtube', 'Pdf', 'Csv', 'Txt'
]

configModels = {
    'Groq':{
        'modelos': ['llama-3.1-70b-versatile', 'gemma2-9b-it', 'mixtral-8x7b-32768'],
        'chat': ChatGroq
    },
    'OpenAI':{
        'modelos': ['gpt-4o-mini', 'gpt-4o', 'o1-preview', 'o1-mini'],
        'chat': ChatOpenAI
    }
 }

memoriaInicial = ConversationBufferMemory()

def carregaArquivo(tipoArquivo, arquivo):
    if tipoArquivo == 'Site':
        documento = carregaSite(arquivo)
    if tipoArquivo == 'Youtube':
        documento = carregaYoutube(arquivo)
    if tipoArquivo == 'Pdf':
        with tempfile.NamedTemporaryFile(suffix = '.pdf', delete = False) as temp:
            temp.write(arquivo.read())
            nomeTemp = temp.name
        documento = carregaPDF(nomeTemp)
    if tipoArquivo == 'Csv':
        with tempfile.NamedTemporaryFile(suffix = '.csv', delete = False) as temp:
            temp.write(arquivo.read())
            nomeTemp = temp.name
        documento = carregaCSV(nomeTemp)
    if tipoArquivo == 'Txt':
        with tempfile.NamedTemporaryFile(suffix = '.txt', delete = False) as temp:
            temp.write(arquivo.read())
            nomeTemp = temp.name
        documento = carregaTxt(nomeTemp)
    
    return documento

def carregaModelo(provedor, modelo, apiKey, tipoArquivo, arquivo):
    
    documento = carregaArquivo(tipoArquivo, arquivo)
    # print(documento)
    
    systemMessage = '''Você é um assistente amigável chamado Oráculo.
        Você possui acesso às seguintes informações vindas 
        de um documento {}: 

        ####
        {}
        ####

        Utilize as informações fornecidas para basear as suas respostas.

        Sempre que houver $ na sua saída, substita por S.

        Se a informação do documento for algo como "Just a moment...Enable JavaScript and cookies to continue" 
        sugira ao usuário carregar novamente o Oráculo!'''.format(tipoArquivo, documento)


    template = ChatPromptTemplate.from_messages([
        ('system', systemMessage),
        ('placeholder', '{chat_history}'),
        ('user', '{input}')
    ])
    
    chat = configModels[provedor]['chat'](model = modelo, api_key = apiKey)
    chain = template | chat
    
    st.session_state['chain'] = chain

def paginaChat():
    st.header('🤖Bem-vindo ao Oráculo', divider=True)

    chain = st.session_state.get('chain')
    if chain is None:
        st.error('Carregue o Oráculo')
        st.stop()
    
    memoria = st.session_state.get('memoria', memoriaInicial)
    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    inputUsuario = st.chat_input('Fale com o oráculo')
    
    if inputUsuario:
        chat = st.chat_message('human')
        chat.markdown(inputUsuario)
        
        chat = st.chat_message('ai')
        resposta = chat.write_stream(chain.stream({
            'input': inputUsuario, 'chat_history': memoria.buffer_as_messages
        }))
        
        memoria.chat_memory.add_user_message(inputUsuario)
        memoria.chat_memory.add_ai_message(resposta)
        st.session_state['memoria'] = memoria


def sidebar():
    tabs = st.tabs(['Upload de Arquivos', 'Seleção de Modelos'])
    with tabs[0]:
        tipoArquivo = st.selectbox('Selecione o tipo de arquivo', TiposArquivosValidos)
        if tipoArquivo == 'Site':
            arquivo = st.text_input('Digite a url do site')
        if tipoArquivo == 'Youtube':
            arquivo = st.text_input('Digite a url do vídeo')
        if tipoArquivo == 'Pdf':
            arquivo = st.file_uploader('Faça o upload do arquivo pdf', type=['.pdf'])
        if tipoArquivo == 'Csv':
            arquivo = st.file_uploader('Faça o upload do arquivo csv', type=['.csv'])
        if tipoArquivo == 'Txt':
            arquivo = st.file_uploader('Faça o upload do arquivo txt', type=['.txt'])
    with tabs[1]:
        provedor = st.selectbox('Selecione o provedor dos modelo', configModels.keys())
        modelo = st.selectbox('Selecione o modelo', configModels[provedor]['modelos'])
        apiKey = st.text_input(
            f'Adicione a api key para o provedor {provedor}',
            value=st.session_state.get(f'api_key_{provedor}'))

        st.session_state[f'api_key_{provedor}'] = apiKey
    
    if st.button('Inicializar Oráculo', use_container_width=True):
        carregaModelo(provedor, modelo, apiKey, tipoArquivo, arquivo)
        
    if st.button('Apagar Histórico de Conversa', use_container_width=True):
        st.session_state['memoria'] = memoriaInicial


def main():
    with st.sidebar:
        sidebar()
    paginaChat()


if __name__ == '__main__':
    main()