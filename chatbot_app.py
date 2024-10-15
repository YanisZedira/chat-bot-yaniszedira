import os
from dotenv import load_dotenv
import streamlit as st
from mistralai import Mistral

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
api_key = os.getenv("API_KEY_MISTRAL")

# Vérifier si la clé API est présente
if api_key is None:
    st.error("Erreur : Clé API non définie. Assurez-vous que le fichier .env contient la clé API.")
else:
    # Initialiser Mistral avec la clé API
    client = Mistral(api_key=api_key)

# Liste des questions autorisées avec réponses adaptées à ton profil
authorized_questions = {
    "formation": "Je suis actuellement en 2e année de bachelor en Data et Intelligence Artificielle à HETIC.",
    "expérience professionnelle": "Je travaille en tant qu'alternant Data Analyst chez Suez, où je participe à des projets de collecte, d'analyse, et de visualisation de données.",
    "missions chez suez": (
        "Chez Suez, mes missions incluent : recenser les besoins en DATA, organiser et participer aux réunions, cadrer les demandes de DATA, "
        "participer à la collecte, au nettoyage et à la préparation des données, contribuer à l'analyse et à la modélisation des données, "
        "et assister à la mise en place d'outils de visualisation et de reporting."
    ),
    "passions": "Je suis passionné par le domaine médical et par l'analyse de données. Mon objectif est de développer des solutions innovantes en IA pour améliorer l'expérience client et optimiser les opérations.",
    "intérêt médical": "Je suis particulièrement intéressé par les maladies comme le cancer et le diabète. J'espère contribuer à des avancées significatives dans le diagnostic et le traitement de ces pathologies.",
    "objectifs futurs": "À l'avenir, je souhaite continuer à développer des compétences en intelligence artificielle, particulièrement dans le domaine de la santé, afin d'apporter des solutions qui impactent positivement la vie des patients."
}

# Ajout de variations des questions
question_keywords = {
    "formation": ["formation", "études", "bachelor"],
    "expérience professionnelle": ["expérience", "alternance", "emploi", "job", "travail", "stage"],
    "missions chez suez": ["suez", "missions", "tâches", "responsabilités"],
    "passions": ["passions", "intérêts", "hobbies", "passion"],
    "intérêt médical": ["médical", "santé", "cancer", "diabète", "maladies"],
    "objectifs futurs": ["futurs", "avenir", "objectif", "projets"]
}

# Fonction pour vérifier si une question correspond à une question autorisée
def get_response_for_question(user_input):
    for key, keywords in question_keywords.items():
        if any(keyword in user_input.lower() for keyword in keywords):
            return authorized_questions[key]
    return None

# Fonction pour générer une réponse
def generate_response(user_input):
    try:
        response = get_response_for_question(user_input)
        if response:
            return response
        else:
            return "Désolé, je ne peux répondre qu'à des questions sur mon parcours professionnel, ma formation, mes missions chez Suez, et mes passions pour l'IA et la santé. Les questions autorisées sont listées ci-dessus."
    except Exception as e:
        return f"Erreur lors de la génération de la réponse : {str(e)}"

# Titre de l'application
st.title("Chatbot Portfolio Professionnel de Yanis Zedira")

# Affichage des questions disponibles sous forme de boutons cliquables sur deux lignes
st.write("### Questions disponibles :")

# Organisation des boutons en deux lignes de trois colonnes
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Formation"):
        user_input = "formation"
        response = generate_response(user_input)
        st.session_state.chat_history.append(("Vous", user_input))
        st.session_state.chat_history.append(("Bot", response))

with col2:
    if st.button("Expérience professionnelle"):
        user_input = "expérience professionnelle"
        response = generate_response(user_input)
        st.session_state.chat_history.append(("Vous", user_input))
        st.session_state.chat_history.append(("Bot", response))

with col3:
    if st.button("Missions chez Suez"):
        user_input = "missions chez Suez"
        response = generate_response(user_input)
        st.session_state.chat_history.append(("Vous", user_input))
        st.session_state.chat_history.append(("Bot", response))

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("Passions"):
        user_input = "passions"
        response = generate_response(user_input)
        st.session_state.chat_history.append(("Vous", user_input))
        st.session_state.chat_history.append(("Bot", response))

with col5:
    if st.button("Intérêt médical"):
        user_input = "intérêt médical"
        response = generate_response(user_input)
        st.session_state.chat_history.append(("Vous", user_input))
        st.session_state.chat_history.append(("Bot", response))

with col6:
    if st.button("Objectifs futurs"):
        user_input = "objectifs futurs"
        response = generate_response(user_input)
        st.session_state.chat_history.append(("Vous", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Sauvegarde de l'historique des conversations
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Formulaire pour saisir une question manuellement
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Posez votre question :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')

# Si une question est posée manuellement, générer la réponse et l'ajouter à l'historique
if submit_button and user_input:
    response = generate_response(user_input)
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Affichage de l'historique des échanges
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")
