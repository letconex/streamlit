import streamlit as st
import httpx
slangs = ('de', 'en', 'ro')
tlangs = ('ro', 'de', 'en')
# sourceLang = "de"
# targetLang = "ro"
# sourceLang = st.text_input("Enter source language:")
sourceLang = st.selectbox('Select source language', slangs)
# targetLang = st.text_input("Enter target language:")
targetLang = st.selectbox('Select target language', tlangs)
sourceText = st.text_input("Enter text to translate:")
url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=" + sourceLang + "&tl=" + targetLang + "&dt=t&q=" + sourceText
response = httpx.get(url)
if st.button('Translate'):
  result = response.text
  indexx = result.index('","')
  result = result[4:int(indexx)]
  # st.write(result)
  st.success(result)

import datetime as dt
st.write(f"Now is {now}")
