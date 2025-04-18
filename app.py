import streamlit as st
import re
from clipboard_component import copy_component

def card_list_fixer(card_list):
    output = []
    for line in card_list.strip().splitlines():
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

st.title("Fabrary to FabProxy Converter")

input_text = st.text_area("Paste your Fabrary card list here:")

if st.button("Reformat"):
    result = card_list_fixer(input_text)
    output_text = "\n".join(result)

    st.subheader("FabProxy Card List:")
    st.text_area("Result", output_text, height=300, key="output_area")

    copy_component(name="Copy to Clipboard", content=output_text)
