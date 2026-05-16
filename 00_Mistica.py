import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'eTLipse',
    page_icon = '💻',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'https://www.linkedin.com/in/joeldiniz/',
        'Report a bug': 'https://www.linkedin.com/in/joeldiniz/',
        'About': 'Site desenvolvido pela eTLipse.'
    }
)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLIPse](https://www.linkedin.com/in/joeldiniz/)')


### Main Page ###

if 'data' not in st.session_state:
    dfActual = ReturnDf('./SupportContent/DataBase/TempData.csv', separator = ';', encoder = 'utf-8')
    st.session_state['data'] = dfActual






st.markdown('## Mística - Revelenda sua hístória com seu nome!')

btn = st.button('Doação! (A ser implementado!)')
# if btn:
#     webbrowser.open_new_tab('https://www.linkedin.com/in/joeldiniz/')

st.write('---') # Hotline
st.markdown(
    '''<div style="text-align: justify;">
    <strong>Funcionalidades já implentadas:</strong><br>
    <br>
    ✓ Pirâmide invertida do seu nome<br>
    ✓ Sequência mestre em seu nome<br>
    ✓ Decodificação do seu nome em números segundo a tabela de numerologia cabalística<br>
    ✓ Sequência numéricas negativas em seu nome e seu significado<br>
    </div>'''
    , unsafe_allow_html = True)

st.write('---') # Hotline
st.markdown(
    '''<div style="text-align: justify;">
    <strong>Funcionalidades em implementação:</strong><br>
    <br>
    ✓ Destino segundo numerologia<br>
    ✓ Dívidas cármicas<br>
    ✓ Missão<br>
    ✓ Impressão<br>
    ✓ Expressão<br>
    ✓ Motivação<br>
    ✓ Motivação impressão e expressão<br>
    ✓ Energia de ambientes<br>
    </div>'''
    , unsafe_allow_html = True)