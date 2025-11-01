import streamlit as st
import os

# Title
st.set_page_config(page_title="Kannada Verb HTML Generator", layout="centered")
st.title("📘 Kannada Verb HTML Generator")
st.markdown("Generate HTML pages for Kannada verbs with tenses and Kannada-script Hindi meanings.")

# Input verbs
verbs_input = st.text_area("Enter Kannada verbs (one per line):", height=300)

# Base output directory
output_dir = "output_html"
os.makedirs(output_dir, exist_ok=True)

# HTML template
def generate_html(verb):
    return f"""
<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<title>{verb}</title>
<style>
body {{
    background-color: #fdf6e3;
    font-family: "Noto Sans Kannada", sans-serif;
    padding: 20px;
    line-height: 1.8;
}}
h2 {{
    color: #d6336c;
    font-size: 28px;
    border-bottom: 2px solid #d6336c;
    display: inline-block;
    padding-bottom: 5px;
}}
h3 {{
    color: #444;
}}
p {{
    font-size: 22px;
    margin-left: 20px;
}}
.arrow {{
    color: #555;
    margin-left: 40px;
}}
</style>
</head>
<body>
<h2>{verb}</h2>

<div>
<h3>🧍 ನಾನು</h3>
<p>ಹಿಂದಿನ ಕಾಲ: ನಾನು {verb}ದೆ.</p>
<p class="arrow">→ ಮೈ ಕಮ್ ಕಿಯಾ</p>

<p>ವರ್ತಮಾನ ಕಾಲ: ನಾನು ಈಗ {verb}ತ್ತಿದ್ದೇನೆ.</p>
<p class="arrow">→ ಮೈ ಅಬಿ ಕಮ್ ಕರ ರಹಾ ಹೂಂ</p>

<p>ಭವಿಷ್ಯತ್ತಿನ ಕಾಲ: ನಾನು ನಾಳೆ {verb}ತ್ತೇನೆ.</p>
<p class="arrow">→ ಮೈ ಕಲ ಕಮ್ ಕರೂಂಗಾ</p>

<h3>🧍 ನೀನು</h3>
<p>ಹಿಂದಿನ ಕಾಲ: ನೀನು {verb}ದೆ.</p>
<p class="arrow">→ ತುಮನೇ ಕಮ್ ಕಿಯಾ</p>

<p>ವರ್ತಮಾನ ಕಾಲ: ನೀನು ಈಗ {verb}ತ್ತಿದ್ದೀಯ.</p>
<p class="arrow">→ ತುಮ ಕಮ್ ಕರ ರಹೇ ಹೋ</p>

<p>ಭವಿಷ್ಯತ್ತಿನ ಕಾಲ: ನೀನು ನಾಳೆ {verb}ತ್ತೀಯ.</p>
<p class="arrow">→ ತು ಕಲ ಕಮ್ ಕರೇಗಾ</p>

<h3>🧍 ಅವನು</h3>
<p>ಹಿಂದಿನ ಕಾಲ: ಅವನು {verb}ದನು.</p>
<p class="arrow">→ ಉಸನೇ ಕಮ್ ಕಿಯಾ ಥಾ</p>

<p>ವರ್ತಮಾನ ಕಾಲ: ಅವನು ಈಗ {verb}ತ್ತಿದ್ದಾನೆ.</p>
<p class="arrow">→ ವಹ ಕಮ್ ಕರ ರಹಾ ಹೈ</p>

<p>ಭವಿಷ್ಯತ್ತಿನ ಕಾಲ: ಅವನು ನಾಳೆ {verb}ತ್ತಾನೆ.</p>
<p class="arrow">→ ವಹ ಕಲ ಕಮ್ ಕರೇಗಾ</p>

<h3>🧍 ಅವಳು</h3>
<p>ಹಿಂದಿನ ಕಾಲ: ಅವಳು {verb}ದಳು.</p>
<p class="arrow">→ ಉಸನೇ ಕಮ್ ಕಿಯೀ ಥೀ</p>

<p>ವರ್ತಮಾನ ಕಾಲ: ಅವಳು ಈಗ {verb}ತ್ತಿದ್ದಾಳೆ.</p>
<p class="arrow">→ ವಹ ಕಮ್ ಕರ ರಹೀ ಹೈ</p>

<p>ಭವಿಷ್ಯತ್ತಿನ ಕಾಲ: ಅವಳು ನಾಳೆ {verb}ತ್ತಾಳೆ.</p>
<p class="arrow">→ ವಹ ಕಲ ಕಮ್ ಕರೇಗೀ</p>

<h3>🧍 ನಾವು</h3>
<p>ಹಿಂದಿನ ಕಾಲ: ನಾವು {verb}ದ್ವು.</p>
<p class="arrow">→ ಹಮ್ ನೇ ಕಮ್ ಕಿಯಾ ಥಾ</p>

<p>ವರ್ತಮಾನ ಕಾಲ: ನಾವು ಈಗ {verb}ತ್ತಿದ್ದೇವೆ.</p>
<p class="arrow">→ ಹಮ್ ಕಮ್ ಕರ ರಹೇ ಹೈಂ</p>

<p>ಭವಿಷ್ಯತ್ತಿನ ಕಾಲ: ನಾವು ನಾಳೆ {verb}ತ್ತೇವೆ.</p>
<p class="arrow">→ ಹಮ್ ಕಲ ಕಮ್ ಕರೇಂಗೇ</p>

<h3>🧍 ನೀವು</h3>
<p>ಹಿಂದಿನ ಕಾಲ: ನೀವು {verb}ದಿರಿ.</p>
<p class="arrow">→ ಆಪನೇ ಕಮ್ ಕಿಯಾ ಥಾ</p>

<p>ವರ್ತಮಾನ ಕಾಲ: ನೀವು ಈಗ {verb}ತ್ತಿದ್ದೀರಿ.</p>
<p class="arrow">→ ಆಪ ಕಮ್ ಕರ ರಹೇ ಹೈಂ</p>

<p>ಭವಿಷ್ಯತ್ತಿನ ಕಾಲ: ನೀವು ನಾಳೆ {verb}ತ್ತೀರಿ.</p>
<p class="arrow">→ ಆಪ ಕಲ ಕಮ್ ಕರೇಂಗೇ</p>

<h3>🧍 ಅವರು</h3>
<p>ಹಿಂದಿನ ಕಾಲ: ಅವರು {verb}ದರು.</p>
<p class="arrow">→ ಉನ್ಹೋನೇ ಕಮ್ ಕಿಯಾ ಥಾ</p>

<p>ವರ್ತಮಾನ ಕಾಲ: ಅವರು ಈಗ {verb}ತ್ತಿದ್ದಾರೆ.</p>
<p class="arrow">→ ವೇ ಕಮ್ ಕರ ರಹೇ ಹೈಂ</p>

<p>ಭವಿಷ್ಯತ್ತಿನ ಕಾಲ: ಅವರು ನಾಳೆ {verb}ತ್ತಾರೆ.</p>
<p class="arrow">→ ವೇ ಕಲ ಕಮ್ ಕರೇಂಗೇ</p>
</div>
</body>
</html>
"""

if st.button("Generate HTML Files"):
    if not verbs_input.strip():
        st.warning("Please enter at least one verb!")
    else:
        verbs = [v.strip() for v in verbs_input.splitlines() if v.strip()]
        for verb in verbs:
            html_content = generate_html(verb)
            file_path = os.path.join(output_dir, f"{verb}.html")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)
        st.success(f"✅ Generated {len(verbs)} HTML files in `{output_dir}/` folder!")
        st.balloons()
