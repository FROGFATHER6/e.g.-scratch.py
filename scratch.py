
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(page_title="my web", layout="wide")

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)




lottie_dancing = load_lottie_file("C:/Users/adnan/Downloads/Animation - 1751827990988.json")





st.subheader("hi folk")
st.title("daaaaaaamn")
st.write("listen big guy")

st.write("learn more< (https://youtube.com/shorts/SXHMnicI6Pg?si=26UNGzeD551BEj3C)")

st.text_input("what you want")

with st.container():
    st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("so i do not know what in the earth this web is supposed to be "
              "but no problem")




with right_column:
    st_lottie(lottie_dancing, height=300, key="dancing")

















