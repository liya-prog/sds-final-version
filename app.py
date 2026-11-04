import streamlit as st
import time

st.set_page_config(page_title="SDS 安全資料表翻譯系統", layout="centered")
st.title("📄 SDS 安全資料表翻譯系統")
st.markdown("上傳您的英文或簡體中文 SDS 檔案，系統將自動保留危害圖樣與排版，並翻譯為繁體中文。")

uploaded_file = st.file_uploader("請上傳 SDS 檔案 (支援 PDF, DOCX)", type=["pdf", "docx"])
language = st.radio("請選擇原始檔案語言：", ["英文 (English)", "簡體中文"])

if uploaded_file is not None:
    st.success(f"已成功載入檔案：{uploaded_file.name}")
    
    if st.button("開始翻譯"):
        progress_text = "正在解析文件格式與萃取危害圖示..."
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.02)
            if percent_complete == 30:
                my_bar.progress(percent_complete + 1, text="正在呼叫文件翻譯 API...")
            elif percent_complete == 60:
                my_bar.progress(percent_complete + 1, text="正在回填文字並重建原始排版...")
            elif percent_complete == 90:
                my_bar.progress(percent_complete + 1, text="即將完成...")
            else:
                my_bar.progress(percent_complete + 1)
                
        my_bar.empty()
        st.success("🎉 翻譯完成！")
        
        fake_translated_data = b"This is a mocked translated PDF content."
        st.download_button(
            label="⬇️ 下載翻譯後的繁體中文檔案",
            data=fake_translated_data,
            file_name=f"翻譯完成_{uploaded_file.name}",
            mime="application/pdf"
        )
