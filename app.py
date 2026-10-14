from flask import Flask, render_template_string, jsonify, request

app = Flask(__name__)

# Base de datos simulada de productos para tu proyecto final
productos_db = [
    {
        "id_producto": 1, 
        "name": "Casco AGV K1 S Matte Black", 
        "descripcion": "Casco aerodinámico de alto desempeño con alerón probado en túnel de viento. Certificación ECE 22.06.", 
        "color": "Matte Black", 
        "marca": "AGV", 
        "stock": 12, 
        "precio": 4899,
        "imagen": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id_producto": 2, 
        "name": "Casco Arai Corsair-X Nakagami", 
        "descripcion": "Tecnología de máxima protección para pista y ciudad, con sistema VAS de visera.", 
        "color": "Rojo/Blanco", 
        "marca": "Arai", 
        "stock": 5, 
        "precio": 18200,
        "imagen": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id_producto": 3, 
        "name": "Chamarra Alpinestars GP Plus", 
        "descripcion": "Piel vacuna perforada con protecciones internas homologadas CE en hombros y codos.", 
        "color": "Negro", 
        "marca": "Alpinestars", 
        "stock": 8, 
        "precio": 11400,
        "imagen": "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id_producto": 4, 
        "name": "Guantes Dainese Carbon 4", 
        "descripcion": "Guantes deportivos de piel con inserciones de carbono en nudillos y palma reforzada.", 
        "color": "Negro/Rojo", 
        "marca": "Dainese", 
        "stock": 15, 
        "precio": 4300,
        "imagen": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?auto=format&fit=crop&w=800&q=80"
    }
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

# Interfaz comercial limpia (sin exponer bases de datos al cliente final)
INDEX_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MotoZone - Tienda Oficial de Accesorios</title>
    <style>
        :root { --primary-blue: #0A192F; --accent-blue: #0066FF; --bg-light: #0F172A; --card-bg: #1E293B; --text-light: #F8FAFC; --text-muted: #94A3B8; }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: var(--bg-light); color: var(--text-light); min-height: 100vh; display: flex; flex-direction: column; }
        
        /* Navbar Superior */
        header { background-color: var(--primary-blue); padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; }
        .logo { font-size: 1.5rem; font-weight: bold; color: white; display: flex; align-items: center; gap: 10px; }
        .logo span { color: var(--accent-blue); }
        .nav-links { display: flex; gap: 20px; align-items: center; }
        .nav-links a { color: var(--text-muted); text-decoration: none; font-size: 0.95rem; transition: 0.3s; }
        .nav-links a:hover { color: white; }
        .cart-btn { background: var(--accent-blue); color: white; padding: 8px 16px; border-radius: 6px; font-weight: 600; }

        /* Contenido Principal */
        main { flex: 1; max-width: 1200px; margin: 0 auto; padding: 40px 20px; width: 100%; }
        
        .hero { text-align: center; margin-bottom: 50px; }
        .hero h1 { font-size: 2.5rem; margin-bottom: 15px; color: white; }
        .hero p { color: var(--text-muted); font-size: 1.1rem; max-width: 600px; margin: 0 auto; }

        .section-title { font-size: 1.5rem; margin-bottom: 25px; border-left: 4px solid var(--accent-blue); padding-left: 12px; }

        /* Grid de Productos */
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 25px; }
        .card { background: var(--card-bg); border-radius: 12px; overflow: hidden; border: 1px solid #334155; transition: 0.3s; display: flex; flex-direction: column; position: relative; }
        .card:hover { transform: translateY(-5px); border-color: var(--accent-blue); box-shadow: 0 10px 20px rgba(0, 102, 255, 0.15); }
        
        .badge-brand { position: absolute; top: 12px; left: 12px; background: rgba(10, 25, 47, 0.85); color: #6EA8FE; padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; backdrop-filter: blur(4px); }
        
        .card img { width: 100%; height: 220px; object-fit: cover; background: #000; }
        .card-body { padding: 20px; display: flex; flex-direction: column; flex: 1; justify-content: space-between; }
        
        .card-body h3 { font-size: 1.1rem; margin-bottom: 10px; color: white; }
        .card-body p { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 15px; line-height: 1.4; }
        
        .card-footer { display: flex; justify-content: space-between; align-items: center; margin-top: auto; }
        .price { font-weight: bold; color: #6EA8FE; font-size: 1.2rem; }
        .btn-buy { background: var(--accent-blue); color: white; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; font-weight: 600; transition: 0.2s; }
        .btn-buy:hover { background: #0052cc; }

        footer { text-align: center; padding: 20px; background: var(--primary-blue); color: var(--text-muted); font-size: 0.85rem; border-top: 1px solid #334155; margin-top: 50px; }
    </style>
</head>
<body>
    <header>
        <div class="logo">Moto<span>Zone</span></div>
        <div class="nav-links">
            <a href="#">Catálogo</a>
            <a href="#">Seguridad</a>
            <a href="#">Contacto</a>
            <a href="#" class="cart-btn">🛒 Carrito (0)</a>
        </div>
    </header>

    <main>
        <section class="hero">
            <h1>Seguridad de Élite para Motociclistas</h1>
            <p>Encuentra cascos certificados, chamarras y equipamiento profesional con los más altos estándares internacionales.</p>
        </section>

        <h2 class="section-title">Productos Más Vendidos</h2>
        
        <div class="grid">
            {% for p in productos %}
            <div class="card">
                <span class="badge-brand">{{ p.marca }}</span>
                <img src="{{ p.imagen }}" alt="{{ p.name }}">
                <div class="card-body">
                    <h3>{{ p.name }}</h3>
                    <p>{{ p.descripcion }}</p>
                    <div class="card-footer">
                        <div class="price">${{ "{:,.2f}".format(p.precio) }} MXN</div>
                        <button class="btn-buy" onclick="alert('¡Producto agregado al carrito con éxito!')">Comprar</button>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </main>

    <footer>
        <p>MotoZone Store &copy; 2026 — Proyecto Académico de Ingeniería Web y Base de Datos (Certificación ECE 22.06 & DOT)</p>
    </footer>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
