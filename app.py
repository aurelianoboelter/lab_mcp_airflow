import streamlit as st
import pandas as pd

# Criar um DataFrame de exemplo
data = {
    'Nome': ['Nei da Silva', 'Ana Paula', 'Ricardo Duarte', 'Lucas Andrade'],
    'Idade': [45, 50, 45, 18],
    'Cidade': ['Penedo', 'Rio de Janeiro', 'São paulo', 'Recife']
}

df = pd.DataFrame(data)

# Exibir no Streamlit
st.title(" Novo modelo visualização DataFrame no Streamlit")
st.write("Aqui está o DataFrame de gerado")
st.dataframe(df)

# Mostrar estatísticas descritivas como exemplo adicional
st.write("Estatísticas descritivas:")
st.write(df.describe())
