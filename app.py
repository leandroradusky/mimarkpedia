import streamlit as st
from app_pages import intro, notfound
from app_pages.mass_spectrometry import ms38ce

sections = {
    "General info": {
        "Introduction": intro,  
    },
    "Cohorts": {
        "Mass spectrometry": {
            "MS-38-CE": ms38ce,  
            "MS-107-CE": notfound,  
        },
    },
}

def load_css():
    with open("assets/css/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def sidebar_navigation():
    def render_sidebar_items(items, depth=0):
        for label, value in items.items():
            if isinstance(value, dict):
                if depth == 0:
                    st.markdown(f"### {label}")
                    render_sidebar_items(value, depth + 1)
                else:
                    with st.expander(label, expanded=True):
                        render_sidebar_items(value, depth + 1)
            else:
                if st.button(label):
                    st.session_state.current_page = value  

    with st.sidebar:
        render_sidebar_items(sections)



def display_content():
    if "current_page" in st.session_state:
        st.session_state.current_page.display()
    else:
        intro.display()  

def main():
    load_css()
    sidebar_navigation()

    display_content()  

if __name__ == "__main__":
    main()
