import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('Agg')

taxa_anual = 0.1415
taxa_diaria = (1 + taxa_anual) ** (1 / 365) - 1

def obter_aliquota_iof(dias):
    if dias <= 0: return 1.0
    elif dias == 1: return 0.96
    elif dias == 2: return 0.93
    elif dias == 3: return 0.90
    elif dias == 4: return 0.86
    elif dias == 5: return 0.83
    elif dias == 6: return 0.80
    elif dias == 7: return 0.76
    elif dias == 8: return 0.73
    elif dias == 9: return 0.70
    elif dias == 10: return 0.66
    elif dias == 11: return 0.63
    elif dias == 12: return 0.60
    elif dias == 13: return 0.56
    elif dias == 14: return 0.53
    elif dias == 15: return 0.50
    elif dias == 16: return 0.46
    elif dias == 17: return 0.43
    elif dias == 18: return 0.40
    elif dias == 19: return 0.36
    elif dias == 20: return 0.33
    elif dias == 21: return 0.30
    elif dias == 22: return 0.26
    elif dias == 23: return 0.23
    elif dias == 24: return 0.20
    elif dias == 25: return 0.16
    elif dias == 26: return 0.13
    elif dias == 27: return 0.10
    elif dias == 28: return 0.06
    elif dias == 29: return 0.03
    else: return 0.0

def obter_aliquota_ir(dias):
    if dias <= 180:
        return 0.225
    elif dias <= 360:
        return 0.20
    elif dias <= 720:
        return 0.175
    else:
        return 0.15

def calcular():
    try:
        valor_inicial = float(entry_valor.get())
        dias = int(entry_dias.get())

        rendimento_bruto = valor_inicial * ((1 + taxa_diaria) ** dias - 1)
        valor_total = valor_inicial + rendimento_bruto

        aliquota_iof = obter_aliquota_iof(dias)
        iof = rendimento_bruto * aliquota_iof

        rendimento_liquido_iof = rendimento_bruto - iof
        aliquota_ir = obter_aliquota_ir(dias)
        ir = rendimento_liquido_iof * aliquota_ir

        valor_liquido = valor_inicial + rendimento_bruto - iof - ir

        resultado_texto = (
            f"Valor Inicial: R$ {valor_inicial:,.2f}\n"
            f"Rendimento Bruto: R$ {rendimento_bruto:,.2f}\n"
            f"Desconto IOF: R$ {iof:,.2f} (Alíquota: {aliquota_iof*100:.1f}%)\n"
            f"Desconto IR: R$ {ir:,.2f} (Alíquota: {aliquota_ir*100:.1f}%)\n"
            f"Valor Final Líquido: R$ {valor_liquido:,.2f}"
        )
        resultado_label.config(text=resultado_texto)

        dias_lista = list(range(1, dias + 1))
        montantes = [valor_inicial * ((1 + taxa_diaria) ** d) for d in dias_lista]

        fig.clear()
        ax = fig.add_subplot(111)
        ax.plot(dias_lista, montantes, color='green', label='Valor acumulado (R$)')
        ax.set_title("Evolução do Investimento", fontsize=12)
        ax.set_xlabel("Dias", labelpad=10)
        ax.set_ylabel("Montante (R$)", labelpad=10)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        fig.tight_layout()
        canvas.draw()

    except ValueError:
        resultado_label.config(text="Insira valores válidos.")

root = tk.Tk()
root.title("Simulador de Investimento - Caixinha Super Cofrinho")
root.configure(bg='white')

style = ttk.Style()
style.configure('TLabel', background='white', font=('Segoe UI', 10))
style.configure('TButton', font=('Segoe UI', 10, 'bold'), foreground='white')
style.configure('TEntry', padding=6)

frame = ttk.Frame(root, padding="30 20 30 20")
frame.pack(pady=10)

ttk.Label(frame, text="Valor Inicial (R$):").grid(column=0, row=0, sticky='W', padx=5, pady=5)
entry_valor = ttk.Entry(frame, width=25)
entry_valor.grid(column=1, row=0, pady=5)

ttk.Label(frame, text="Número de Dias:").grid(column=0, row=1, sticky='W', padx=5, pady=5)
entry_dias = ttk.Entry(frame, width=25)
entry_dias.grid(column=1, row=1, pady=5)

botao = tk.Button(frame, text="Calcular 💰", command=calcular,
                  bg="green", fg="white", font=("Segoe UI", 10, "bold"),
                  relief='flat', padx=12, pady=6)
botao.grid(column=0, row=2, columnspan=2, pady=10)

resultado_label = ttk.Label(root, text="", background='white', font=("Segoe UI", 10))
resultado_label.pack(pady=10)

fig = plt.Figure(figsize=(6.5, 3.2), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=10)

root.mainloop()
