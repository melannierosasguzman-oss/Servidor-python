from flask import Flask, render_template_string, jsonify, request

app = Flask(__name__)

# Base de datos simulada de productos para tu proyecto final
productos_db = [
    {"id_producto": 1, "name": "AGV K6 S Helmet", "descripcion": "Casco aerodinámico de fibra de vidrio y carbono", "color": "Negro Mate", "marca": "AGV", "stock": 12, "precio": 8500},
    {"id_producto": 2, "name": "Arai Corsair-X", "descripcion": "Casco profesional de alta competición", "color": "Rojo/Blanco", "marca": "Arai", "stock": 5, "precio": 18200},
    {"id_producto": 3, "name": "Alpinestars Leather Jacket", "descripcion": "Chamarra de piel perforada con protecciones CE", "color": "Negro", "marca": "Alpinestars", "stock": 8, "precio": 11400},
    {"id_producto": 4, "name": "Dainese Racing Gloves", "descripcion": "Guantes de piel con refuerzo de titanio en nudillos", "color": "Negro/Rojo", "marca": "Dainese", "stock": 15, "precio": 4300},
    {"id_producto": 5, "name": "Shoei X-Spirit III", "descripcion": "Casco aerodinámico de alta velocidad", "color": "Azul Racing", "marca": "Shoei", "stock": 7, "precio": 16900}
]

@app.route('/')
def home():
    return render_template_string(INDEX_HTML, productos=productos_db)

@app.route('/api/productos', methods=['GET'])
def get_productos():
    return jsonify(productos_db)

@app.route('/api/productos', methods=['POST'])
def add_producto():
    nuevo = request.json
    nuevo["id_producto"] = len(productos_db) + 1
    productos_db.append(nuevo)
    return jsonify({"mensaje": "Producto agregado con éxito", "producto": nuevo}), 201

# Interfaz visual profesional en tonos azules para tu proyecto
INDEX_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MotoZone - Proyecto Final de Semestre</title>
    <style>
        :root { --primary-blue: #0A2540; --accent-blue: #0066FF; --bg-light: #F4F6F8; --text-dark: #333; }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { display: flex; height: 100vh; background-color: var(--bg-light); color: var(--text-dark); overflow: hidden; }
        aside { width: 280px; background-color: var(--primary-blue); color: white; display: flex; flex-direction: column; padding: 20px; box-shadow: 2px 0 5px rgba(0,0,0,0.1); }
        aside h2 { font-size: 1.2rem; margin-bottom: 25px; color: #6EA8FE; }
        aside a { color: #CBD5E1; text-decoration: none; padding: 12px 15px; border-radius: 6px; margin-bottom: 8px; transition: 0.3s; font-size: 0.95rem; }
        aside a:hover { background-color: var(--accent-blue); color: white; }
        main { flex: 1; padding: 30px; overflow-y: auto; }
        header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; border-bottom: 1px solid #ddd; padding-bottom: 15px; }
        h1 { color: var(--primary-blue); font-size: 1.8rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .card { background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: 0.3s; border: 1px solid #e1e4e8; }
        .card:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); }
        .card img { width: 100%; height: 200px; object-fit: cover; }
        .card-body { padding: 15px; }
        .card-body h3 { font-size: 1.1rem; margin-bottom: 8px; color: var(--primary-blue); }
        .card-body p { font-size: 0.9rem; color: #666; margin-bottom: 15px; }
        .price { font-weight: bold; color: var(--accent-blue); font-size: 1.1rem; }
    </style>
</head>
<body>
    <aside>
        <h2>MotoZone Panel</h2>
        <a href="#">Catálogo General</a>
        <a href="#">Gestión de Inventario</a>
        <a href="#">Base de Datos SQL</a>
        <a href="#">Documentación Proyecto</a>
    </aside>
    <main>
        <header>
            <h1>Catálogo de Accesorios y Cascos</h1>
            <span style="background: var(--accent-blue); color: white; padding: 6px 14px; border-radius: 20px; font-size: 0.9rem; font-weight: 600;">Semestre 2026</span>
        </header>
        <div class="grid">
            <div class="card">
                <img src="https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=600&q=80" alt="Casco AGV">
                <div class="card-body">
                    <h3>AGV K6 S Matt Black</h3>
                    <p>Casco aerodinámico de fibra de carbono, homologación ECE 2206.</p>
                    <div class="price">$8,500 MXN</div>
                </div>
            </div>
            <div class="card">
                <img src="https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=600&q=80" alt="Casco Arai">
                <div class="card-body">
                    <h3>Arai Corsair-X Red/White</h3>
                    <p>Tecnología de máxima protección para pista y ciudad.</p>
                    <div class="price">$18,200 MXN</div>
                </div>
            </div>
            <div class="card">
                <img src="https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=600&q=80" alt="Chamarra">
                <div class="card-body">
                    <h3>Alpinestars Leather Jacket</h3>
                    <p>Piel vacuna perforada con protecciones internas en hombros y codos.</p>
                    <div class="price">$11,400 MXN</div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
