from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt


def criar_painel_lateral(tabela):

    layout_lateral = QVBoxLayout()

    labels_circular = []

    labels_livres = []

    # =========================================
    # PAINEL DE CIRCULARES
    # =========================================

    titulo = QLabel(
        "PRÓXIMOS CIRCULARES"
    )

    titulo.setStyleSheet("""
        font-size: 14px;
        font-weight: bold;
        color: white;
        background-color: #222;
        padding: 5px;
    """)

    layout_lateral.addWidget(titulo)

    for linha in range(5):

        horario = tabela.item(
            linha,
            0
        ).text()

        responsavel = tabela.item(
            linha,
            1
        ).text()

        label = QLabel(
            f"{horario} → {responsavel}"
        )

        label.setStyleSheet("""
            font-size: 15px;
            padding: 8px;
            background-color: #333;
            color: white;
            margin-bottom: 5px;
        """)

        layout_lateral.addWidget(label)

        labels_circular.append(label)

    # =========================================
    # FUNCIONÁRIOS LIVRES
    # =========================================

    titulo_livres = QLabel(
        "FUNCIONÁRIOS LIVRES"
    )

    titulo_livres.setStyleSheet("""
        font-size: 18px;
        font-weight: bold;
        color: white;
        background-color: #1E5128;
        padding: 10px;
        margin-top: 20px;
    """)

    layout_lateral.addWidget(
        titulo_livres
    )

    for i in range(10):

        label_livre = QLabel("")

        label_livre.setStyleSheet("""
            font-size: 14px;
            padding: 6px;
            background-color: #1B4332;
            color: white;
            margin-bottom: 3px;
        """)

        layout_lateral.addWidget(
            label_livre
        )

        labels_livres.append(
            label_livre
        )

    # =========================================
    # PAINEL FINAL
    # =========================================

    painel = QFrame()

    painel.setLayout(layout_lateral)

    painel.setStyleSheet("""
        background-color: #111;
    """)

    painel.setFixedWidth(250)

    return (
        painel,
        labels_circular,
        labels_livres
    )