import tkinter as tk
from time import strftime

# Definição da função para atualizar o tempo no Label


def time():
    # Formata a hora atual como 'HH:MM:SS AM/PM'
    string = strftime('%H:%M:%S %p')
    # Atualiza o texto do Label com a hora formatada
    label.config(text=string)
    # Agenda a função time para ser chamada novamente após 1000ms (1 segundo)
    label.after(1000, time)


# Criação da janela principal da aplicação tkinter
janela = tk.Tk()
# Define o título da janela como 'Relógio Digital'
janela.title('Relógio Digital')
# Define as dimensões da janela como 500 pixels de largura por 100 pixels de altura
janela.geometry('500x100')

# Criação do Label para exibir o tempo
label = tk.Label(janela, font=('calibri', 40, 'bold'),
                 background='black', foreground='white')
label.pack(anchor='center')          # Posiciona o Label no centro da janela

# Inicia a atualização contínua do tempo chamando a função time
time()

# Inicia o loop principal da aplicação tkinter
janela.mainloop()
