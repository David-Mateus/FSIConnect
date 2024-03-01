from sendEmail import getEmail
import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import time

st.write("Fundamentos de Sistemas de Informação")

qtd_number = st.number_input("Quantidade de pessoas no grupo", min_value=1, value=1)

# Usar st.text_area para entrada de e-mails
email_inputs = st.text_area("Insira as siglas dos e-mails separadas por espaço (ex: user1 user2)", height=100)

if st.button("Enviar E-mails"):
    email_list = [email.strip() + "@cin.ufpe.br" for email in email_inputs.split()]
    getEmail(email_list)
    st.write("Email Enviado com sucesso")
    time.sleep(0.5)
    streamlit_js_eval(js_expressions="parent.window.location.reload()")
