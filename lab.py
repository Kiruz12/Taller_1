import tkinter as tk
from tkinter import filedialog, messagebox

# Modelo de mapa
class TileMap:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.layers = {
            "background": [[0 for _ in range(width)] for _ in range(height)],
            "objects": [[None for _ in range(width)] for _ in range(height)],
            "collision": [[False for _ in range(width)] for _ in range(height)],
        }
        self.spawn_points = []

    # Métodos para modificar el mapa, guardar/cargar, etc.

# Vista principal
class MapEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Mapas Tile-Based")
        self.geometry("1200x800")
        # Aquí se agregarán los paneles y el lienzo

        # Ejemplo de inicialización de mapa
        self.map = TileMap(width=20, height=15, tile_size=32)

        # Métodos para crear la interfaz gráfica

if __name__ == "__main__":
    app = MapEditor()
    app.mainloop()

        self.create_widgets()
    def create_widgets(self):
        # Panel de herramientas
        self.toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.save_button = tk.Button(self.toolbar, text="Guardar", command=self.save_map)
        self.save_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.load_button = tk.Button(self.toolbar, text="Cargar", command=self.load_map)
        self.load_button.pack(side=tk.LEFT, padx=2, pady=2)

        # Lienzo para el mapa
        self.canvas = tk.Canvas(self, bg="white", width=640, height=480)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Panel de propiedades
        self.properties_panel = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.properties_panel.pack(side=tk.RIGHT, fill=tk.Y)

        self.tile_label = tk.Label(self.properties_panel, text="Tile:")
        self.tile_label.pack(pady=10)

        self.tile_entry = tk.Entry(self.properties_panel)
        self.tile_entry.pack(pady=10)
        self.tile_entry.insert(0, "0")
    def save_map(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".map", filetypes=[("Map Files", "*.map")])
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    # Guardar el mapa en el archivo
                    f.write(str(self.map.layers))
                messagebox.showinfo("Guardar Mapa", "Mapa guardado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el mapa: {e}")
    def load_map(self):
        file_path = filedialog.askopenfilename(defaultextension=".map", filetypes=[("Map Files", "*.map")])
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    # Cargar el mapa desde el archivo
                    layers = eval(f.read())
                    self.map.layers = layers
                messagebox.showinfo("Cargar Mapa", "Mapa cargado exitosamente.")
                self.redraw_map()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el mapa: {e}")
    def redraw_map(self):
        self.canvas.delete("all")
        for y in range(self.map.height):
            for x in range(self.map.width):
                tile = self.map.layers["background"][y][x]
                color = "lightgrey" if tile == 0 else "darkgrey"
                self.canvas.create_rectangle(
                    x * self.map.tile_size, y * self.map.tile_size,
                    (x + 1) * self.map.tile_size, (y + 1) * self.map.tile_size,
                    fill=color, outline="black"
                )
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.create_widgets()
        