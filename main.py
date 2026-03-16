import streamlit as st
import pandas as pd
import plotly.express as px

# 1. СТИЛЬ ЖӘНЕ БЕТ БАПТАУЫ
st.set_page_config(page_title="Edu Analytics KZ", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #F8F9FA; }
    h1, h2 { color: #1E3A8A; font-family: 'Georgia', serif; border-bottom: 2px solid #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

# 2. ДЕРЕКТЕРДІ ҚҰРАСТЫРУ (Pandas)
grants_data = pd.DataFrame({
    'Бағыт': ['IT', 'IT', 'IT', 'Медицина', 'Медицина', 'Педагогика', 'Педагогика', 'Инженерия'],
    'Мамандық': ['Ақпараттық қауіпсіздік', 'Data Science', 'Software Eng', 'Жалпы медицина', 'Стоматология', 'Математика', 'Физика', 'Құрылыс'],
    'Грант_саны': [1500, 800, 1200, 2000, 300, 1000, 700, 1800],
    'Шекті_балл': [115, 110, 108, 125, 130, 95, 90, 100]
})

serpin_data = pd.DataFrame({
    'Өңір': ['СҚО', 'ШҚО', 'Павлодар', 'Қостанай', 'Ақмола'],
    'Квота': [500, 450, 600, 400, 350],
    'Игерілгені': [480, 410, 580, 320, 340]
})

grads_data = pd.DataFrame({
    'Университет': ['AITU', 'ENU', 'KazNU', 'KBTU', 'Satbayev', 'SDU'],
    'Жұмыс_%': [95, 88, 85, 92, 87, 90],
    'Жалақы': [450000, 320000, 310000, 480000, 350000, 400000],
    'Түлектер_саны': [800, 2500, 3000, 700, 1500, 1200]
})

st.title("🎓 Қазақстан Жоғары Білім Беру Аналитикасы")

# --- 1. TREEMAP: ГРАНТТАР ---
st.header("1. Мамандықтар бойынша гранттар бөлінісі")
fig1 = px.treemap(grants_data, path=['Бағыт', 'Мамандық'], values='Грант_саны', 
                  color='Грант_саны', color_continuous_scale='Blues')
st.plotly_chart(fig1, use_container_width=True)

# --- 2. BAR CHART: СЕРПІН ---
st.header("2. 'Серпін' бағдарламасының тиімділігі")
fig2 = px.bar(serpin_data, x='Өңір', y=['Квота', 'Игерілгені'], barmode='group',
             color_discrete_map={'Квота': '#1E3A8A', 'Игерілгені': '#60A5FA'})
st.plotly_chart(fig2, use_container_width=True)

# --- 3. BUBBLE CHART: ТҮЛЕКТЕР ---
st.header("3. Жұмысқа орналасу және Орташа жалақы")
fig3 = px.scatter(grads_data, x="Жұмыс_%", y="Жалақы", size="Түлектер_саны", 
                 color="Университет", hover_name="Университет", size_max=60)
st.plotly_chart(fig3, use_container_width=True)

# --- 4. PREDICTOR: ГРАНТҚА ТҮСУ ---
st.sidebar.header("🎯 Grant Predictor")
user_score = st.sidebar.number_input("ҰБТ балыңыз:", 50, 140, 100)
user_major = st.sidebar.selectbox("Мамандық таңдаңыз:", grants_data['Мамандық'].unique())

# Pandas Filter
major_info = grants_data[grants_data['Мамандық'] == user_major].iloc[0]
threshold = major_info['Шекті_балл']

st.header("4. Грантқа түсу мүмкіндігін болжау")
col1, col2 = st.columns(2)
col1.metric("Сіздің балыңыз", user_score)
col1.metric("Шекті балл (былтыр)", threshold)

if user_score >= threshold:
    col2.success(f"Мүмкіндік ЖОҒАРЫ! Сіз {user_major} грантына үміткерсіз.")
    st.balloons()
else:
    col2.error(f"Мүмкіндік ТӨМЕН. Бұл мамандыққа кемінде {threshold} балл керек.")

st.info("Academic Style Dashboard 2024")