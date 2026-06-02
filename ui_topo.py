from datetime import datetime

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QDateEdit,
    QMenuBar
)


def criar_topo():

    # =========================================
    # LAYOUT TOPO
    # =========================================

    layout_topo = QHBoxLayout()

    # =========================================
    # NOME DA ESCALA
    # =========================================

    label_nome_escala = QLabel(
        "Nome da Escala:"
    )

    label_nome_escala.setStyleSheet("""
        color: white;
        font-size: 14px;
        font-weight: bold;
    """)

    campo_nome_escala = QLineEdit()

    campo_nome_escala.setPlaceholderText(
        "Ex: Escala Domingo"
    )

    campo_nome_escala.setStyleSheet("""
        background-color: white;
        color: black;
        padding: 5px;
        font-size: 13px;
    """)

    # =========================================
    # DATA
    # =========================================

    label_data = QLabel("Data:")

    label_data.setStyleSheet("""
        color: white;
        font-size: 14px;
        font-weight: bold;
    """)

    campo_data = QDateEdit()

    campo_data.setCalendarPopup(True)

    campo_data.setDate(
        datetime.now().date()
    )

    campo_data.setStyleSheet("""
        background-color: white;
        color: black;
        padding: 5px;
        font-size: 13px;
    """)

    # =========================================
    # ADICIONAR AO LAYOUT
    # =========================================

    layout_topo.addWidget(
        label_nome_escala
    )

    layout_topo.addWidget(
        campo_nome_escala
    )

    layout_topo.addSpacing(20)

    layout_topo.addWidget(
        label_data
    )

    layout_topo.addWidget(
        campo_data
    )

    layout_topo.addStretch()

    # =========================================
    # MENU SUPERIOR
    # =========================================

    menu_bar = QMenuBar()

    menu_arquivo = menu_bar.addMenu(
        "Arquivo"
    )

    acao_novo = menu_arquivo.addAction(
        "Novo"
    )

    acao_abrir = menu_arquivo.addAction(
        "Abrir"
    )

    acao_salvar = menu_arquivo.addAction(
        "Salvar"
    )

    acao_salvar_como = (
        menu_arquivo.addAction(
            "Salvar Como"
        )
    )

    return (
        layout_topo,
        menu_bar,
        campo_nome_escala,
        campo_data,
        acao_novo,
        acao_abrir,
        acao_salvar,
        acao_salvar_como
    )