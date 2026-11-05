import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageOps

# =====================================================
# CONFIGURAÇÃO
# =====================================================

st.set_page_config(
    page_title="Vision Lab | Calculadora DORI",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================
# IDENTIDADE VISUAL
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg: #07111f;
    --panel: #0d1b2d;
    --panel-2: #10243a;
    --line: rgba(148, 184, 220, .15);
    --text: #e8f1fb;
    --muted: #91a8c1;
    --cyan: #35d5f2;
    --blue: #3987ff;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background:
      radial-gradient(ellipse at 12% 0%, rgba(22, 112, 184, .18), transparent 34%),
      radial-gradient(ellipse at 90% 12%, rgba(24, 198, 211, .10), transparent 30%),
      linear-gradient(145deg, #07111f 0%, #091626 48%, #07111f 100%);
    color: var(--text);
}
[data-testid="stHeader"] { background: rgba(7,17,31,.72); }
[data-testid="stToolbar"] { right: 1rem; }
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}
h1, h2, h3, h4 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text) !important;
}
p, label, .stMarkdown, [data-testid="stCaptionContainer"] {
    color: var(--text);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0c1b2d 0%, #091523 100%);
    border-right: 1px solid var(--line);
}
[data-testid="stSidebar"] > div:first-child { padding-top: 1.4rem; }
[data-testid="stSidebar"] label {
    color: #c8d8e9 !important;
    font-weight: 600;
}
[data-testid="stSelectbox"] > div > div,
[data-testid="stSlider"] {
    color: var(--text);
}
div[data-baseweb="select"] > div {
    background: #12263c;
    border: 1px solid rgba(111,166,216,.25);
    border-radius: 10px;
}
div[data-baseweb="select"] * { color: #e8f1fb !important; }
[data-testid="stFileUploader"] section {
    background: rgba(16,36,58,.72);
    border: 1px dashed rgba(53,213,242,.45);
    border-radius: 14px;
}
[data-testid="stFileUploader"] section:hover {
    border-color: var(--cyan);
}
[data-testid="stMetric"] {
    background: linear-gradient(145deg, rgba(17,39,62,.96), rgba(12,27,45,.96));
    border: 1px solid var(--line);
    padding: 18px 20px;
    border-radius: 16px;
    box-shadow: 0 12px 28px rgba(0,0,0,.18);
}
[data-testid="stMetricLabel"] {
    color: #9db5ce !important;
    font-size: .82rem;
    font-weight: 700;
    letter-spacing: .08em;
    text-transform: uppercase;
}
[data-testid="stMetricValue"] {
    color: #f2f8ff !important;
    font-family: 'Space Grotesk', sans-serif;
}
[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: var(--line) !important;
    border-radius: 18px;
    background: rgba(13,27,45,.58);
}
hr { border-color: var(--line); }
.stButton > button {
    border: 1px solid rgba(53,213,242,.45);
    border-radius: 10px;
    background: linear-gradient(100deg, #1262a5, #087e9c);
    color: white;
    font-weight: 700;
}
.stButton > button:hover {
    border-color: #75eaff;
    color: white;
    box-shadow: 0 0 22px rgba(53,213,242,.18);
}
.hero {
    position: relative;
    overflow: hidden;
    padding: 27px 30px;
    border: 1px solid rgba(74,177,226,.25);
    border-radius: 22px;
    background: linear-gradient(110deg, rgba(17,54,86,.96), rgba(11,31,51,.92) 60%, rgba(9,49,66,.92));
    box-shadow: 0 18px 45px rgba(0,0,0,.20);
    margin-bottom: 25px;
}
.hero:after {
    content: "";
    position: absolute;
    width: 250px; height: 250px;
    right: -65px; top: -115px;
    border: 1px solid rgba(53,213,242,.22);
    border-radius: 50%;
    box-shadow: 0 0 0 25px rgba(53,213,242,.035), 0 0 0 55px rgba(53,213,242,.025);
}
.eyebrow {
    color: #5fe5f7;
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: .18em;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    color: #f5faff;
    font-size: clamp(1.8rem, 4vw, 2.7rem);
    font-weight: 700;
    line-height: 1.08;
    margin: 0;
}
.hero-subtitle {
    color: #b4c9dd;
    margin-top: 10px;
    font-size: 1rem;
}
.section-heading {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 22px 0 12px 0;
    color: #eaf5ff;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.18rem;
    font-weight: 600;
}
.section-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--cyan);
    box-shadow: 0 0 12px var(--cyan);
}
.result-card {
    min-height: 128px;
    padding: 19px 20px;
    border-radius: 16px;
    border: 1px solid var(--line);
    background: linear-gradient(145deg, rgba(17,39,62,.98), rgba(11,27,45,.98));
    box-shadow: 0 12px 26px rgba(0,0,0,.16);
}
.result-label {
    color: #9db5ce;
    font-size: .78rem;
    text-transform: uppercase;
    letter-spacing: .1em;
    font-weight: 700;
}
.result-value {
    color: #f5faff;
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.5rem, 2.6vw, 2rem);
    font-weight: 700;
    margin-top: 8px;
}
.result-foot {
    color: #8fa9c2;
    font-size: .78rem;
    margin-top: 4px;
}
.status-pill {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: .82rem;
    font-weight: 700;
    border: 1px solid currentColor;
    margin-top: 8px;
}
.dori-identificar { color: #c4a5ff; background: rgba(142,68,173,.16); }
.dori-reconhecer { color: #ff9d9d; background: rgba(231,76,60,.15); }
.dori-observar { color: #ffd27a; background: rgba(243,156,18,.14); }
.dori-detectar { color: #b8c5d2; background: rgba(127,140,141,.16); }
.dori-abaixo { color: #ff9d9d; background: rgba(231,76,60,.12); }
.note {
    padding: 13px 16px;
    border-radius: 12px;
    border: 1px solid rgba(53,213,242,.18);
    background: rgba(18,75,100,.18);
    color: #b9d3e8;
    font-size: .9rem;
}
.footer {
    color: #6f8ba6;
    font-size: .78rem;
    text-align: center;
    padding-top: 28px;
}
[data-testid="stImage"] img {
    border-radius: 14px;
    border: 1px solid var(--line);
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# DADOS
# =====================================================

SENSORES = {
    '1/4"': 3.2,
    '1/3"': 4.8,
    '1/2.8"': 5.37,
    '1/2.7"': 5.37,
    '1/2"': 6.4,
    '1"': 12.8,
}

LENTES = [2.8, 3.6, 6, 9, 12]

RESOLUCOES = {
    'HD (1280 × 720)': 1280,
    'FHD (1920 × 1080)': 1920,
    'QHD (2560 × 1440)': 2560,
    '4K (3840 × 2160)': 3840,
}

DORI = {
    'Identificar': 250,
    'Reconhecer': 125,
    'Observar': 63,
    'Detectar': 25,
}


# =====================================================
# FUNÇÕES
# =====================================================

def calcular_fov(sensor, focal):
    return 2 * np.degrees(np.arctan(sensor / (2 * focal)))


def largura_coberta(fov, distancia):
    return 2 * distancia * np.tan(np.radians(fov / 2))


def classificar(pxm):
    if pxm >= 250:
        return "Identificar"
    if pxm >= 125:
        return "Reconhecer"
    if pxm >= 63:
        return "Observar"
    if pxm >= 25:
        return "Detectar"
    return "Abaixo"


def simular_camera(img, pxm):
    fator = max(1, int(600 / max(10, pxm)))
    w, h = img.size

    pequena = img.resize(
        (max(1, w // fator), max(1, h // fator)),
        Image.Resampling.BOX
    )
    simulada = pequena.resize((w, h), Image.Resampling.NEAREST)

    blur = max(0, 4 - pxm / 80)
    return simulada.filter(ImageFilter.GaussianBlur(radius=blur))


def estilizar_grafico(ax):
    ax.set_facecolor("#0d1b2d")
    ax.tick_params(colors="#a9bfd4", labelsize=9)
    ax.xaxis.label.set_color("#a9bfd4")
    ax.yaxis.label.set_color("#a9bfd4")
    ax.title.set_color("#eaf5ff")
    for spine in ax.spines.values():
        spine.set_color("#29445f")
    ax.grid(True, color="#29445f", alpha=0.55, linestyle="--")


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:
    st.markdown("## 📡 VISION LAB")
    st.caption("CALCULADORA DORI")
    st.divider()

    st.markdown("### ⚙️ Parâmetros da câmera")

    sensor = st.selectbox(
        "Tamanho do sensor:",
        list(SENSORES.keys()),
        index=2,
        help="Selecione o tamanho do sensor da câmera."
    )

    lente = st.selectbox(
        "Distância focal da lente:",
        LENTES,
        index=1,
        format_func=lambda x: f"{x:.1f} mm",
    )

    res = st.selectbox(
        "Resolução:",
        list(RESOLUCOES.keys()),
        index=1,
    )

    st.markdown("### 📏 Cenário de instalação")
    distancia = st.slider(
        "Distância do objeto (metros):",
        min_value=2,
        max_value=100,
        value=20,
        step=1,
    )

    st.divider()
    st.markdown(
        '<div class="note">Ajuste os parâmetros para visualizar, em tempo real, '
        'o campo de visão e a classificação DORI estimada.</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="footer">VISION LAB<br>Ferramenta de apoio ao dimensionamento</div>',
        unsafe_allow_html=True
    )


# =====================================================
# CÁLCULOS
# =====================================================

sensor_mm = SENSORES[sensor]
res_h = RESOLUCOES[res]

fov = calcular_fov(sensor_mm, lente)
largura = largura_coberta(fov, distancia)
pxm = res_h / largura
nivel = classificar(pxm)

classes = {
    "Identificar": "dori-identificar",
    "Reconhecer": "dori-reconhecer",
    "Observar": "dori-observar",
    "Detectar": "dori-detectar",
    "Abaixo": "dori-abaixo",
}


# =====================================================
# CABEÇALHO
# =====================================================

st.markdown("""
<div class="hero">
    <div class="eyebrow">CALCULADORA DORI • CAMERA PLANNER</div>
    <div class="hero-title">Vision Lab</div>
    <div class="hero-subtitle">Dimensionamento de campo de visão, densidade de pixels
    e análise de nível de detalhe para projetos de CFTV</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-heading"><span class="section-dot"></span> Resultado da análise</div>',
            unsafe_allow_html=True)

# =====================================================
# INDICADORES
# =====================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">Campo de visão horizontal</div>
        <div class="result-value">{fov:.1f}°</div>
        <div class="result-foot">Ângulo de abertura</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">Largura coberta</div>
        <div class="result-value">{largura:.1f} m</div>
        <div class="result-foot">Na distância selecionada</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">Densidade de pixels</div>
        <div class="result-value">{pxm:.0f} <span style="font-size:1rem;color:#9db5ce">px/m</span></div>
        <div class="result-foot">Pixels por metro</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    classe_css = classes[nivel]
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">Classificação DORI</div>
        <div class="result-value" style="font-size:1.65rem">{nivel}</div>
        <span class="status-pill {classe_css}">{pxm:.0f} px/m</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# =====================================================
# GRÁFICOS
# =====================================================

st.markdown('<div class="section-heading"><span class="section-dot"></span> Análise visual</div>',
            unsafe_allow_html=True)

esq, dire = st.columns(2, gap="large")

with esq:
    with st.container(border=True):
        st.markdown("#### ◉ Campo de cobertura")
        fig, ax = plt.subplots(figsize=(7, 4.6))
        fig.patch.set_facecolor("#0d1b2d")
        meia = largura / 2

        ax.fill(
            [0, distancia, distancia],
            [0, meia, -meia],
            color="#25bfe5",
            alpha=0.18
        )
        ax.plot([0, distancia], [0, meia], color="#35d5f2", linewidth=2.5)
        ax.plot([0, distancia], [0, -meia], color="#35d5f2", linewidth=2.5)
        ax.scatter([0], [0], s=110, color="#f4fbff", marker="s",
                   edgecolors="#35d5f2", linewidths=2, zorder=5)
        ax.text(
            distancia * 0.76,
            meia * 0.72,
            f"{fov:.1f}°",
            fontsize=11,
            fontweight="bold",
            color="#66e7f7"
        )
        ax.set_title("Área horizontal de cobertura", pad=14, fontweight="bold")
        ax.set_xlabel("Distância (m)")
        ax.set_ylabel("Largura (m)")
        estilizar_grafico(ax)
        fig.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

with dire:
    with st.container(border=True):
        st.markdown("#### ◉ Curva de densidade DORI")
        x = np.linspace(1, 100, 300)
        y = res_h / largura_coberta(fov, x)

        fig2, ax2 = plt.subplots(figsize=(7, 4.6))
        fig2.patch.set_facecolor("#0d1b2d")

        ax2.semilogy(
            x, y, color="#35d5f2", linewidth=2.8,
            label="Densidade calculada"
        )

        # Faixas de referência DORI
        ax2.axhspan(250, max(250, float(np.max(y))), color="#8e44ad",
                    alpha=0.12, label="Identificar")
        ax2.axhspan(125, 250, color="#e74c3c", alpha=0.10, label="Reconhecer")
        ax2.axhspan(63, 125, color="#f39c12", alpha=0.10, label="Observar")
        ax2.axhspan(25, 63, color="#7f8c8d", alpha=0.12, label="Detectar")

        for limite, cor in [(250, "#bd8cff"), (125, "#ff8585"),
                            (63, "#ffc45e"), (25, "#aebdca")]:
            ax2.axhline(limite, color=cor, linewidth=1.2, alpha=0.85)

        ax2.scatter(
            distancia, pxm, color="#ffffff", s=105,
            edgecolors="#35d5f2", linewidths=2, zorder=10
        )
        ax2.annotate(
            f" {pxm:.0f} px/m",
            (distancia, pxm),
            textcoords="offset points",
            xytext=(8, 9),
            fontsize=9,
            fontweight="bold",
            color="#ffffff"
        )

        ax2.set_xlim(1, 100)
        ax2.set_ylim(10, max(1000, float(np.max(y)) * 1.15))
        ax2.set_title("Pixels por metro × distância", pad=14, fontweight="bold")
        ax2.set_xlabel("Distância (m)")
        ax2.set_ylabel("Pixels por metro (px/m)")
        estilizar_grafico(ax2)
        legend = ax2.legend(loc="upper right", fontsize=8, frameon=True)
        legend.get_frame().set_facecolor("#10243a")
        legend.get_frame().set_edgecolor("#29445f")
        for txt in legend.get_texts():
            txt.set_color("#d9e8f5")
        fig2.tight_layout()
        st.pyplot(fig2, use_container_width=True)
        plt.close(fig2)

# =====================================================
# RESUMO TÉCNICO
# =====================================================

with st.container(border=True):
    st.markdown("#### 📋 Configuração utilizada")
    r1, r2, r3, r4 = st.columns(4)
    r1.metric("Sensor", sensor)
    r2.metric("Lente", f"{lente:.1f} mm")
    r3.metric("Resolução", res.split(" ")[0])
    r4.metric("Distância", f"{distancia} m")

# =====================================================
# SIMULADOR DE IMAGEM
# =====================================================

st.markdown('<div class="section-heading"><span class="section-dot"></span> Simulador de imagem</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="note">Carregue uma imagem de referência para visualizar uma simulação '
    'ilustrativa do efeito da densidade de pixels calculada.</div>',
    unsafe_allow_html=True
)

arquivo = st.file_uploader(
    "Selecione uma imagem de referência",
    type=["jpg", "jpeg", "png"],
    help="Formatos aceitos: JPG, JPEG e PNG."
)

if arquivo:
    try:
        img = Image.open(arquivo)
        img = ImageOps.exif_transpose(img).convert("RGB")
        simulada = simular_camera(img, pxm)

        col1, col2 = st.columns(2, gap="large")
        with col1:
            with st.container(border=True):
                st.markdown("#### Imagem original")
                st.image(img, use_container_width=True)
        with col2:
            with st.container(border=True):
                st.markdown(f"#### Simulação estimada • {pxm:.0f} px/m")
                st.image(simulada, use_container_width=True)
    except Exception as erro:
        st.error(f"Não foi possível abrir a imagem. Verifique o arquivo enviado. Detalhe: {erro}")
else:
    st.info("Envie uma imagem para comparar a referência com a simulação estimada.")

# =====================================================
# RODAPÉ
# =====================================================

st.markdown("""
<div class="footer">
    VISION LAB · CALCULADORA DORI<br>
    Desenvolvido por Marco Piva
</div>
""", unsafe_allow_html=True)
