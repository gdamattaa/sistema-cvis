# =========================================
# IMPORTAÇÕES
# =========================================

from dados import funcionarios

from funcoes_tabela import (
    alternar_funcionario
)

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QVBoxLayout,
    QCheckBox,
    QWidget,
    QFrame,
    QPushButton
)


# =========================================
# PAINEL DE FUNCIONÁRIOS
# =========================================

def criar_painel_funcionarios(
    tabela,
    atualizar_sistema
):

    layout_funcionarios = QVBoxLayout()

    checkboxes_funcionarios = []

    # =====================================
    # BOTÃO EXPANSÍVEL
    # =====================================

    botao_expandir = QPushButton(
        "▼ FUNCIONÁRIOS"
    )

    botao_expandir.setCheckable(True)

    botao_expandir.setChecked(True)

    botao_expandir.setCursor(
        Qt.CursorShape.PointingHandCursor
    )

    botao_expandir.setStyleSheet("""
        QPushButton {
            background-color: #222;
            color: white;
            font-size: 14px;
            font-weight: bold;
            padding: 8px;
            text-align: left;
            border: none;
        }

        QPushButton:hover {
            background-color: #333;
        }
    """)

    layout_funcionarios.addWidget(
        botao_expandir
    )

    # =====================================
    # CONTAINER DOS CHECKBOXES
    # =====================================

    container_funcionarios = QFrame()

    container_funcionarios.setStyleSheet("""
        background-color: #111;
    """)

    layout_container = QVBoxLayout()

    container_funcionarios.setLayout(
        layout_container
    )

    # =====================================
    # CHECKBOXES
    # =====================================

    for indice, funcionario in enumerate(
        funcionarios
    ):

        checkbox = QCheckBox(
            funcionario
        )

        checkbox.setChecked(True)

        checkbox.setStyleSheet("""
            color: white;
            font-size: 14px;
            padding: 5px;
        """)

        coluna_real = indice + 2

        checkbox.toggled.connect(
            lambda estado, c=coluna_real: (
                alternar_funcionario(
                    tabela,
                    c,
                    estado
                ),
                atualizar_sistema()
            )
        )

        checkboxes_funcionarios.append(
            checkbox
        )

        layout_container.addWidget(
            checkbox
        )

    # =====================================
    # EXPANDIR / RECOLHER
    # =====================================

    def alternar_visibilidade():

        visivel = (
            container_funcionarios.isVisible()
        )

        container_funcionarios.setVisible(
            not visivel
        )

        if visivel:

            botao_expandir.setText(
                "▶ FUNCIONÁRIOS"
            )

        else:

            botao_expandir.setText(
                "▼ FUNCIONÁRIOS"
            )

    botao_expandir.clicked.connect(
        alternar_visibilidade
    )

    # =====================================
    # ADICIONAR CONTAINER
    # =====================================

    layout_funcionarios.addWidget(
        container_funcionarios
    )

    # =====================================
    # WIDGET FINAL
    # =====================================

    painel_funcionarios = QWidget()

    painel_funcionarios.setLayout(
        layout_funcionarios
    )

    return (
        painel_funcionarios,
        checkboxes_funcionarios
    )