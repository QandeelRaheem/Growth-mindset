# streamlit
import streamlit as st

st.set_page_config(page_title ="Growth Mindset Project" , page_icon ="★")
st.title("Growth Mindset Challenge: Web App with streamlit ")

st.header("🚀 Welcome To Your Growth Journey!")
st.write("This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

# quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.- Winston Churchill")

("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


# condition
if user_input:
    st.Success(f"💪 you're facing: {user_input}. Keep pushing forward towords your goal!🚀")
else:
    st.warning("Tell us amount or challenge to get started!")

# reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("write your reflections here:")

if reflection:
    st.Success(f"✨ Great Insight! Your reflection:{reflection}")
else:
    st.info("Reflection on past experience help you grow! Share your difficulties")


# acheivements
st.header("🏆 Celebrate Your Wins!")
acheivement = st.text_input("Share somethings you're recently accomplished:")


if acheivement:
    st.Success(f"🎉 Amazing! You achieved: {acheivement}")
else:
    st.info("Big or small , every achivement counts! share one now! 😍")


# footer
st.write("- - -")
st.write("🚀 Keep belivieving in yourself.  Growth is a Growth is a journey, not a destination! 🌟")
st.write("""⛔ Created by Qandeel Raheem""")
