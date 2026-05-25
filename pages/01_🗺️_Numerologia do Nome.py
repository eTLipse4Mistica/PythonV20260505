import streamlit as st
import webbrowser
from Utils.Utils import *
from Utils.ConstantsVariablesDictionaries import NegativeSequencesSimple

### Page Configuration ###
st.set_page_config(
    page_title = 'Numerologia do Nome',
    page_icon = '🗺️',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'https://www.linkedin.com/in/joeldiniz/',
        'Report a bug': 'https://www.linkedin.com/in/joeldiniz/',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.linkedin.com/in/joeldiniz/)')

### Main Page ###

st.markdown('## Numerologia do Nome')
st.write('---') # Hotline
st.markdown("""
    <div style="text-align: justify;">
    <br>
    Descubra a Numerologia do seu Nome!
    <br><br>
    Importante compreender que, para uma avaliação mais completa, é necessária a consulta a um profissional da Numerologia!
    <br>
    </div>
    """, unsafe_allow_html = True)

st.write('---') # Hotline

### App Page ###

# NOME_TESTE = "Maria José Fonseca Costa"

# Save values in session_state
if 'nameInString' not in st.session_state:
    st.session_state.nameInString = ""
if 'nameInInt' not in st.session_state:
    st.session_state.nameInInt = ""
if 'converted' not in st.session_state:
    st.session_state.converted = False
if 'nameInput' not in st.session_state:
    st.session_state.nameInput = ""
if 'numberInput' not in st.session_state:
    st.session_state.numberInput = ""

# Control variables for enabling buttons
if 'btnNameInString_enabled' not in st.session_state:
    st.session_state.btnNameInString_enabled = True  # NameInString button always enabled
if 'btnCreatePyramid_enabled' not in st.session_state:
    st.session_state.btnCreatePyramid_enabled = False  # CreatePyramid button

def onFirstInputChange():
    """ Callback executed when the first input changes """
    # Clear the number input
    st.session_state.numberInput = ""
    # Reset the button states
    st.session_state.btnCreatePyramid_enabled = False
    # st.session_state.btn3_enabled = False

nameInString = st.text_input(
    'Nome a analisar:',
    placeholder = 'Informe seu nome.',
    key = 'nameInput',
    on_change = onFirstInputChange
)

# Variável para controlar se o aviso já foi mostrado
if 'zero_warning_shown' not in st.session_state:
    st.session_state.zero_warning_shown = False

if st.button('Nome em números', disabled=not st.session_state.btnNameInString_enabled):
    
    if nameInString:
        try:
            nameInInt = ConvertsNameToInts(nameInString)
            st.session_state.nameInInt = nameInInt
            st.session_state.converted = True
            
            # Convert the list to a string and save it to numberInput
            defaultNameInInt = ''.join([str(item) for item in nameInInt])
            st.session_state.numberInput = defaultNameInInt
            
            # Verifica se existe o dígito '0' na sequência
            if '0' in defaultNameInInt or '9' in defaultNameInInt:
                st.session_state.zero_warning_shown = True
            else:
                st.session_state.zero_warning_shown = False
            
            # Enables the second button upon success
            st.session_state.btnCreatePyramid_enabled = True
            
        except Exception as e:
            st.error(f'Erro: {e}')
            st.session_state.converted = False
            st.session_state.btnCreatePyramid_enabled = False
    
nameInInt = st.text_input(
    'Sequência Numérica do Nome:',
    key = 'numberInput',
    placeholder = 'Informe a sequência numérica correspondente ao seu nome.'
)

# Exibe o aviso se necessário
if st.session_state.zero_warning_shown:
    st.markdown("---")
    st.markdown(':red[Existe caracter não tabelado na sequência numérica calculada com o nome informado!]')
    st.markdown("---")

finalPyramid = ''

if st.button('Gerar pirâmide', disabled=not st.session_state.btnCreatePyramid_enabled):
    st.markdown(nameInInt)
    
    formattedPyramid = ""
    negativeSequence = []
    
    try:
        pyramid = GeneratePyramid(nameInInt)
        
        # formattedPyramid = '<br>'.join([' '.join(map(str, seq)) for seq in pyramid])
        
        formatted_lines = []
        
        for seq in pyramid:
            seq_str = [str(num) for num in seq]
            
            # Mark the positions that are part of triples
            to_highlight = [False] * len(seq_str)
            
            # Triple searches
            i = 0
            while i <= len(seq_str) - 3:
                if seq_str[i] == seq_str[i+1] == seq_str[i+2]:
                    to_highlight[i] = to_highlight[i+1] = to_highlight[i+2] = True
                    negativeSequence.append(seq_str[i] + seq_str[i+1] + seq_str[i+2])  # Adiciona apenas o valor
                    i += 3
                else:
                    i += 1
            
            # Build the line
            line_parts = []
            for idx, digit in enumerate(seq_str):
                if to_highlight[idx]:
                    line_parts.append(f'<span style="color:red">{digit}</span>')
                else:
                    line_parts.append(digit)
            
            formatted_lines.append(' '.join(line_parts))
        
        formattedPyramid = '<br>'.join(formatted_lines)
        
        st.markdown(
            f"""
                <div style="text-align: center;">
                Pirâmide da sequência númerica do seu nome:
                <br><br>
                {formattedPyramid}
                <br>
                </div>
            """,
            unsafe_allow_html = True
        )
            
        # Check the second-to-last row of the pyramid
        if pyramid and len(pyramid) >= 2:
            # Take the penultimate list
            second2Last = pyramid[-2]
            
            # Add up the digits in the list (e.g. [7, 9] -> 16)
            second2Last_result = sum(second2Last)
            
            # Check the result
            if second2Last_result == 11:
                st.markdown("---")
                st.markdown("Sequência mestre encontrada na base da pirâmide:")
                st.markdown("11 - O Iluminado: Representa carisma, intuição elevada e a ponte entre o espiritual e o material. É frequentemente um curador ou visionário.")
                st.markdown("---")
            elif second2Last_result == 22:
                st.markdown("---")
                st.markdown("Sequência mestre encontrada na base da pirâmide:")
                st.markdown("22 - O Construtor Mestre: Simboliza a capacidade de transformar sonhos em realidade. Possui grande persistência e foco no coletivo, criando bases sólidas.")
                st.markdown("---")
            elif second2Last_result == 33:
                st.markdown("---")
                st.markdown("Sequência mestre encontrada na base da pirâmide:")
                st.markdown("33 - O Mestre Professor:** Foca no amor incondicional, ensino e elevação da humanidade, sendo considerado um dos números mais evoluídos espiritualmente.")
                st.markdown("---")
        
        # Show results
        if negativeSequence:
            # Create a list containing unique values
            negativeSequenceUnique = list(set(negativeSequence))

            st.markdown("#### Sequência Negativa Encontrada:")
            st.write(', '.join(map(str, negativeSequenceUnique)))
            
            # Descreve cada sequência negativa encontrada
            st.markdown("---")
            for sequence in negativeSequenceUnique:
                if sequence in NegativeSequencesSimple:
                    st.markdown(f'<div style="text-align: justify;">{NegativeSequencesSimple[sequence]}</div><br>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div style="text-align: justify;"><b>{sequence} - Sequência negativa não registrada!</b></div>', unsafe_allow_html=True)
            
            st.markdown("---")

            # Save to session_state if necessary
            st.session_state.negativeSequence = negativeSequence
            st.session_state.negativeSequenceUnique = negativeSequenceUnique
        
        st.markdown(
            '<p style="text-align: center; color: red; font-weight: bold;">'
            '✨ Volte ao menu principal e realize sua doação (R$ 7,99)! Sua doação é fundamental para a manutenção das funcionalidades já implementadas, e avançar com as a serem implementadas! ✨'
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

        
    except Exception as e:
        st.error(f'Erro: {e}')
