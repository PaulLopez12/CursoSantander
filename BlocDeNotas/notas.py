import tkinter as tk
from tkinter import CASCADE, filedialog, messagebox

class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("600x400")
        #Crear área de texto
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        #Crear menú
        self.crear_menu()
        
    def crear_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        self.config(menu=menubar)
        
    def abrir_archivo(self):
        """Abre un archivo de texto y lo carga en el área de texto"""
        archivo = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, contenido)
                    self.title(f"Editor de Notas - {archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{str(e)}")
    
    def guardar_archivo(self):
        """Guarda el contenido del área de texto en un archivo"""
        archivo = filedialog.asksaveasfilename(
            title="Guardar archivo",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if archivo:
            try:
                contenido = self.text_area.get(1.0, tk.END)
                with open(archivo, 'w', encoding='utf-8') as f:
                    f.write(contenido)
                self.title(f"Editor de Notas - {archivo}")
                messagebox.showinfo("Éxito", "Archivo guardado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")

if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()