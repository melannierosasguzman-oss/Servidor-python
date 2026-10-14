from flask import Flask, render_template_string, jsonify, request

app = Flask(__name__)

# Base de datos simulada con productos reales de motociclismo
productos_db = [
    {
        "id_producto": 1, 
        "name": "Casco AGV K1 S Matte gris", 
        "categoria": "CASCOS",
        "marca": "AGV",
        "badge": "MATTE BLACK",
        "estrellas": "4.9",
        "descripcion": "Casco aerodinámico de alto desempeño con alerón probado en túnel de viento. Certificación ECE 22.06 y visor panorámico.", 
        "precio": 4899,
        "imagen": "https://th.bing.com/th/id/R.c9e70af783bdf11c18122e15c49b8d87?rik=vhblqJZlwp7PWw&riu=http%3a%2f%2fmoterosperu.com%2fwp-content%2fuploads%2f2021%2f06%2fcascos-AGV-2.jpg&ehk=PnyMdYgfs4%2f8nZHQMsvtovJLsGP8%2b%2fssKnay6rlJffU%3d&risl=&pid=ImgRaw&r=0"
    },
    {
        "id_producto": 2, 
        "name": "Casco Arai #0101-15938 Corsair-X - Negro", 
        "categoria": "CASCOS",
        "marca": "ARAI",
        "badge": "RACING",
        "estrellas": "5.0",
        "descripcion": "Tecnología de máxima protección para pista y ciudad, con sistema VAS de visera y ventilación de competencia.", 
        "precio": 18200,
        "imagen": "https://http2.mlstatic.com/D_NQ_NP_671555-MLA89724160746_082025-O.webp"
    },
    {
        "id_producto": 3, 
        "name": "Chamarra Alpinestars GP Plus", 
        "categoria": "EQUIPAMIENTO",
        "marca": "ALPINESTARS",
        "badge": "PIEL CE",
        "estrellas": "4.8",
        "descripcion": "Piel vacuna perforada con protecciones internas homologadas CE en hombros y codos para máxima seguridad.", 
        "precio": 11400,
        "imagen": "https://bosico.vtexassets.com/arquivos/ids/2125148/Chaqueta-CQ91NR-NGxRJ_2.jpg?v=638838966789500000"
    },
    {
        "id_producto": 4, 
        "name": "Guantes Dainese Carbon 4", 
        "categoria": "ACCESORIOS",
        "marca": "DAINESE",
        "badge": "CARBONO",
        "estrellas": "4.7",
        "descripcion": "Guantes deportivos de piel con inserciones de carbono en nudillos y palma reforzada para agarre superior.", 
        "precio": 4300,
        "imagen": "https://www.canariasenmoto.com/images/varias/Seventy_Degrees_Guantes_(1).jpg"
    }
]

@app.route('/')
def home():
    return render_template_string(INDEX_HTML, productos=productos_db)

@app.route('/api/productos', methods=['GET'])
def get_productos():
    return jsonify(productos_db)

# Interfaz visual profesional recuperada (limpia, funcional y atractiva)
INDEX_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MotoZone - Tienda Oficial de Accesorios</title>
    <style>
        :root { --primary-blue: #0A192F; --accent-blue: #0066FF; --bg-dark: #070D1B; --card-bg: #111E38; --text-light: #F8FAFC; --text-muted: #94A3B8; }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: var(--bg-dark); color: var(--text-light); min-height: 100vh; display: flex; flex-direction: column; }
        
        /* Navbar Superior */
        header { background-color: var(--primary-blue); padding: 18px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1E293B; position: sticky; top: 0; z-index: 100; }
        .logo-container { display: flex; align-items: center; gap: 12px; }
        .logo-icon { background: var(--accent-blue); width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; color: white; }
        .logo-text { font-size: 1.4rem; font-weight: bold; letter-spacing: 1px; color: white; }
        .logo-text span { color: var(--accent-blue); }
        
        .nav-right { display: flex; align-items: center; gap: 20px; }
        .cart-badge { background: var(--accent-blue); color: white; padding: 8px 16px; border-radius: 8px; font-weight: 600; display: flex; align-items: center; gap: 8px; cursor: pointer; transition: 0.2s; }
        .cart-badge:hover { background: #0052cc; }

        /* Contenido Principal */
        main { flex: 1; max-width: 1280px; margin: 0 auto; padding: 40px 20px; width: 100%; }
        
        .hero { text-align: center; margin-bottom: 45px; }
        .hero-pill { display: inline-block; background: rgba(0, 102, 255, 0.15); color: #6EA8FE; padding: 6px 16px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; margin-bottom: 15px; border: 1px solid rgba(0, 102, 255, 0.3); }
        .hero h1 { font-size: 2.4rem; margin-bottom: 12px; color: white; font-weight: 800; }
        .hero p { color: var(--text-muted); font-size: 1.05rem; max-width: 650px; margin: 0 auto; line-height: 1.5; }

        .section-title { font-size: 1.4rem; margin-bottom: 25px; border-left: 4px solid var(--accent-blue); padding-left: 12px; color: white; font-weight: 700; }

        /* Grid de Productos (Idéntico al estilo que te gustaba) */
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; }
        .card { background: var(--card-bg); border-radius: 14px; overflow: hidden; border: 1px solid #1E293B; transition: 0.3s; display: flex; flex-direction: column; position: relative; }
        .card:hover { transform: translateY(-6px); border-color: var(--accent-blue); box-shadow: 0 12px 25px rgba(0, 102, 255, 0.2); }
        
        /* Etiquetas superiores en la tarjeta */
        .badge-brand { position: absolute; top: 14px; left: 14px; background: rgba(10, 25, 47, 0.85); color: #6EA8FE; padding: 5px 12px; border-radius: 6px; font-size: 0.75rem; font-weight: bold; backdrop-filter: blur(4px); letter-spacing: 0.5px; }
        .badge-rating { position: absolute; top: 14px; right: 14px; background: rgba(15, 23, 42, 0.85); color: #FACC15; padding: 5px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: bold; backdrop-filter: blur(4px); display: flex; align-items: center; gap: 4px; }
        
        .card img { width: 100%; height: 230px; object-fit: cover; background: #000; }
        .card-body { padding: 20px; display: flex; flex-direction: column; flex: 1; justify-content: space-between; }
        
        .card-meta { display: flex; justify-content: space-between; font-size: 0.75rem; color: var(--text-muted); margin-bottom: 8px; text-transform: uppercase; font-weight: 600; }
        .card-body h3 { font-size: 1.15rem; margin-bottom: 10px; color: white; font-weight: 700; }
        .card-body p { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 20px; line-height: 1.4; }
        
        .card-footer { display: flex; justify-content: space-between; align-items: center; margin-top: auto; border-top: 1px solid #1E293B; padding-top: 15px; }
        .price-container .label { font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; }
        .price-container .price { font-weight: 800; color: #6EA8FE; font-size: 1.15rem; }
        
        .btn-buy { background: var(--accent-blue); color: white; border: none; width: 44px; height: 44px; border-radius: 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.2s; font-size: 1.1rem; }
        .btn-buy:hover { background: #0052cc; transform: scale(1.05); }

        footer { text-align: center; padding: 25px; background: var(--primary-blue); color: var(--text-muted); font-size: 0.85rem; border-top: 1px solid #1E293B; margin-top: 60px; }
    </style>
</head>
<body>
    <header>
        <div class="logo-container">
            <div class="logo-icon">MZ</div>
            <div class="logo-text">MOTO<span>ZONE</span></div>
        </div>
        <div class="nav-right">
            <div class="cart-badge" onclick="alert('Tu carrito de compras está activo. ¡Productos listos para procesar!')">
                🛒 Carrito <span style="background: white; color: var(--accent-blue); padding: 2px 6px; border-radius: 4px; font-size: 0.8rem;">0</span>
            </div>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="hero-pill">E-COMMERCE OFICIAL &bull; SEGURIDAD CERTIFICADA</div>
            <h1>Seguridad de Élite para Motociclistas</h1>
            <p>Catálogo comercial de cascos certificados, chamarras y equipamiento profesional con los más altos estándares internacionales.</p>
        </section>

        <h2 class="section-title">Productos Destacados</h2>
        
        <div class="grid">
            {% for p in productos %}
            <div class="card">
                <span class="badge-brand">{{ p.marca }}</span>
                <span class="badge-rating">&#9733; {{ p.estrellas }}</span>
                <img src="{{ p.imagen }}" alt="{{ p.name }}">
                <div class="card-body">
                    <div class="card-meta">
                        <span>{{ p.categoria }}</span>
                        <span>{{ p.badge }}</span>
                    </div>
                    <h3>{{ p.name }}</h3>
                    <p>{{ p.descripcion }}</p>
                    <div class="card-footer">
                        <div class="price-container">
                            <div class="label">Precio MXN</div>
                            <div class="price">${{ "{:,.2f}".format(p.precio) }}</div>
                        </div>
                        <button class="btn-buy" title="Agregar al carrito" onclick="alert('¡{{ p.name }} agregado al carrito con éxito!')">🛒</button>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </main>

    <footer>
        <p>MotoZone Store &copy; 2026 — Mel Guzman (Certificación ECE 22.06 & DOT)</p>
    </footer>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
