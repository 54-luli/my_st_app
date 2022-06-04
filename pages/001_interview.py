import streamlit as st
import datetime
import files.interview_app as iv


# 程序入口
def main():
    # 应用页面设置（显示在网站标签）
    st.set_page_config(page_title="路明非的面试题库", page_icon=":rainbow:", layout="wide", initial_sidebar_state="auto")
    # 加载成功动画
    st.balloons()

    with st.sidebar:
        st.success('## ' + datetime.datetime.now().strftime("%Y-%m-%d"))
        st.info("## 欢迎来到路明非的面试题库")
        gs_selectbox = st.selectbox(label="", options=["全部", "阿里巴巴", "字节跳动"])
        gw_selectbox = st.selectbox(label="", options=["后端"])
        tm_selectbox = st.selectbox(label="",
                                    options=[
                                        "计算机网络", "操作系统",
                                        "Java基础", "Java多线程", "Java虚拟机", "设计模式",
                                        "数据结构与算法", "数据库", "Redis"])

    c11, c12= st.columns([0.75, 9.25])
    c11.markdown("##### 编号")
    c12.markdown("##### 题目")
    st.markdown('''---''')  # 分割线

    data = ()
    if tm_selectbox:
        if tm_selectbox == "计算机网络":
            data = iv.cnet
        elif tm_selectbox == "操作系统":
            data = iv.os
        elif tm_selectbox == "Java基础":
            data = iv.java
        elif tm_selectbox == "Java虚拟机":
            data = iv.jvm
        elif tm_selectbox == "Java多线程":
            data = iv.jmt
        elif tm_selectbox == "设计模式":
            data = iv.dm
        elif tm_selectbox == "数据结构与算法":
            data = iv.ds_al
        elif tm_selectbox == "数据库":
            data = iv.mysql
        elif tm_selectbox == "Redis":
            data = iv.redis
        n = len(data)
        st.write(f"该目录下有{n}道题：")
        for cnt in range(n):
            d11, d12= st.columns([0.75, 9.25])
            d11.markdown("#### " + str(cnt + 1))
            with d12:
                with st.expander(data[cnt][0]):
                    st.markdown(data[cnt][1])


# 运行：streamlit run app_interview.py
if __name__ == '__main__':
    main()
