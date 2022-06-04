import streamlit as st
import datetime
import files.algorithms_app as algo


# 程序入口
def main():
    # 应用页面设置（显示在网站标签）
    st.set_page_config(page_title="路明非的算法笔记", page_icon=":rainbow:", layout="wide", initial_sidebar_state="auto")
    # 加载成功动画
    st.balloons()

    with st.sidebar:
        st.success('## ' + datetime.datetime.now().strftime("%Y-%m-%d"))
        st.info("## 欢迎来到路明非的算法笔记")
        algo_selectbox = st.selectbox(label="", options=["请选择一个算法", "1-冒泡排序", "2-选择排序", "3-插入排序", "4-希尔排序",
                                                         "5-快速排序", "6-归并排序", "7-堆排序", "8-桶排序", "9-基数排序", "10-计数排序"])

    a11, a12 = st.columns([5, 5])
    a11.markdown("""#### 参考1：[算法通关手册（LeetCode）](https://algo.itcharge.cn/01.Array/02.Array-Sort)""")
    a12.markdown("""#### 参考2：[python实例](https://www.runoob.com/python3/python3-examples.html)""")
    st.markdown('''---''')  # 分割线

    def data():
        if algo_selectbox == "请选择一个算法":
            return None
        elif algo_selectbox == "1-冒泡排序":
            return algo.bubble_sort
        elif algo_selectbox == "2-选择排序":
            return algo.select_sort
        elif algo_selectbox == "3-插入排序":
            return algo.insert_sort
        elif algo_selectbox == "4-希尔排序":
            return algo.shell_sort
        elif algo_selectbox == "5-快速排序":
            return algo.quick_sort
        elif algo_selectbox == "6-归并排序":
            return algo.merge_sort
        elif algo_selectbox == "7-堆排序":
            return algo.heap_sort
        elif algo_selectbox == "8-桶排序":
            return algo.bucket_sort
        elif algo_selectbox == "9-基数排序":
            return algo.radix_sort
        elif algo_selectbox == "10-计数排序":
            return algo.counting_sort

    if data():
        st.write(data().compare)
        st.write(data().compares)
        c11, c12 = st.columns([4, 1])
        with c11:
            st.code(data().code, language="python")
        with c12:
            text = st.text_input(label="请输入您的数组（例：54,26,17,31,20,13）：",
                                 value="54,26,17,31,20,13")
            if st.button("运行") and text:
                res = list(map(int, text.strip().split(',')))
                st.write("算法的运行结果是：", data().sort_array(res))

    st.image('files/algorithms_app/image/sort.png')
    st.image('files/algorithms_app/image/a11.png')


# 运行：streamlit run app_myalgo.py
if __name__ == '__main__':
    main()
