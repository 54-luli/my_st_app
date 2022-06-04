import streamlit as st


# 运行：streamlit run hello.py
def main():
    st.set_page_config(page_title="主页", page_icon="🎉", layout="wide")
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")


if __name__ == '__main__':
    main()
