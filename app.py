from flask import Flask, request, jsonify
from csv_processing import process_csv
import uuid
import os
import threading

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULTS_FOLDER = "results"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(RESULTS_FOLDER):
    os.makedirs(RESULTS_FOLDER)

@app.route("/process_csv", methods=["POST"])
def process_csv_view():
    if "csv_file" not in request.files:
        return "No file provided", 400

    file = request.files["csv_file"]
    print(file,"PRINT FILE")
    filename = f"{str(uuid.uuid4())}.csv" ## Genera el ID
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)# gurda el archivo CSV

    thread = threading.Thread(
        target=process_csv,
        args=(file_path, os.path.join(RESULTS_FOLDER, filename)),
    )
    thread.start()

    return {"task_id": filename.split(".")[0]}


@app.route("/get_result/<task_id>", methods=["GET"]) ## Esta ruta permite obtener los resultados del procesamiento del archivo
def get_result_view(task_id):
    filename = f"{task_id}.csv"
    file_path = os.path.join(RESULTS_FOLDER, filename)

    if not os.path.exists(file_path):
        return "File not ready", 404

    with open(file_path, "r") as f:
        csv_data = f.read()

    return jsonify({"csv_data": csv_data})


if __name__ == "__main__":
    app.run(debug=True)
