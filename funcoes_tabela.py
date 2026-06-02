from datetime import datetime

from PySide6.QtGui import QColor

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QTableWidgetItem
)

from estilos import CORES_SERVICOS



# =========================================
# FUNÇÃO DE CORES DOS SERVIÇOS
# =========================================

def atualizar_cor(combo):

    texto = combo.currentText()

    cor_fundo, cor_texto = CORES_SERVICOS.get(
        texto,
        ("white", "black")
    )

    combo.setStyleSheet(f"""
        background-color: {cor_fundo};
        color: {cor_texto};
        font-weight: bold;
        text-align: center;
    """)


# =========================================
# DESTACAR HORÁRIO ATUAL
# =========================================

def destacar_horario_atual(tabela):

    agora_datetime = datetime.now()

    minutos = (agora_datetime.minute // 15) * 15

    agora_ajustado = agora_datetime.replace(
        minute=minutos,
        second=0
    )

    agora = agora_ajustado.strftime("%H:%M")

    for linha in range(tabela.rowCount()):

        item_horario = tabela.item(linha, 0)

        if item_horario:

            horario_tabela = item_horario.text()

            for coluna in range(2):

                item = tabela.item(linha, coluna)

                if item:
                    item.setBackground(
                        Qt.GlobalColor.transparent
                    )

            if horario_tabela == agora:

                for coluna in range(2):

                    item = tabela.item(linha, coluna)

                    if item:

                        item.setBackground(
                            QColor("#ADD8E6")
                        )

                        item.setForeground(
                            QColor("black")
                        )


# =========================================
# ATUALIZAR COLUNA CIRCULAR
# =========================================

def atualizar_circular(tabela):

    for linha in range(tabela.rowCount()):

        responsavel = ""

        for coluna in range(2, tabela.columnCount()):

            combo = tabela.cellWidget(
                linha,
                coluna
            )

            if combo:

                if combo.currentText() == "Circular":

                    nome_funcionario = (
                        tabela.horizontalHeaderItem(
                            coluna
                        ).text()
                    )

                    responsavel = nome_funcionario

        item_circular = QTableWidgetItem(
            responsavel
        )

        item_circular.setTextAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        tabela.setItem(
            linha,
            1,
            item_circular
        )


# =========================================
# ATUALIZAR PAINEL DE PRÓXIMOS CIRCULARES
# =========================================

def atualizar_painel_circular(
    tabela,
    labels_circular
):

    agora_datetime = datetime.now()

    minutos = (
        agora_datetime.minute // 15
    ) * 15

    agora_ajustado = agora_datetime.replace(
        minute=minutos,
        second=0
    )

    agora = agora_ajustado.strftime("%H:%M")

    linha_atual = 0

    for linha in range(tabela.rowCount()):

        item = tabela.item(linha, 0)

        if item and item.text() == agora:

            linha_atual = linha
            break

    for i in range(5):

        linha_tabela = linha_atual + i

        if linha_tabela < tabela.rowCount():

            horario = tabela.item(
                linha_tabela,
                0
            ).text()

            responsavel_item = tabela.item(
                linha_tabela,
                1
            )

            responsavel = ""

            if responsavel_item:
                responsavel = (
                    responsavel_item.text()
                )

            labels_circular[i].setText(
                f"{horario} → {responsavel}"
            )

        else:

            labels_circular[i].setText("")


# =========================================
# MOSTRAR / ESCONDER FUNCIONÁRIOS
# =========================================

def alternar_funcionario(
    tabela,
    coluna,
    estado
):

    esconder = not estado

    tabela.setColumnHidden(
        coluna,
        esconder
    )


# =========================================
# ATUALIZAR FUNCIONÁRIOS LIVRES
# =========================================

def atualizar_funcionarios_livres(
    tabela,
    labels_livres
):

    agora_datetime = datetime.now()

    minutos = (
        agora_datetime.minute // 15
    ) * 15

    agora_ajustado = agora_datetime.replace(
        minute=minutos,
        second=0
    )

    agora = agora_ajustado.strftime("%H:%M")

    linha_atual = None

    for linha in range(tabela.rowCount()):

        item = tabela.item(linha, 0)

        if item and item.text() == agora:

            linha_atual = linha
            break

    livres = []

    if linha_atual is not None:

        for coluna in range(
            2,
            tabela.columnCount()
        ):

            if tabela.isColumnHidden(coluna):
                continue

            combo = tabela.cellWidget(
                linha_atual,
                coluna
            )

            if combo:

                if combo.currentText() == "Livre":

                    nome = (
                        tabela.horizontalHeaderItem(
                            coluna
                        ).text()
                    )

                    livres.append(nome)

    for i in range(len(labels_livres)):

        if i < len(livres):

            labels_livres[i].setText(
                f"✓ {livres[i]}"
            )

        else:

            labels_livres[i].setText("")


# =========================================
# VALIDAR APENAS UM CIRCULAR
# =========================================

def validar_circular(
    tabela,
    linha_atual,
    combo_atual
):

    quantidade_circular = 0

    for coluna in range(
        2,
        tabela.columnCount()
    ):

        combo = tabela.cellWidget(
            linha_atual,
            coluna
        )

        if combo:

            if combo.currentText() == "Circular":

                quantidade_circular += 1

    if quantidade_circular > 1:

        combo_atual.setCurrentText(
            "Livre"
        )


# =========================================
# ATUALIZAÇÕES AUTOMÁTICAS
# =========================================

def atualizar_sistema(
    tabela,
    labels_circular,
    labels_livres
):

    destacar_horario_atual(tabela)

    atualizar_painel_circular(
        tabela,
        labels_circular
    )

    atualizar_funcionarios_livres(
        tabela,
        labels_livres
    )