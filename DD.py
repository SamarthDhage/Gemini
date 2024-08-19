from dotenv import load_dotenv
import google.generativeai as genai
from random import choices
import streamlit as st
import os

load_dotenv() #loading all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro Model and get response

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    respose = model.generate_content(question)
    return respose.text

#initialize streamlit app

st.set_page_config(page_title="D&d")

st.header("D&D with Gemini")

input=st.text_input("Input : ",key="input")

submit = st.button("Ask the Question")

#when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The response")
    st.write(response)




























# model = GenerativeModel('gemini-1.5-pro')

# r = model.generate_content("whats the full form of HTML")

# print(r.text)

# r2 = model.generate_content("whats the full form of css")

# print(r2.text)


# characters = {

#     "Arannis Faelar": {
#         "Race": "Elf",
#         "Class": "Ranger",
#         "Skills": {
#             "Perception": 92,
#             "Stealth": 90,
#             "Survival": 85,
#             "Nature": 88
#         },
#         "Background": "Arannis grew up in the deep woods of the Elven Kingdom, where he learned to live off the land. His family was part of a clan of rangers who protected the forest from invaders and dark creatures. He has a deep connection with nature and animals, often accompanied by his loyal wolf companion, Shadow. Driven by a desire to protect his homeland, he now ventures into the wider world to combat threats before they reach his forest."
#     },
#     "Tordek Ironfist": {
#         "Race": "Dwarf",
#         "Class": "Cleric",
#         "Skills": {
#             "Medicine": 88,
#             "Religion": 92,
#             "History": 85,
#             "Insight": 80
#         },
#         "Background": "Tordek hails from the ancient halls of the Dwarven Stronghold beneath the mountains. Raised as a devout follower of Moradin, the Dwarf god of creation, he chose the path of a cleric to heal and protect his kin. After receiving a divine vision of a great evil awakening in the world, Tordek embarked on a journey to prevent this darkness from engulfing the realms, offering his healing powers and divine wisdom to those in need."
#     },
#     "Lyra Moonshadow": {
#         "Race": "Half-Elf",
#         "Class": "Bard",
#         "Skills": {
#             "Performance": 95,
#             "Persuasion": 90,
#             "Arcana": 80,
#             "Deception": 85
#         },
#         "Background": "Lyra grew up in a bustling port city, where her elven mother ran an inn popular with travelers. Fascinated by the stories and songs of the patrons, she developed her talents as a bard. Her half-elven heritage gave her a unique perspective, allowing her to bridge cultural divides and charm people from all walks of life. Lyra now travels the world, seeking inspiration for her songs and using her talents to defuse conflicts and uncover hidden secrets."
#     },
#     "Kara Stoneheart": {
#         "Race": "Human",
#         "Class": "Fighter",
#         "Skills": {
#             "Athletics": 85,
#             "Intimidation": 80,
#             "Survival": 75,
#             "Acrobatics": 78
#         },
#         "Background": "Kara was raised in a small frontier village constantly threatened by bandits and wild beasts. Trained from a young age by her warrior father, she became a formidable fighter to protect her home. After her village was destroyed in a raid, Kara set out as a mercenary, offering her sword to those in need of protection. Driven by a desire for justice and vengeance, she seeks out evildoers to punish them for their misdeeds."
#     },
#     "Quinn Lightfoot": {
#         "Race": "Halfling",
#         "Class": "Rogue",
#         "Skills": {
#             "Sleight of Hand": 90,
#             "Stealth": 88,
#             "Investigation": 82,
#             "Thieves' Tools": 85
#         },
#         "Background": "Quinn grew up in the bustling city of Waterdeep, learning the ways of the streets as an orphan. Quick-witted and light on his feet, he became a successful thief and con artist. Despite his criminal beginnings, Quinn has a strong moral compass, often stealing from the corrupt to give to those in need. His talents caught the eye of a secretive guild, which now employs him for daring heists and covert missions. Quinn's charm and agility make him a valuable ally and a dangerous opponent."
#     }
# }

# # def start_game():
# #   print("Welcome adventurers!")
# #   num_players = int(input("How many players are joining today? "))

# #   available_characters = list(characters.keys())
# #   selected_characters = choices(available_characters, k=num_players)

# #   for character_name in selected_characters:
# #     character = characters[character_name]
# #     print(f"\t* {character_name} the {character['Race']} {character['Class']} (")
# #     for skill, value in character["Skills"].items():
# #       print(f"\t\t{skill}: {value}, ", end="")  # Print skills and values on the same line
# #     print(f"\b\b)")  # Remove the trailing comma and space
# #     print(f"\t\tBackground: {character['Background']}")  # Print background story