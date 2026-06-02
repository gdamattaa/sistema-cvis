from datetime import datetime, timedelta

from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QHeaderView
)

from PySide6.QtGui import QFont

from PySide6.QtCore import Qt

from dados import (
    funcionarios,
    servicos
)

from estilos import ESTILO_TABELA

from funcoes_tabela import (
    atualizar_cor,
    validar_circular
)


def criar_tabela(
    marcar_alterado,
    atualizar_sistema
):

    # =========================================
    # CONFIGURAÇÃO DA TABELA
    # =========================================

    tabela = QTableWidget()

    tabela.setEditTriggers(
        QTableWidget.EditTrigger.NoEditTriggers
    )

    tabela.setStyleSheet(
        ESTILO_TABELA
    )

    fonte = QFont()

    fonte.setPointSize(13)

    tabela.setFont(fonte)

    tabela.verticalHeader().setDefaultSectionSize(40)

    tabela.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeMode.Stretch
    )

    tabela.setColumnCount(
        len(funcionarios) + 2
    )

    cabecalhos = (
        ["Horário", "Circular"]
        + funcionarios
    )

    tabela.setHorizontalHeaderLabels(
        cabecalhos
    )

    # =========================================
    # GERAÇÃO DOS HORÁRIOS
    # =========================================

    dados = []

    hora_atual = datetime.strptime(
        "08:00",
        "%H:%M"
    )

    for i in range(37):

        horario = hora_atual.strftime(
            "%H:%M"
        )

        linha = [horario, ""]

        for funcionario in funcionarios:

            linha.append("Livre")

        dados.append(linha)

        hora_atual += timedelta(
            minutes=15
        )

    tabela.setRowCount(len(dados))

    # =========================================
    # CRIAÇÃO DA TABELA
    # =========================================

    for linha in range(len(dados)):

        for coluna in range(
            len(dados[linha])
        ):

            texto = dados[linha][coluna]

            # =========================================
            # PRIMEIRAS COLUNAS
            # =========================================

            if coluna <= 1:

                item = QTableWidgetItem(
                    texto
                )

                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )

                item.setFlags(
                    item.flags()
                    & ~Qt.ItemFlag.ItemIsEditable
                )

                tabela.setItem(
                    linha,
                    coluna,
                    item
                )

            # =========================================
            # COLUNAS DOS FUNCIONÁRIOS
            # =========================================

            else:

                combo = QComboBox()

                combo.addItems(servicos)

                if texto in servicos:

                    combo.setCurrentText(
                        texto
                    )

                    atualizar_cor(combo)

                combo.currentTextChanged.connect(
                    lambda _, c=combo, l=linha: (
                        marcar_alterado(),
                        validar_circular(
                            tabela,
                            l,
                            c
                        ),
                        atualizar_cor(c),
                        atualizar_sistema()
                    )
                )

                tabela.setCellWidget(
                    linha,
                    coluna,
                    combo
                )

    return tabela