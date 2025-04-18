import streamlit as st
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

    return "\n".join(output)

st.title("Card List Format Fixer")

input_text = st.text_area("Paste your card list here:", height=300)

if st.button("Convert"):
    if input_text.strip():
        fixed = card_list_fixer(input_text)
        st.text_area("Converted list:", fixed, height=300)
    else:
        st.warning("Please paste a card list to convert.")