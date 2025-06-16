import os
from tkinter import Tk, Label, Button, filedialog, messagebox, StringVar, Frame
from PIL import Image, ImageDraw, ImageFont

def processar_imagens(pasta_entrada, pasta_saida):
    os.makedirs(pasta_saida, exist_ok=True)

    try:
        fonte = ImageFont.truetype("arial.ttf", 40)
    except:
        fonte = ImageFont.load_default()

    margem_lateral = 80
    margem_superior = 80
    imagens_processadas = 0

    for nome_arquivo in os.listdir(pasta_entrada):
        if nome_arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
            caminho_imagem = os.path.join(pasta_entrada, nome_arquivo)
            try:
                imagem = Image.open(caminho_imagem)
            except:
                continue

            largura, altura = imagem.size
            nova_largura = largura + 2 * margem_lateral
            nova_altura = altura + margem_superior

            nova_imagem = Image.new("RGB", (nova_largura, nova_altura), "white")
            nova_imagem.paste(imagem, (margem_lateral, margem_superior))

            draw = ImageDraw.Draw(nova_imagem)
            titulo = os.path.splitext(nome_arquivo)[0]
            bbox = fonte.getbbox(titulo)
            texto_largura = bbox[2] - bbox[0]
            pos_x = (nova_largura - texto_largura) // 2
            draw.text((pos_x, 20), titulo, fill="black", font=fonte)

            nova_imagem.save(os.path.join(pasta_saida, nome_arquivo))
            imagens_processadas += 1

    return imagens_processadas

janela = Tk()
janela.title("Gerador de QR Code com Título")
janela.geometry("500x320")
janela.configure(bg="#f2f2f2")

entrada_path = StringVar()
saida_path = StringVar()

def escolher_entrada():
    pasta = filedialog.askdirectory()
    if pasta:
        entrada_path.set(pasta)

def escolher_saida():
    pasta = filedialog.askdirectory()
    if pasta:
        saida_path.set(pasta)

def iniciar_processamento():
    entrada = entrada_path.get()
    saida_base = saida_path.get()

    if not entrada or not saida_base:
        messagebox.showwarning("Aviso", "Selecione a pasta de entrada e de saída.")
        return

    pasta_saida_final = os.path.join(saida_base, "qrcodes_com_titulo")
    os.makedirs(pasta_saida_final, exist_ok=True)

    total = processar_imagens(entrada, pasta_saida_final)
    messagebox.showinfo("Finalizado", f"{total} imagem(s) processada(s) com sucesso!\n\nSalvo em:\n{pasta_saida_final}")

Label(janela, text="Gerador de QR Code com Título", font=("Segoe UI", 16, "bold"), bg="#f2f2f2").pack(pady=15)

# Área de seleção de pastas
frame = Frame(janela, bg="#f2f2f2")
frame.pack(pady=10)

Button(frame, text="📂 Escolher pasta com QR Codes", width=30, command=escolher_entrada).grid(row=0, column=0, padx=5, pady=5)
Label(frame, textvariable=entrada_path, bg="#f2f2f2", wraplength=400, anchor="w", justify="left").grid(row=0, column=1)

Button(frame, text="💾 Escolher pasta de saída", width=30, command=escolher_saida).grid(row=1, column=0, padx=5, pady=5)
Label(frame, textvariable=saida_path, bg="#f2f2f2", wraplength=400, anchor="w", justify="left").grid(row=1, column=1)

# Botão de iniciar
Button(janela, text="🚀 Iniciar Processamento", font=("Segoe UI", 12), bg="#4CAF50", fg="white",
       activebackground="#45A049", padx=20, pady=5, command=iniciar_processamento).pack(pady=20)

Label(janela, text="Escolha as pastas para processar as imagens e gerar QR Codes com título.",
      font=("Segoe UI", 9), bg="#f2f2f2", fg="#555").pack(pady=10)

janela.mainloop()
