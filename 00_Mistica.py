import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf
from Utils.ApiMercadoPago import GeneratePaymentLink
from streamlit.components.v1 import html

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

linkStartPayment = GeneratePaymentLink();

st.markdown(
    """
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    div.stButton > button:first-child {
        animation: pulse 2s infinite;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 30px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.05);
        transition: all 0.3s ease;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# JavaScript function to open the link
def open_page(url):
    open_script = f"""
        <script type="text/javascript">
            window.open('{url}', '_blank').focus();
        </script>
    """
    html(open_script)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    btn = st.button('💝 Apoie este Projeto - Doe R$ 7,99 💝', use_container_width=True)
    if btn:
        open_page(linkStartPayment)

# Awareness-raising text about organ donation
st.markdown(
    '<p style="text-align: center; color: red; font-weight: bold;">'
    '✨ Sua doação é fundamental para a manutenção das funcionalidades já implementadas e avançar com as a serem implementadas! ✨'
    '</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align: center; color: red;">'
    '🔗 <strong>Link alternativo para doação de valores variados:</strong> '
    '<a href="https://link.mercadopago.com.br/j3di" target="_blank" style="color: #0066cc;">link.mercadopago.com.br/j3di</a>'
    '</p>',
    unsafe_allow_html=True
)

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