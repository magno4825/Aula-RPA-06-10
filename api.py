import streamlit as st
from dotenv import load_dotenv
import os
import requests 
from datetime import datetime



load_dotenv()

VALIDAR_API_CNPJ_CPF_TOKEN = os.getenv('VALIDAR_CNPJ_CPF_TOKEN')

st.title('Consulta de CNPJ')

with st.form('consulta-cnpj'):
    cnpj = st.text_input('CNPJ', max_chars=14, placeholder='20441978000104')
    consultar = st.form_submit_button('Consultar')

    if consultar:
        # url = f'https://api.invertexto.com/v1/validator?token={VALIDAR_API_CNPJ_CPF_TOKEN}&value={cnpj}&type=cnpj'
        url = f'https://api.invertexto.com/v1/validator'
        parametros = {
            'token': VALIDAR_API_CNPJ_CPF_TOKEN,
            'value': cnpj,
            'type': 'cnpj'
        }
        
        req = requests.get(url, params=parametros)
        if req.status_code == 200:
            if req.json()['valid']:
                req = requests.get(f'https://publica.cnpj.ws/cnpj/{cnpj}').json()
                st.write(req)
            else:
                st.write('CNPJ INEXISYENTE')
        else:
            st.write(req.status_code)

