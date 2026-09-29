import datetime
import random
import tkinter as tk
from tkinter import messagebox

# --- Lista de productos definidos (Tecnologia) ---
PRODUCTOS = {
    "Laptop Gamer 15.6": 18500.00,
    "Teclado Mecanico RGB": 1250.00,
    "Mouse Inalambrico Ergonomico": 450.00,
    "Monitor Curvo 24 pulgadas": 3800.00,
    "Audifonos Gamer con Microfono": 890.00,
    "Disco Duro Solido SSD 1TB": 1400.00,
}


class PuntoDeVentaApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Punto de Venta - Tecnologia")
        self.root.geometry("650x650")
        self.root.config(bg="#1e1e2f")
        self.root.resizable(False, False)

        self.folio_actual = f"FAC-{random.randint(1000, 9999)}"
        self.fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.root,
            text="SISTEMA PUNTO DE VENTA - TECNOLOGIA",
            font=("Arial", 16, "bold"),
            bg="#1e1e2f",
            fg="#00ffcc",
        )
        titulo.pack(pady=15)

        frame_form = tk.Frame(self.root, bg="#2d2d44", bd=2, relief="groove")
        frame_form.pack(padx=20, pady=10, fill="both", expand=True)

        tk.Label(
            frame_form,
            text="Folio de Venta:",
            font=("Arial", 10, "bold"),
            bg="#2d2d44",
            fg="white",
        ).grid(row=0, column=0, sticky="w", padx=15, pady=10)
        self.lbl_folio = tk.Label(
            frame_form,
            text=self.folio_actual,
            font=("Arial", 10, "bold"),
            bg="#2d2d44",
            fg="#ffcc00",
        )
        self.lbl_folio.grid(row=0, column=1, sticky="w", padx=15, pady=10)

        tk.Label(
            frame_form,
            text="Fecha y Hora:",
            font=("Arial", 10, "bold"),
            bg="#2d2d44",
            fg="white",
        ).grid(row=1, column=0, sticky="w", padx=15, pady=10)
        self.lbl_fecha = tk.Label(
            frame_form,
            text=self.fecha_actual,
            font=("Arial", 10),
            bg="#2d2d44",
            fg="white",
        )
        self.lbl_fecha.grid(row=1, column=1, sticky="w", padx=15, pady=10)

        tk.Label(
            frame_form,
            text="Usuario de Venta:",
            font=("Arial", 10, "bold"),
            bg="#2d2d44",
            fg="white",
        ).grid(row=2, column=0, sticky="w", padx=15, pady=10)
        self.txt_usuario = tk.Entry(
            frame_form, font=("Arial", 10), width=25, bg="#ffffff", fg="#000000"
        )
        self.txt_usuario.insert(0, "Jesus Corzo")
        self.txt_usuario.grid(row=2, column=1, sticky="w", padx=15, pady=10)

        tk.Label(
            frame_form,
            text="Nombre del Cliente:",
            font=("Arial", 10, "bold"),
            bg="#2d2d44",
            fg="white",
        ).grid(row=3, column=0, sticky="w", padx=15, pady=10)
        self.txt_cliente = tk.Entry(
            frame_form, font=("Arial", 10), width=25, bg="#ffffff", fg="#000000"
        )
        self.txt_cliente.grid(row=3, column=1, sticky="w", padx=15, pady=10)

        tk.Label(
            frame_form,
            text="Seleccione Producto:",
            font=("Arial", 10, "bold"),
            bg="#2d2d44",
            fg="white",
        ).grid(row=4, column=0, sticky="w", padx=15, pady=10)
        self.producto_seleccionado = tk.StringVar(value=list(PRODUCTOS.keys())[0])
        self.dropdown_productos = tk.OptionMenu(
            frame_form, self.producto_seleccionado, *PRODUCTOS.keys()
        )
        self.dropdown_productos.config(
            font=("Arial", 9), width=28, bg="#ffffff", fg="#000000"
        )
        self.dropdown_productos.grid(row=4, column=1, sticky="w", padx=15, pady=10)

        tk.Label(
            frame_form,
            text="Cantidad:",
            font=("Arial", 10, "bold"),
            bg="#2d2d44",
            fg="white",
        ).grid(row=5, column=0, sticky="w", padx=15, pady=10)
        self.txt_cantidad = tk.Entry(
            frame_form, font=("Arial", 10), width=10, bg="#ffffff", fg="#000000"
        )
        self.txt_cantidad.insert(0, "1")
        self.txt_cantidad.grid(row=5, column=1, sticky="w", padx=15, pady=10)

        frame_botones = tk.Frame(self.root, bg="#1e1e2f")
        frame_botones.pack(pady=15)

        btn_guardar = tk.Button(
            frame_botones,
            text="Guardar Venta",
            command=self.guardar_venta,
            font=("Arial", 10, "bold"),
            bg="#28a745",
            fg="white",
            width=15,
            relief="raised",
        )
        btn_guardar.grid(row=0, column=0, padx=10)

        btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar Campos",
            command=self.limpiar_campos,
            font=("Arial", 10, "bold"),
            bg="#dc3545",
            fg="white",
            width=15,
            relief="raised",
        )
        btn_limpiar.grid(row=0, column=1, padx=10)

    def limpiar_campos(self):
        self.txt_cliente.delete(0, tk.END)
        self.txt_cantidad.delete(0, tk.END)
        self.txt_cantidad.insert(0, "1")
        self.producto_seleccionado.set(list(PRODUCTOS.keys())[0])
        self.folio_actual = f"FAC-{random.randint(1000, 9999)}"
        self.lbl_folio.config(text=self.folio_actual)
        messagebox.showinfo(
            "Limpiar", "Los campos del formulario han sido limpiados."
        )

    def guardar_venta(self):
        cliente = self.txt_cliente.get().strip()
        usuario = self.txt_usuario.get().strip()
        cantidad_str = self.txt_cantidad.get().strip()

        if not cliente:
            messagebox.showerror(
                "Error", "El nombre del cliente es obligatorio."
            )
            return

        if not cantidad_str.isdigit() or int(cantidad_str) <= 0:
            messagebox.showerror(
                "Error", "Ingrese una cantidad valida mayor a 0."
            )
            return

        cantidad = int(cantidad_str)
        producto = self.producto_seleccionado.get()
        precio_unitario = PRODUCTOS[producto]

        subtotal = precio_unitario * cantidad
        iva = subtotal * 0.16
        total = subtotal + iva

        nombre_archivo = f"{self.folio_actual}.txt"

        contenido_ticket = f"""========================================
         PUNTO DE VENTA - TECNOLOGIA
========================================
Folio de Venta : {self.folio_actual}
Fecha y Hora   : {self.fecha_actual}
Usuario Venta  : {usuario}
Cliente        : {cliente}
----------------------------------------
PRODUCTO       : {producto}
Precio Unitario: ${precio_unitario:,.2f}
Cantidad       : {cantidad}
----------------------------------------
Subtotal       : ${subtotal:,.2f}
IVA (16%)      : ${iva:,.2f}
TOTAL A PAGAR  : ${total:,.2f}
========================================
Gracias por su preferencia!
"""

        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(contenido_ticket)

            messagebox.showinfo(
                "Exito",
                f"Venta guardada correctamente.\nArchivo generado: {nombre_archivo}",
            )
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror(
                "Error", f"No se pudo guardar el archivo: {str(e)}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = PuntoDeVentaApp(root)
    root.mainloop()