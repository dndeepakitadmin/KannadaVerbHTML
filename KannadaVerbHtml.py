from io import BytesIO
from docx import Document

doc = Document()
doc.add_paragraph("This is a DOCX file created in memory.")
buffer = BytesIO()
doc.save(buffer)
buffer.seek(0)

st.download_button(
    "⬇️ Download DOCX",
    data=buffer,
    file_name="output.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)
