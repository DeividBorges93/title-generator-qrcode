# 🧾 Gerador de QR Code com Título

Uma ferramenta simples e eficiente que lê imagens de QR Codes e adiciona automaticamente o **nome da mesa (ou título)** sobre o código, com base no **nome do arquivo**.

Ideal para bares, restaurantes ou eventos que usam QR Code para menus fixos por mesa — evitando erros na hora de colar os códigos impressos.

---

## 🎯 Funcionalidades

- 🖼️ Lê imagens JPEG, JPG e PNG com QR Codes (geradas por outros sistemas)
- 🏷️ Insere automaticamente o título com base no nome do arquivo
- 🗂️ Organiza os arquivos em uma subpasta de saída
- 🖥️ Interface simples e intuitiva (GUI)
- 📦 Geração automática do `.exe` para uso em Windows

---

## 📁 Estrutura esperada dos arquivos

Seu sistema de bar/QR gera imagens como:

/entrada/
├── Mesa_01.jpeg
├── Mesa_02.jpeg
├── Mesa_03.jpeg

O app vai transformar essas imagens em:

/saida/qrcodes_com_titulo/
├── Mesa_01.jpeg ← com o título "Mesa 01" inserido
├── Mesa_02.jpeg
├── Mesa_03.jpeg


---

## 🖥️ Como usar o aplicativo (usuários finais)

1. Faça o download do arquivo [`title-qrcode-generator.exe`](link-para-o-exe) *(adicione o link real aqui após subir)*
2. Extraia o `.zip` (se estiver compactado)
3. Clique duas vezes em `title-qrcode-generator.exe`
4. Selecione:
   - 📂 Pasta com os QR Codes (entrada)
   - 📂 Onde salvar os arquivos com título (saída)
5. Clique em **"Iniciar Processamento"**
6. As imagens com título serão salvas em `qrcodes_com_titulo` dentro da pasta escolhida

> ⚠️ Se aparecer uma mensagem de segurança do Windows, clique em **"Mais Informações" > "Executar mesmo assim"**

---

## 🛠️ Como rodar localmente (desenvolvedores)

### Pré-requisitos:
- Python 3.8+
- Pillow (`pip install pillow`)
- Tkinter (já vem com o Python)

### Executando:

```bash
python qrcode_with_title.py
```
### Compilando .exe (Windows):

```bash
pyinstaller --onefile --windowed --icon=icone_qr.ico qrcode_with_title.py
```
---
## 📄 Licença
Este projeto é gratuito e de código aberto. Fique à vontade para usar, modificar ou contribuir.

## 👨‍💻 Autor
Desenvolvido por Deivid Machado
