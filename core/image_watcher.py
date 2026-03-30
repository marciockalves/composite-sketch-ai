import os
from PySide6.QtCore import QObject, Signal, QFileSystemWatcher

class ImageWatcher(QObject):
    image_generated = Signal(str)

    def __init__(self, output_dir):
        super().__init__()
        self.output_dir = output_dir

        self.watcher = QFileSystemWatcher()
        self.watcher.addPath(self.output_dir)

        self.watcher.directoryChanged.connect(self._check_new_image)
        self.know_files = set(os.listdir(self.output_dir))

    def _check_new_image(self, path):
        current_files = set(os.listdir(self.output_dir))
        new_files = current_files - self.know_files

        if new_files:
            new_file = list(new_files)[0]
            full_path = os.path.join(self.output_dir, new_file)

            self.know_files = current_files
            self.image_generated.emit(full_path)
