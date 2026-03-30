from wizard.base import BaseWizardpage
from PySide6.QtWidgets import QRadioButton

class PageEyes(BaseWizardpage):
    def __init__(self):
        super().__init__("Definição dos Olhos", "Selecione o fomrato dos olhos:")
        
        self.rb1 =QRadioButton("Grandes")
        self.rb2 =QRadioButton("Amendoados")
        self.rb3 =QRadioButton("Profundos")

        self.add_widget(self.rb1)
        self.add_widget(self.rb2)
        self.add_widget(self.rb3)

        self.registerField("olhos", self.rb1)