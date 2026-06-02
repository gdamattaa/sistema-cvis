# =========================================
# IMPORTAÇÕES
# =========================================

import sys

from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from funcoes_tabela import (
    destacar_horario_atual,
    atualizar_circular,
    atualizar_painel_circular,
    atualizar_funcionarios_livres
)

from funcoes_arquivo import (
    salvar_dados,
    abrir_dados,
    novo_arquivo
)

from funcoes_janela import (
    confirmar_fechamento
)

from ui_topo import criar_topo
from ui_tabela import criar_tabela
from ui_lateral import criar_painel_lateral
from ui_direita import criar_painel_direita
from ui_funcionarios import criar_painel_funcionarios

from utils import centralizar_janela


# =========================================
# INICIALIZAÇÃO DO APP
# =========================================

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Sistema CVIS")
janela.setWindowIcon(QIcon("icone.ico"))
janela.resize(1200, 600)


# =========================================
# CONTROLE DE ESTADO
# =========================================

arquivo_atual = None
alteracoes_nao_salvas = False


def alterar_arquivo_atual(valor):
    global arquivo_atual
    arquivo_atual = valor


def alterar_salvo(valor):
    global alteracoes_nao_salvas
    alteracoes_nao_salvas = valor


def marcar_alterado():
    global alteracoes_nao_salvas
    alteracoes_nao_salvas = True


# =========================================
# TOPO
# =========================================

(
    layout_topo,
    menu_bar,
    campo_nome_escala,
    campo_data,
    acao_novo,
    acao_abrir,
    acao_salvar,
    acao_salvar_como
) = criar_topo()


# =========================================
# TABELA
# =========================================

def atualizar_sistema():
    destacar_horario_atual(tabela)
    atualizar_circular(tabela)
    atualizar_painel_circular(tabela, labels_circular)
    atualizar_funcionarios_livres(tabela, labels_livres)


tabela = criar_tabela(
    marcar_alterado,
    atualizar_sistema
)


# =========================================
# PAINEL LATERAL
# =========================================

painel, labels_circular, labels_livres = criar_painel_lateral(tabela)


# =========================================
# PAINEL DIREITO
# =========================================

painel_direita, campo_obs = criar_painel_direita()


painel_funcionarios, checkboxes_funcionarios = criar_painel_funcionarios(
    tabela,
    atualizar_sistema
)

layout_painel_direita = painel_direita.layout()
layout_painel_direita.addWidget(painel_funcionarios)


# =========================================
# LAYOUTS
# =========================================

layout_principal = QHBoxLayout()
layout_geral = QVBoxLayout()
layout_tabela = QVBoxLayout()


layout_tabela.addLayout(layout_topo)
layout_tabela.addWidget(tabela)

layout_principal.addWidget(painel)
layout_principal.addLayout(layout_tabela)
layout_principal.addWidget(painel_direita)

layout_geral.setMenuBar(menu_bar)
layout_geral.addLayout(layout_principal)

janela.setLayout(layout_geral)


# =========================================
# INICIALIZAÇÃO
# =========================================

atualizar_sistema()


# =========================================
# TIMER
# =========================================

timer = QTimer()
timer.timeout.connect(atualizar_sistema)
timer.start(30000)


# =========================================
# CENTRALIZAR
# =========================================

centralizar_janela(janela)


# =========================================
# AÇÕES MENU
# =========================================

acao_novo.triggered.connect(
    lambda: novo_arquivo(
        janela,
        tabela,
        campo_obs,
        alterar_arquivo_atual
    )
)

acao_salvar.triggered.connect(
    lambda: salvar_dados(
        janela,
        tabela,
        campo_obs,
        checkboxes_funcionarios,
        arquivo_atual,
        alterar_arquivo_atual,
        alterar_salvo,
        salvar_como=False
    )
)

acao_salvar_como.triggered.connect(
    lambda: salvar_dados(
        janela,
        tabela,
        campo_obs,
        checkboxes_funcionarios,
        arquivo_atual,
        alterar_arquivo_atual,
        alterar_salvo,
        salvar_como=True
    )
)

acao_abrir.triggered.connect(
    lambda: abrir_dados(
        janela,
        tabela,
        campo_obs,
        checkboxes_funcionarios,
        labels_circular,
        labels_livres,
        alterar_arquivo_atual
    )
)


# =========================================
# FECHAMENTO CORRIGIDO
# =========================================

def close_event(event):
    confirmar_fechamento(
        event,
        janela,
        tabela,
        campo_obs,
        checkboxes_funcionarios,
        arquivo_atual,
        alterar_arquivo_atual,
        alterar_salvo,
        alteracoes_nao_salvas
    )

janela.closeEvent = close_event


# =========================================
# EXECUÇÃO
# =========================================

janela.show()
app.exec()