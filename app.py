import sys
from PySide6.QtWidgets import QApplication, QWizard
from wizard.pages import PageEyes
from core.ai_bridge import AIBridge

class CompositeSketchApp(QWizard):
    def __init__(self):
        super().__init__()
        self.addPage(PageEyes())

        self.finished.connect(self.result_process)

    def result_process(self):
        data = {
            "olhos": self.field("formato_olho")
        }
        bridge = AIBridge()
        prompt = bridge.ollama_prompt_generate(data=data)
        bridge.send_to_comfy(prompt)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = CompositeSketchApp()
    window.show()
    sys.exit(app.exe())
