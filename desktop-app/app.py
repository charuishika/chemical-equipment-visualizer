import sys
import requests
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLabel, QFileDialog, QVBoxLayout, QMessageBox
)


class EquipmentApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Visualizer")
        self.setGeometry(300, 200, 420, 220)

        layout = QVBoxLayout()

        self.label = QLabel("Upload a CSV file to analyze equipment.")
        layout.addWidget(self.label)

        upload_btn = QPushButton("Select CSV & Analyze")
        upload_btn.clicked.connect(self.upload_csv)
        layout.addWidget(upload_btn)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    # ⭐⭐⭐ MAIN FUNCTION
    def upload_csv(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select CSV File",
            "",
            "CSV Files (*.csv)"
        )

        if not file_path:
            return

        url = "http://127.0.0.1:8000/api/upload/"

        try:
            # ⭐ VERY IMPORTANT → use WITH (auto closes file)
            with open(file_path, 'rb') as f:

                response = requests.post(
                    url,
                    files={'file': f},
                    timeout=10
                )

            # ⭐ Show real error if backend fails
            if response.status_code != 200:
                QMessageBox.critical(
                    self,
                    "Upload Failed",
                    f"Server Error:\n{response.text}"
                )
                return

            data = response.json()

            self.result_label.setText(
                f"Total Equipment: {data['total_equipment']}\n"
                f"Avg Pressure: {data['avg_pressure']}\n"
                f"Avg Temperature: {data['avg_temperature']}"
            )

            self.show_chart(data['type_distribution'])

        except requests.exceptions.ConnectionError:
            QMessageBox.critical(
                self,
                "Connection Error",
                "Cannot connect to Django server.\n\nIs it running?"
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )
            print(e)

    # ⭐ CHART
    def show_chart(self, distribution):

        labels = list(distribution.keys())
        sizes = list(distribution.values())

        plt.figure(figsize=(6, 6))

        plt.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90
        )

        plt.title("Equipment Type Distribution")
        plt.tight_layout()
        plt.show()


# ⭐ APP START
app = QApplication(sys.argv)
window = EquipmentApp()
window.show()
sys.exit(app.exec_())
