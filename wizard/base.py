from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QLabel

class BaseWizardpage(QWizardPage):
    def __init__(self, title, instruction):
        super().__init__()
        self.setTitle(title)

        self.layout = QVBoxLayout()
        self.label = QLabel(instruction)
        self.layout.addWidget(self.label)
        self.layout.addStretch()

        self.setLayout(self.layout)

    def add_widget(self, widget):
        self.layout.insertWidget(self.layout.count() -1, widget)

    