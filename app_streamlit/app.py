import streamlit as st
import joblib
import pandas as pd

st.title('2A BANK')
# st.image("2A bank.png", caption="2A BANK")
col1, col2, col3 = st.columns(3)

with col1:
    score_credit = st.number_input('CreditScore')
    Gender = st.radio('Gender', ['Homme', 'Femme'])
    anciennete = st.number_input('Ancienneté', 0)
    salaireestimer = st.number_input('salaireestimer')


with col2:
    age = st.number_input('Age', 1, 100)
    pays = st.selectbox('Geography', ['France', 'Germany', 'Spain'])
    solde = st.number_input('Solde du compte ($)', 0.0)

with col3:
    credit_carte = st.radio('Carte de crédit', ['oui', 'non'])
    membre_active = st.selectbox('Client actif', ['Oui', 'Non'])
    produit_nombre = st.number_input('NumOfProducts', 0, 10)

# Traitement des données d'entrée avec les 13 colonnes attendues
data = pd.DataFrame([{
    'CreditScore': score_credit,
    'Age': age,
    'Tenure': anciennete,
    'Balance': solde,
    'NumOfProducts': produit_nombre,
    'HasCrCard': 1 if credit_carte == 'oui' else 0,
    'IsActiveMember': 1 if membre_active == 'Oui' else 0,
    'Geography_France': int(pays == 'France'),
    'Geography_Germany': int(pays == 'Germany'),
    'Geography_Spain': int(pays == 'Spain'),
    'Gender_Female': int(Gender == 'Femme'),
    'Gender_Male': int(Gender == 'Homme')
}])

# Chargement du modèle
model = joblib.load("app_streamlit\\ch.joblib")

if st.button("Prédire la fidélité"):
    st.write("Traitement en cours...")
    
    # Affichage temporaire pour debug (optionnel)
    # st.write("Colonnes fournies :", data.columns.tolist())
    # st.write("Colonnes attendues :", model.feature_names_in_)
    
    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success('✅ Client fidèle')
    else:
        st.warning('⚠️ Client non fidèle')

# st.image("222.png", caption="2A BANK")
