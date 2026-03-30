import sys
from PySide6.QtWidgets import QApplication, QWizard
from wizard.pages.page_eyes import PageEyes
from wizard.pages.page_faces import PageFaces
from core.ai_bridge import AIBridge

class CompositeSketchApp(QWizard):
    def __init__(self):
        super().__init__()
        self.addPage(PageFaces())
        self.addPage(PageEyes())
        

        self.finished.connect(self.result_process)

    def result_process(self):
        data = {
            "olhos": self.field("olhos"),
            "rostos": self.field("rostos"),
        }
        bridge = AIBridge()
        prompt = bridge.ollama_prompt_generate(data=data)
        bridge.send_to_comfy(prompt)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = CompositeSketchApp()
    window.show()
    sys.exit(app.exec())
