import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import app
import uuid
import os
import threading


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Crea una instancia del cliente de prueba Flask
        self.app.testing = True  # Habilita el modo de prueba en el cliente

    def test_process_csv_view(self):
        with open("test.csv", "rb") as csv_file:  # Abre el archivo de prueba CSV en modo lectura binaria
            response = self.app.post("/process_csv", data={"csv_file": csv_file})  # Realiza una solicitud POST a la ruta /process_csv con el archivo adjunto
            data = response.get_json()  # Obtiene los datos de la respuesta en formato JSON
            self.assertEqual(response.status_code, 200)  # Verifica que el código de estado de la respuesta sea 200 (éxito)
            self.assertIn("task_id", data)  # Verifica que el campo "task_id" esté presente en los datos de la respuesta

    def test_get_result_view(self):
        response = self.app.get("/get_result/123")  # Realiza una solicitud GET a la ruta /get_result/123
        self.assertEqual(response.status_code, 404)  # Verifica que el código de estado de la respuesta sea 404 (no encontrado)

    def tearDown(self):
        # Eliminar cualquier archivo creado durante las pruebas
        if os.path.exists("uploads/test.csv"):
            os.remove("uploads/test.csv")
        if os.path.exists("results/123.csv"):
            os.remove("results/123.csv")


if __name__ == "__main__":
    unittest.main()