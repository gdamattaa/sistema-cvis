import webbrowser

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QFrame
)


def criar_painel_direita():

    layout_direita = QVBoxLayout()

    layout_direita.setSpacing(3)

    layout_direita.setContentsMargins(
        5, 5, 5, 5
    )

    # =========================================
    # PAINEL DE OBSERVAÇÕES
    # =========================================

    titulo_obs = QLabel(
        "OBSERVAÇÕES"
    )

    titulo_obs.setAlignment(
        Qt.AlignmentFlag.AlignCenter
    )

    titulo_obs.setFixedHeight(30)

    titulo_obs.setStyleSheet("""
        font-size: 15px;
        font-weight: bold;
        color: white;
        background-color: #444;
        padding: 5px;
    """)

    layout_direita.addWidget(
        titulo_obs
    )

    campo_obs = QTextEdit()

    campo_obs.setPlaceholderText(
        "Digite observações..."
    )

    campo_obs.setStyleSheet("""
        background-color: white;
        color: black;
        font-size: 14px;
        padding: 5px;
    """)

    campo_obs.setFixedHeight(120)

    layout_direita.addWidget(
        campo_obs
    )

    # =========================================
    # BOTÃO GOOGLE FORMS
    # =========================================

    botao_forms = QPushButton(
        "LINK GOOGLE FORMS"
    )

    botao_forms.setCursor(
        Qt.CursorShape.PointingHandCursor
    )

    botao_forms.setStyleSheet("""
        background-color: #4285F4;
        color: white;
        font-size: 13px;
        font-weight: bold;
        padding: 8px;
    """)

    layout_direita.addSpacing(10)

    layout_direita.addWidget(
        botao_forms
    )

    botao_forms.clicked.connect(
        lambda: webbrowser.open(
            "https://forms.gle/Kc84B9fjhaFWx3Xs7"
        )
    )

    layout_direita.addStretch()

    # =========================================
    # PAINEL FINAL
    # =========================================

    painel_direita = QFrame()

    painel_direita.setLayout(
        layout_direita
    )

    painel_direita.setStyleSheet("""
        background-color: #111;
    """)

    painel_direita.setFixedWidth(300)

    return (
        painel_direita,
        campo_obs
    )