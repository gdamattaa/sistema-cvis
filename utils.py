from PySide6.QtGui import QGuiApplication


def centralizar_janela(janela):

    screen = QGuiApplication.primaryScreen()

    screen_geometry = (
        screen.availableGeometry()
    )

    x = (
        screen_geometry.width()
        - janela.width()
    ) // 2

    y = (
        screen_geometry.height()
        - janela.height()
    ) // 2

    janela.move(x, y)