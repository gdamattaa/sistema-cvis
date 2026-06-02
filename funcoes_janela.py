from PySide6.QtWidgets import QMessageBox

from funcoes_arquivo import salvar_dados


def confirmar_fechamento(
    event,
    janela,
    tabela,
    campo_obs,
    checkboxes_funcionarios,
    arquivo_atual,
    alterar_arquivo_atual,
    alterar_salvo,
    alteracoes_nao_salvas
):

    if alteracoes_nao_salvas:

        resposta = QMessageBox.question(
            janela,
            "Sair",
            "Existem alterações não salvas.\nDeseja salvar antes de sair?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
            | QMessageBox.StandardButton.Cancel
        )

        if resposta == QMessageBox.StandardButton.Yes:

            salvar_dados(
                janela,
                tabela,
                campo_obs,
                checkboxes_funcionarios,
                arquivo_atual,
                alterar_arquivo_atual,
                alterar_salvo
            )

            event.accept()

        elif resposta == QMessageBox.StandardButton.No:

            event.accept()

        else:

            event.ignore()

    else:

        event.accept()