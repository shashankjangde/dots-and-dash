import streamlit as st
from streamlit_lottie import st_lottie

import translator as t

st.set_page_config(page_title="dots & dash", page_icon="logo.png")

with st.container():
    l_side, m_side, r_side = st.columns([1, 5, 1])
    with m_side:
        st.image("biglogo.png")


with st.container():
    l_side, r_side = st.columns(2)
    hi_lottie = t.load_lottiefile("hi.json")

    with l_side:

        st_lottie(hi_lottie, key="Hi")
    with r_side:
        st.subheader(" ")

        st.header("Welcome to dots & dash")
        st.subheader(
            "\nThis is a online text to Morse code translator made in Python and Streamlit."
        )
        st.subheader("How to translate:")
        st.text("1. Enter your input in the input box.")
        st.text("2. Click translate button.")
        st.text("3. Get the text translated..")

        choice = st.selectbox(
            "Do you want to traslate:", ("Text to Morse Code", "Morse Code To Text")
        )

    if choice == "Text to Morse Code":
        with st.container():
            inp = st.text_input("Enter your preferred text:")
            a, b, c, d, e = st.columns(5)
            with c:
                but1 = st.button("Translate")

            if but1:
                st.subheader("The translation will be displayed below:")

                st.markdown(
                    '" " represents ending of each letter and "/" represents whitespace between each word.'
                )
                st.subheader("")
                trans = t.to_morse(inp)
                st.subheader(f"Output:- {trans}")
                st.subheader("Listen to the translation below:")
                t.to_aud(trans)
                st.audio("output.mp3")

    elif choice == "Morse Code To Text":
        with st.container():
            inp = st.text_input("Enter your morse code:")
            a, b, c, d, e = st.columns(5)
            with c:
                but1 = st.button("Translate")

            if but1:
                st.subheader("The translation is displayed below:")
                st.subheader("")
                trans = t.to_text(inp)
                st.subheader(f"Output:- {trans.lower()}")
                st.subheader("")

                st.subheader("Listen to the translation below:")
                t.to_aud(trans)

                st.audio("output.mp3")
