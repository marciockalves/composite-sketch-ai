from wizard.base import BaseWizardpage
from PySide6.QtWidgets import QRadioButton

class PageFaces(BaseWizardpage):
    def __init__(self):
        super().__init__("Formato do Rosto", "Selecione o formato predominante:")
        
        self.rb1 =QRadioButton("Redondo")
        self.rb2 =QRadioButton("Quadrado")
        self.rb3 =QRadioButton("Afilado")

        self.add_widget(self.rb1)
        self.add_widget(self.rb2)
        self.add_widget(self.rb3)

        self.registerField("rostos", self.rb1)