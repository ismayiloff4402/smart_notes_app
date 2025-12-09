import streamlit as st
from app import add_note, load_notes
from search import search_by_text, search_by_tag
from analytics import count_notes, tag_frequency, activity_by_date

st.title("Smart Notes App")

menu = ["Add note", "Search", "Analytics"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add note":
    st.header("Add a new note")
    title = st.text_input("Title")
    text = st.text_area("Text")
    tags = st.text_input("Tags (comma separated)")

    if st.button("Add"):
        tag_list = [t.strip() for t in tags.split(",") if t.strip()]
        add_note(title, text, tag_list)
        st.success("Note added!")

elif choice == "Search":
    st.header("Search notes")

    query = st.text_input("Search in title/text")
    tag = st.text_input("Search by tag")

    if st.button("Search"):
        results = []

        if query:
            results.extend(search_by_text(query))

        if tag:
            results.extend(search_by_tag(tag))

        st.write(f"Found {len(results)} notes")

        for note in results:
            st.subheader(note["title"])
            st.write(note["text"])
            st.write("Tags:", ", ".join(note["tags"]))
            st.write("Created:", note["created"])
            st.write("---")

elif choice == "Analytics":
    st.header("Analytics")

    st.write("Total notes:", count_notes())

    st.subheader("Tag frequency")
    st.write(tag_frequency())

    st.subheader("Activity by date")
    st.write(activity_by_date())
