from PySide6.QtGui import QWheelEvent
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QDialog
import Utils


class ImageDialog(QDialog):
    """
    A class to represent an image dialog.
    """

    def __init__(self, parent, path):
        super().__init__(parent)
        self.setWindowTitle("图可视化")
        layout = QVBoxLayout(self)
        svg_widget = QSvgWidget()
        svg_widget.load(path)
        layout.addWidget(svg_widget)
        self.setLayout(layout)

        self.w, self.h = Utils.get_svg_pixel_dimensions(path)

        # 根据SVG图像的大小设置对话框的大小
        self.setGeometry(100, 100, self.w, self.h)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.angleDelta().y() > 0:
            self.w *= 1.1
            self.h *= 1.1
        else:
            self.w /= 1.1
            self.h /= 1.1

        self.resize(self.w, self.h)
