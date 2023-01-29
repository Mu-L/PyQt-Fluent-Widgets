# coding:utf-8
from .config import qconfig
from PyQt6.QtCore import QFile



def getStyleSheet(file):
    """ get style sheet

    Parameters
    ----------
    file: str
        qss file name, without `.qss` suffix
    """
    f = QFile(f":/qfluentwidgets/qss/{qconfig.theme}/{file}.qss")
    f.open(QFile.OpenModeFlag.ReadOnly)
    qss = str(f.readAll(), encoding='utf-8')
    f.close()
    return qss


def setStyleSheet(widget, file):
    """ set the style sheet of widget

    Parameters
    ----------
    widget: QWidget
        the widget to set style sheet

    file: str
        qss file name, without `.qss` suffix
    """
    widget.setStyleSheet(getStyleSheet(file))