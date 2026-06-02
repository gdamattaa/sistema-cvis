import json

from PySide6.QtWidgets import (
    QFileDialog,
    QMessageBox
)

from funcoes_tabela import (
    atualizar_cor,
    atualizar_circular,
    atualizar_painel_circular,
    atualizar_funcionarios_livres
)

from dados import funcionarios


# =========================================
# SALVAR DADOS
# =========================================

def salvar_dados(
    janela,
    tabela,
    campo_obs,
    checkboxes_funcionarios,
    arquivo_atual,
    alterar_arquivo_atual,
    alterar_salvo,
    salvar_como=False,
    mostrar_popup=True
):

    if salvar_como or not arquivo_atual:

        caminho_arquivo, _ = QFileDialog.getSaveFileName(
            janela,
            "Salvar escala",
            "",
            "Arquivos JSON (*.json)"
        )

        if not caminho_arquivo:
            return

        alterar_arquivo_atual(
            caminho_arquivo
        )

        arquivo_atual = caminho_arquivo

    dados_salvos = {
        "observacoes": campo_obs.toPlainText(),
        "funcionarios_ativos": [],
        "tabela": {}
    }

    for indice in range(len(funcionarios)):

        checkbox = checkboxes_funcionarios[indice]

        if checkbox.isChecked():

            dados_salvos[
                "funcionarios_ativos"
            ].append(
                funcionarios[indice]
            )

    for linha in range(tabela.rowCount()):

        horario = tabela.item(
            linha,
            0
        ).text()

        dados_salvos["tabela"][
            horario
        ] = {}

        for coluna in range(
            2,
            tabela.columnCount()
        ):

            nome = tabela.horizontalHeaderItem(
                coluna
            ).text()

            combo = tabela.cellWidget(
                linha,
                coluna
            )

            if combo:

                dados_salvos["tabela"][
                    horario
                ][nome] = combo.currentText()

    with open(
        arquivo_atual,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            dados_salvos,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

    alterar_salvo(False)

    if mostrar_popup:

        QMessageBox.information(
            janela,
            "Salvo",
            "Escala salva com sucesso!"
        )


# =========================================
# NOVO ARQUIVO
# =========================================

def novo_arquivo(
    janela,
    tabela,
    campo_obs,
    alterar_arquivo_atual
):

    resposta = QMessageBox.question(
        janela,
        "Novo",
        "Deseja limpar a escala atual?"
    )

    if resposta == QMessageBox.StandardButton.Yes:

        for linha in range(tabela.rowCount()):

            for coluna in range(
                2,
                tabela.columnCount()
            ):

                combo = tabela.cellWidget(
                    linha,
                    coluna
                )

                if combo:

                    combo.setCurrentText(
                        "Livre"
                    )

        campo_obs.clear()

        alterar_arquivo_atual(None)


# =========================================
# ABRIR DADOS
# =========================================

def abrir_dados(
    janela,
    tabela,
    campo_obs,
    checkboxes_funcionarios,
    labels_circular,
    labels_livres,
    alterar_arquivo_atual
):

    caminho_arquivo, _ = QFileDialog.getOpenFileName(
        janela,
        "Abrir escala",
        "",
        "Arquivos JSON (*.json)"
    )

    if not caminho_arquivo:
        return

    alterar_arquivo_atual(
        caminho_arquivo
    )

    try:

        with open(
            caminho_arquivo,
            "r",
            encoding="utf-8"
        ) as arquivo:

            dados_salvos = json.load(
                arquivo
            )

        campo_obs.setText(
            dados_salvos.get(
                "observacoes",
                ""
            )
        )

        ativos = dados_salvos.get(
            "funcionarios_ativos",
            []
        )

        for indice, checkbox in enumerate(
            checkboxes_funcionarios
        ):

            nome = funcionarios[indice]

            checkbox.setChecked(
                nome in ativos
            )

        tabela_salva = dados_salvos.get(
            "tabela",
            {}
        )

        for linha in range(
            tabela.rowCount()
        ):

            horario = tabela.item(
                linha,
                0
            ).text()

            if horario in tabela_salva:

                for coluna in range(
                    2,
                    tabela.columnCount()
                ):

                    nome = tabela.horizontalHeaderItem(
                        coluna
                    ).text()

                    valor = tabela_salva[
                        horario
                    ].get(
                        nome,
                        "Livre"
                    )

                    combo = tabela.cellWidget(
                        linha,
                        coluna
                    )

                    if combo:

                        combo.setCurrentText(
                            valor
                        )

                        atualizar_cor(combo)

        atualizar_circular(
            tabela
        )

        atualizar_painel_circular(
            tabela,
            labels_circular
        )

        atualizar_funcionarios_livres(
            tabela,
            labels_livres
        )

    except Exception as erro:

        QMessageBox.warning(
            janela,
            "Erro",
            f"Erro ao abrir arquivo:\n{erro}"
        )