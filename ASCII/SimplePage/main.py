import streamlit as st

st.header("ASCII Converter", divider="rainbow" )
st.subheader("A simple tool to convert values to and from ASCII.")

st.markdown('''
    This is a test while the website is under development
''')

def text_to_ascii(pText):
  ascii_values = []
  for char in pText:
      ascii_values.append(ord(char))
  return ascii_values

text = st.text_input("Convert value to ASCII:")
ascii = (text_to_ascii( text))
st.markdown("Your ASCII values are: " + str(ascii))

text1 = st.number_input("Convert value from ASCII: ", value = 1)
character = chr(text1)
st.markdown(str("Your character is: " + character))