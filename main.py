import boto3
import json

# Nome do arquivo da imagem
image_path = "imagens/lista-material-escolar.jpeg"

# Cliente do AWS Textract
client = boto3.client("textract")

# Carregar a imagem
with open(image_path, "rb") as image_file:
    image_bytes = image_file.read()

# Chamar o Textract
response = client.detect_document_text(Document={"Bytes": image_bytes})

# Salvar a resposta em response.json
with open("response.json", "w", encoding="utf-8") as f:
    json.dump(response, f, ensure_ascii=False, indent=4)

# Extrair e exibir o texto detectado
print("\nTexto extraído:")
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print(item["Text"])
