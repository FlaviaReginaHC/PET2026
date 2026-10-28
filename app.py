from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="DinoArtGallery PRO",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
PASTA_ARTES = BASE_DIR / "artes"
PASTA_RELATORIOS = BASE_DIR / "relatorios"
ARQUIVO_CSS = BASE_DIR / "styles.css"
ARQUIVO_LOGO = BASE_DIR / "arte_logo.png"

PASTA_ARTES.mkdir(parents=True, exist_ok=True)
PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)

if ARQUIVO_CSS.exists() and ARQUIVO_CSS.stat().st_size > 0:
    st.markdown(
        f"<style>{ARQUIVO_CSS.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )

with st.sidebar:
    if ARQUIVO_LOGO.exists():
        st.image(str(ARQUIVO_LOGO), use_container_width=True)
    else:
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="sidebar-brand-icon">🎨</div>
                <div>
                    <div class="sidebar-brand-title">DinoArtGallery</div>
                    <div class="sidebar-brand-pro">PRO</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

paginas = [
    st.Page("pages/Home.py", title="Início", icon="🏠", default=True),
    st.Page("pages/Cadastro.py", title="Cadastrar Obra", icon="➕"),
    st.Page("pages/Artes.py", title="Acervo de Artes", icon="🖼️"),
    st.Page("pages/Avaliacao.py", title="Avaliação Curatorial", icon="🔎"),
    st.Page("pages/Relatorios.py", title="Laudos e Relatórios", icon="📄"),
    st.Page("pages/Dashboard.py", title="Dashboard", icon="📊"),
]

navegacao = st.navigation(paginas, position="sidebar")

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-footer">
            <strong>DinoArtGallery PRO</strong><br>
            Versão 2.0<br>
            Professor Dinaldo Guedes
        </div>
        """,
        unsafe_allow_html=True,
    )

navegacao.run()
