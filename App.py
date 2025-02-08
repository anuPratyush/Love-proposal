import streamlit as st
import time

# Streamlit Page Configuration
st.set_page_config(page_title="My Love Proposal ❤️", page_icon="💖", layout="centered")

# Title
st.title("💘 Will You Be My Valentine, Anushka? 💖")

# Button Container
button_container = st.empty()

# Function to Handle Button Click
def on_click():
    # Clear Buttons
    button_container.empty()
    
    # Show Romantic Message
    st.markdown("<h2 style='color:red; text-align:center;'>I Love You ❤️</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#ff1493; text-align:center;'>My Babe, My Cutie Pie, My Sweetu, My Bacha, My Love, My World, My Everything 💖</h3>", unsafe_allow_html=True)
    
    # Small Hearts Animation
    heart_animation = """
    <div style="text-align:center; font-size:50px;">
        ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️
    </div>
    """
    st.markdown(heart_animation, unsafe_allow_html=True)
    
    # Delay for Heart Animation
    time.sleep(2)

    # Show "Pratyush 💘 Anushka" in Heart
    heart_text_animation = """
    <div style="text-align: center; font-size: 30px; color: red;">
        ❤️ <b>Pratyush 💘 Anushka</b> ❤️
    </div>
    """
    st.markdown(heart_text_animation, unsafe_allow_html=True)

    # Delay before Showing the Rose
    time.sleep(2)

    # Show Beautiful Rose
    rose = """
    <h2 style="color: green; text-align:center;">A beautiful rose for you, Anushka! 🌹</h2>
    """
    st.markdown(rose, unsafe_allow_html=True)

# Display Yes/No Buttons
if button_container.button("Yes ❤️", key="yes_button"):
    on_click()

if button_container.button("No 💔", key="no_button"):
    on_click()  # No bhi Yes ke tara behave karega

