import streamlit as st
import time

st.set_page_config(
    page_title="Happy Teacher's Day 🌸",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #2c003e, #4b006e);
    color: gold;
    text-align: center;
}

.title {
    font-size: 42px;
    font-weight: bold;
    text-shadow: 0 0 20px gold;
    margin-top: 40px;
}

.message {
    font-size: 21px;
    line-height: 1.7;
    margin-top: 30px;
    background: rgba(255, 215, 0, 0.08);
    padding: 28px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
}

.stButton>button {
    background-color: gold;
    color: purple;
    border-radius: 30px;
    font-size: 18px;
    padding: 10px 25px;
    box-shadow: 0 0 15px gold;
    border: none;
}

.stButton>button:hover {
    box-shadow: 0 0 25px gold;
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)


# ---------------- Session Setup ----------------
if "page" not in st.session_state:
    st.session_state.page = 1

if "animation_done" not in st.session_state:
    st.session_state.animation_done = False


# ---------------- Typewriter ----------------
def typewriter(text):
    placeholder = st.empty()
    typed = ""

    for char in text:
        typed += char

        placeholder.markdown(
            '<div class="message">' + typed + '</div>',
            unsafe_allow_html=True
        )

        time.sleep(0.02)


# ================= PAGE 1 =================
if st.session_state.page == 1:

    st.markdown(
        '<div class="title">🔐 Enter Password</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="message">🌸 A Small Teacher\'s Day Surprise 🌸</div>',
        unsafe_allow_html=True
    )

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Open 🔓"):

        if password == "Guri@780":

            st.session_state.page = 2
            st.session_state.animation_done = False
            st.rerun()

        else:

            st.error("Wrong Password ❌ Try Again")


# ================= PAGE 2 =================
elif st.session_state.page == 2:

    st.markdown(
        '<div class="title">🌸 Happy Teacher\'s Day 🌸</div>',
        unsafe_allow_html=True
    )

    welcome_text = """Dear Teacher 💐

Teacher sirf oh nahi hunda jo books padhaunda hai,
balki oh hunda hai jo students nu life vich agge vadhan
da raasta dikhaunda hai. 🌟

Thank you for always guiding us,
supporting us and believing in us. ❤️
"""

    if not st.session_state.animation_done:

        typewriter(welcome_text)

        st.session_state.animation_done = True

    else:

        st.markdown(
            '<div class="message">' + welcome_text + '</div>',
            unsafe_allow_html=True
        )

    if st.button("Next ⏭️"):

        st.session_state.page = 3
        st.session_state.animation_done = False
        st.rerun()


# ================= PAGE 3 =================
elif st.session_state.page == 3:

    st.markdown(
        '<div class="title">🙏 Thank You Teacher</div>',
        unsafe_allow_html=True
    )

    thank_text = """Thank You So Much Ma'am/Sir 🌸

Tusi sirf sanu subjects nahi sikhaunde,
tusi sanu confidence, discipline te
life vich better banan di inspiration dinde ho. ✨

Your guidance means a lot to us. 💐

We are truly grateful to have a teacher like you. ❤️
"""

    if not st.session_state.animation_done:

        typewriter(thank_text)

        st.session_state.animation_done = True

    else:

        st.markdown(
            '<div class="message">' + thank_text + '</div>',
            unsafe_allow_html=True
        )

    if st.button("Next Page ⏭️"):

        st.session_state.page = 4
        st.session_state.animation_done = False
        st.rerun()


# ================= PAGE 4 =================
elif st.session_state.page == 4:

    st.markdown(
        '<div class="title">🌟 A Special Message 🌟</div>',
        unsafe_allow_html=True
    )

    special_text = """A Great Teacher 👩‍🏫👨‍🏫

A great teacher teaches from the heart,
inspires students to dream big,
and makes learning something special. 📚✨

Your words, guidance and encouragement
will always be remembered. 🌸

Thank you for being an amazing teacher. 🙏
"""

    if not st.session_state.animation_done:

        typewriter(special_text)

        st.session_state.animation_done = True

    else:

        st.markdown(
            '<div class="message">' + special_text + '</div>',
            unsafe_allow_html=True
        )

    if st.button("Next ⏭️"):

        st.session_state.page = 5
        st.session_state.animation_done = False
        st.rerun()


# ================= PAGE 5 =================
elif st.session_state.page == 5:

    st.markdown(
        '<div class="title">💐 Once Again 💐</div>',
        unsafe_allow_html=True
    )

    final_text = """🎉 HAPPY TEACHER'S DAY 🎉

Dear Teacher,

Thank you for everything you do for us. ❤️

May you always keep smiling 😊
May you always stay happy 🌸
And may your life be filled with
success, respect and countless beautiful moments. ✨

Thank you for being an inspiration. 🙏

🌸 Happy Teacher's Day! 🌸
"""

    if not st.session_state.animation_done:

        typewriter(final_text)

        st.session_state.animation_done = True

    else:

        st.markdown(
            '<div class="message">' + final_text + '</div>',
            unsafe_allow_html=True
        )

    st.balloons()

    if st.button("🎉 Finish"):

        st.success("Thank You Teacher! 🌸❤️")
