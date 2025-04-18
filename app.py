import streamlit as st
import pyperclip
import re

def card_list_fixer(input_text):
    output = []
    for line in input_text.strip().splitlines():
        line = line.strip()
        if not line or "cards" in line.lower():
            continue
        match = re.match(r"(\d+)x (.+)", line)

        if line.lower().startswith("hero:"):
            hero_card = line.split(":", 1)[1].strip()
            output.append(hero_card)
            continue

        if match:
            count = int(match.group(1))
            card_name = match.group(2)
            output.extend([card_name] * count)

    return output

st.title("Fab Proxy Card List Fixer")

input_text = st.text_area("Paste your Fabrary card list here:")

if st.button("Reformat"):
    result = card_list_fixer(input_text)
    output_text = "\n".join(result)

    st.subheader("FabProxy Card List:")
    st.text_area("FabProxy Card List", output_text, height=300)

    if st.button("Copy to Clipboard"):
        pyperclip.copy(output_text)
        st.success("Card list copied to clipboard!")
