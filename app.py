import streamlit as st

st.set_page_config(page_title='Мій додаток 67', page_icon='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRD1UAm4I-BBebCjpi5YGNMwPrB6Vpt45RxGkwtqajSF6Pk0bwRAgdCGt4b&s=10', layout='wide')

st.title('Салют! Сікс севен!')

tab1, tab2, tab3= st.tabs(['Про мене', 'Мій інструмент', 'Корисні посилання'])

with tab1:
    st.header('Знайомствo з автором')
    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader('Привіт! Я фанат Скали')
        st.write('Я навчаюсь в Малій Компютерній Академії IT STEP. Створюю крути веб-додатки')

        with st.container():
                    st.info('Контакти для звязку:')
                    st.markdown('- Телеграм: [посилання](https://t.me/sixseven)')
                    st.markdown('- Пошта: [посилання](sixseven@gmail.com)')
    with col2:
        st.image('https://i.pinimg.com/1200x/3e/9b/bf/3e9bbf8c2c3d701854e018da42af838b.jpg', width=300)

with tab2:
    st.info('У процессі розробки...')

with tab3:
    st.header('Список моїх улюблених навчальних сайтів:')

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('- 🧐: [Вікіпедія](https://us.wikipedia.org/wiki/Main_Pagw)')
        st.markdown('- 📺: [Youtube](https://www.youtube.com/)')

    with col2:
        st.markdown('- 🕹️: [YPT](https://www.yeolpumta.com/en/)')
        st.markdown('- 📝: [Notion](https://www.notion.com/б)')