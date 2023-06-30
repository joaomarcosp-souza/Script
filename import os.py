import os
import datetime
import getpass


def busca_pasta_arquivo(caminho, data_referencia):
    encontrou_resultado = False 
    usuario_alvo = "Aluno"

    for pasta_raiz, pastas, arquivos in os.walk(caminho):

        for pasta in pastas:
            caminho_pasta = os.path.join(pasta_raiz, pasta)
            data_modificacao = datetime.datetime.fromtimestamp(
                os.path.getmtime(caminho_pasta))
            if data_modificacao >= data_referencia:
                print(
                    f"Pasta encontrada: {caminho_pasta} (Data de modificação: {data_modificacao})")
                encontrou_resultado = True

        for arquivo in arquivos:
            if arquivo.lower().endswith((".pdf", ".exe", ".msi", ".dmg", ".jpg", ".png", ".gif", ".avi", ".mp4", ".mp3", ".doc", ".docx")):
                caminho_arquivo = os.path.join(pasta_raiz, arquivo)

                # Check if the file was modified by the target user
                data_modificacao_arquivo = datetime.datetime.fromtimestamp(
                    os.path.getmtime(caminho_arquivo))
                if data_modificacao_arquivo >= data_referencia and (getpass.getuser() == usuario_alvo or getpass.getuser().lower() == f"{usuario_alvo}@{os.getenv('USERDOMAIN')}"):
                    print(
                        f"Arquivo encontrado: {caminho_arquivo} (Data de modificação: {data_modificacao_arquivo})")
                    encontrou_resultado = True

    if not encontrou_resultado:
        print(
            "Nenhum arquivo, pasta ou instalador encontrado com os critérios especificados.")
# Defina o caminho raiz onde a busca será iniciada
caminho_raiz = "C:"  # Substitua pelo caminho desejado

# Defina a data de referência a partir da qual você deseja buscar os arquivos
data_referencia = datetime.datetime(2023, 1, 1)  # Substitua pela data desejada

busca_pasta_arquivo(caminho_raiz, data_referencia)
