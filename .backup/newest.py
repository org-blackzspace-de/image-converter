import os
import sys

import time 
import datetime

import os.path
import pathlib




from PIL import Image

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QProgressBar, QPushButton, QFileDialog, QListWidget, QListWidgetItem, QMessageBox
from PyQt6.QtCore import QTimer
from PyQt6.QtCore import QSize, Qt

from mainui import Ui_MainWindow







class ImageListWidget(QListWidget):
    """Benutzerdefinierte QListWidget-Klasse für Drag & Drop von Bilddateien."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)  # Aktiviert Drag & Drop für das Widget

    def dragEnterEvent(self, event):
        """Wird aufgerufen, wenn eine Datei über das Widget gezogen wird."""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()  # Erlaubt das Drop-Event
        else:
            event.ignore()

    def dropEvent(self, event):
        """Wird aufgerufen, wenn Dateien ins Widget fallen gelassen werden."""
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                # Prüfen, ob die Datei eine gültige Bilddatei ist
                if file_path.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                    self.addItem(QListWidgetItem(file_path))  # Füge Bild zur Liste hinzu
                    self.parent().image_paths.append(file_path)  # Speichere den Pfad in der Liste
            event.acceptProposedAction()
            
            
            


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        # self.load_images_Button.clicked.connect(self.load_images)
        # self.load_images_from_folder_Button.clicked.connect(self.select_folder)
        # self.load_images_Path.mouseDoubleClickEvent = self.open_file_dialog_on_double_click
        # self.load_images_from_folder_Path.mouseDoubleClickEvent = self.open_folder_dialog_on_double_click
        # self.convert_Button.clicked.connect(self.convert_images)
        # # Eigene Methode für das Doppelklick-Ereignis setzen
        # #self.lineEdit.mouseDoubleClickEvent = self.open_file_dialog_on_double_click
        # # Liste für Bildpfade
        # self.image_paths = []
        
              
        
    # def open_file_dialog_on_double_click(self, event):
    #     """Will called, by a double-click on QLineEdit."""
    #     self.load_images()
        
    # def open_folder_dialog_on_double_click(self, event):
    #     """Will called, by a double-click on QLineEdit."""
    #     self.select_folder()
        
        
        
        
        
    # def load_images(self):
    #     """Opens a QFileDialog, to select pictures, and show them in the ListWidget."""
    #     file_dialog = QFileDialog()
    #     files, _ = file_dialog.getOpenFileNames(self, "Select Pictures", "", "Pictures (*.png *.jpg *.jpeg *.bmp *.gif)")

    #     if files:
    #         self.image_paths = files  # Liste speichern
    #         self.listWidget_images_source.clear()  # Liste leeren
    #         for file in files:
    #             self.listWidget_images_source.addItem(QListWidgetItem(file))  # Bilder in Liste einfügen
                
                
             
    
    # def select_folder(self):
    #     """Öffnet einen QFileDialog, um einen Ordner auszuwählen, und fügt gefundene Bilddateien zum listWidget hinzu."""
    #     folder_dialog = QFileDialog(self)
    #     folder_dialog.setFileMode(QFileDialog.FileMode.Directory)  # Nur Ordner auswählen
    #     folder_dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)  # Nur Verzeichnisse anzeigen
    #     folder_dialog.setViewMode(QFileDialog.ViewMode.List)
    #     # Zeigt den Ordnerdialog und gibt den ausgewählten Ordnerpfad zurück
    #     folder_path = folder_dialog.getExistingDirectory(self, "Wählen Sie einen Ordner")
    #     if folder_path:  # Falls ein Ordner ausgewählt wurde
    #         self.image_paths = folder_path
    #         self.listWidget_images_source.clear()  # Liste leeren, bevor neue Dateien hinzugefügt werden
    #         # Erlaubte Bildformate
    #         valid_extensions = {".png", ".jpg", ".jpeg"}
    #         # Alle Dateien im Ordner durchsuchen
    #         for filename in os.listdir(folder_path):
    #             if any(filename.lower().endswith(ext) for ext in valid_extensions):
    #                 # Neuen Listeneintrag erstellen und hinzufügen
    #                 item = QListWidgetItem(os.path.join(folder_path, filename))
                    
    #                 self.listWidget_images_source.addItem(item)

         # Gibt den Ordnerpfad zurück             
             
             
             
             
    # def display_images_in_list(self, files):
    #     """Displays the selected image files in the ListWidget."""
    #     self.listWidget_ico_Output.clear()  # Leere die Liste
    #     for file in files:
    #         # Füge jedes Bild zur ListWidget hinzu
    #         self.listWidget_ico_Output.addItem(QListWidgetItem(file))       
             


    # def get_image_files_from_folder(self, folder_path):
    #     """Scans the folder for image files, excluding .ico files."""
    #     # Alle Dateien im Ordner abfragen
    #     all_files = os.listdir(folder_path)
    #     # Bilddateien filtern, außer .ico
    #     valid_image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')  # Liste der unterstützten Bildformate
    #     image_files = [os.path.join(folder_path, file) for file in all_files if file.lower().endswith(valid_image_extensions) and not file.lower().endswith('.ico')]
    #     return image_files




    # def show_error_message(self, title, message):
    #     """Displays an error message box."""
    #     msg_box = QMessageBox(self)
    #     msg_box.setIcon(QMessageBox.Icon.Critical)
    #     msg_box.setWindowTitle(title)
    #     msg_box.setText(message)
    #     msg_box.exec()
                


    # def convert_images(self):
    #     """Converts selected Images into ICO-Format."""
    #     if not self.image_paths:
    #         return

    #     save_folder = QFileDialog.getExistingDirectory(self, "Zielordner auswählen")
    #     if not save_folder:
    #         return

    #     for image_path in self.image_paths:
    #         try:
    #             img = Image.open(image_path)
    #             filename = os.path.splitext(os.path.basename(image_path))[0] + ".ico"
    #             save_path = os.path.join(save_folder, filename)
    #             img.save(save_path, format="ICO")
    #         except Exception as e:
    #             print(f"Fehler beim Konvertieren von {image_path}: {e}")

    #     print("Konvertierung abgeschlossen!")



        
        
        
        self.load_images_from_folder_Path.mouseDoubleClickEvent = self.load_images_from_folder
        self.load_images_from_folder_Button.clicked.connect(self.load_images_from_folder)
         
        self.load_images_Path.mouseDoubleClickEvent = self.load_images
        self.load_images_Button.clicked.connect(self.load_images)
        
        
        self.convert_Button.clicked.connect(self.convert_images_to_ico)
        
        self.listWidget_images_source.setDragEnabled(True)  # Aktiviert Drag & Drop für das ListWidget



    def load_images_from_folder(self, event=None):
        """Öffnet einen QFileDialog zur Auswahl eines Ordners und lädt alle Bilder (außer .ico) ins ListWidget."""
        folder_path = QFileDialog.getExistingDirectory(self, "Wählen Sie einen Ordner")
        if folder_path:
            self.load_images_from_folder_Path.setText(folder_path)
            self.listWidget_images_source.clear()

            # Erlaubte Bildformate außer ICO
            valid_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".gif"}

            # Bilder aus Ordner filtern und in ListWidget einfügen
            for filename in os.listdir(folder_path):
                if any(filename.lower().endswith(ext) for ext in valid_extensions):
                    self.listWidget_images_source.addItem(os.path.join(folder_path, filename))
                    
                    

    def load_images(self, event=None):
        """Öffnet einen QFileDialog zur Auswahl mehrerer Bilddateien (außer .ico)."""
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Wählen Sie Bilddateien", "", 
                                                     "Bilder (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_paths:
            self.load_images_Path.setText("; ".join(file_paths))
            self.listWidget_images_source.clear()
            self.listWidget_images_source.addItems(file_paths)
            


    def convert_images_to_ico(self):
        """Konvertiert ausgewählte Bilder zu ICO und speichert sie an einem gewählten Speicherort."""
        if self.listWidget_images_source.count() == 0:
            return  # Keine Bilder zum Konvertieren

        # Speicherort für die ICO-Dateien auswählen
        save_folder = QFileDialog.getExistingDirectory(self, "Speicherort für ICOs auswählen")
        if not save_folder:
            return

        self.listWidget_ico_Output.clear()  # Liste leeren

        for i in range(self.listWidget_images_source.count()):
            image_path = self.listWidget_images_source.item(i).text()
            image = Image.open(image_path)

            # Falls kein RGBA-Modus, umwandeln für Transparenz-Unterstützung
            if image.mode != 'RGBA':
                image = image.convert('RGBA')

            # ICO-Dateiname erstellen
            ico_filename = os.path.splitext(os.path.basename(image_path))[0] + ".ico"
            ico_path = os.path.join(save_folder, ico_filename)

            # Konvertierung durchführen
            image.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

            # Zur Liste der konvertierten Dateien hinzufügen
            self.listWidget_ico_Output.addItem(ico_path)
            
            
        
        
        
        
        
  










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())