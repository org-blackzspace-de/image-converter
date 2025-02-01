self.load_images_from_folder_Button.clicked.connect(self.load_images_from_folder)
        self.load_images_from_folder_Path.mouseDoubleClickEvent = self.load_images_from_folder
        self.load_images_Button.clicked.connect(self.load_images)
        self.load_images_Path.mouseDoubleClickEvent = self.load_images
        self.convert_Button.clicked.connect(self.convert_images_to_ico)

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