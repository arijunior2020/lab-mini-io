from flask import Flask, request, jsonify
from flask_cors import CORS
from minio import Minio
from minio.error import S3Error
import os

app = Flask(__name__)
CORS(app)

# Conectar ao MinIO usando variáveis de ambiente
minio_client = Minio(
    os.getenv("MINIO_ENDPOINT", "minio:9000"),
    access_key=os.getenv("MINIO_ACCESS_KEY", "admin"),
    secret_key=os.getenv("MINIO_SECRET_KEY", "password"),
    secure=False
)

# Nome do bucket configurado via variável de ambiente
bucket_name = os.getenv("BUCKET_NAME", "uploads")

# Verificar se o bucket existe, caso contrário criar
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)

# Endpoint para upload de arquivos
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo fornecido"}), 400

    file = request.files['file']
    try:
        # Calcular o tamanho do arquivo
        file.stream.seek(0, os.SEEK_END)
        file_length = file.stream.tell()
        file.stream.seek(0)  # Voltar ao início do arquivo

        minio_client.put_object(
            bucket_name, file.filename, file.stream, length=file_length
        )
        return jsonify({"message": "Upload realizado com sucesso!"}), 200
    except S3Error as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)