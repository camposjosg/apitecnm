from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def root():
    return ""

# Lista de carreras
carreras = [
    {"id": "01", "nombre": "Ing. en Sistemas Computacionales"},
    {"id": "02", "nombre": "Ing. Industrial"},
    {"id": "03", "nombre": "Ing. en Tecnologías de la Información y Comunicaciones"},
    {"id": "04", "nombre": "Ing. en Gestión Empresarial"},
    {"id": "05", "nombre": "Ing. Electrónica"},
    {"id": "06", "nombre": "Ing. Electromecánica"},
    {"id": "07", "nombre": "Ing. Mecatrónica"},
    {"id": "08", "nombre": "Ing. en Logística"}
]

# Lista de especialidades por carrera
especialidades = {
    "01": [
        {"id": "01", "nombre": "Cómputo Empresarial"},
        {"id": "02", "nombre": "Redes"},
        {"id": "03", "nombre": "Inteligencia Artificial"}
    ],
    "02": [
        {"id": "01", "nombre": "Ingeniería en Manufactura y Calidad"},
        {"id": "02", "nombre": "Manufactura en Artículos de Piel"}
    ],
    "03": [
        {"id": "01", "nombre": "Gestión de Servicios de TI en Ambientes Empresariales"}
    ]
    # Las demás carreras no tienen especialidades
}

# Lista de materias por carrera
materias = {
    "02": [
        "Química",
        "Taller de Ética",
        "Cálculo Diferencial",
        "Taller de Herramientas Intelectuales",
        "Fundamentos de Investigación",
        "Dibujo Industrial",
        "Actividades Complementarias",
        "Metrología y Normalización",
        "Electricidad y Electrónica Industrial",
        "Cálculo Integral",
        "Física",
        "Probabilidad y Estadística",
        "Análisis de la Realidad Nacional",
        "Taller de Liderazgo",
        "Propiedad de los Materiales",
        "Economía",
        "Cálculo Vectorial",
        "Álgebra Lineal",
        "Estadística Inferencial 1",
        "Estudio del Trabajo 1",
        "Administración de Proyectos",
        "Procesos de Fabricación",
        "Algoritmos y Lenguajes de Programación",
        "Administración de Operaciones 1",
        "Investigación de Operaciones 1",
        "Estadística Inferencial 2",
        "Estudio del Trabajo 2",
        "Higiene y Seguridad Industrial",
        "Gestión de Costos",
        "Mercadotecnia",
        "Administración de Operaciones 2",
        "Investigación de Operaciones 2",
        "Control Estadístico de la Calidad",
        "Ergonomía",
        "Desarrollo Sustentable",
        "Ing. Económica",
        "Taller de Investigación 1",
        "Ing. de Sistemas",
        "Simulación",
        "Administración del Mantenimiento",
        "Planeación Financiera",
        "Relaciones Industriales",
        "Planeación y Diseño de Instalaciones",
        "Sistemas de Manufactura",
        "Logística y Cadena de Suministro",
        "Gestión de los Sistemas de Calidad",
        "Formación y Evaluación de Proyectos",
        "Servicio Social",
        "Taller de Investigación 2",
        "Residencia Profesional"
    ]
}

# Lista de materias por especialidad
materias_especialidades = {
    "02": {
        "01": [
            "Sistemas Neumáticos e Hidráulicos",
            "Diseño Asistido por Computadora",
            "Controladores Lógicos Programables",
            "Temas Selectos de Manufactura",
            "Core Tools",
            "Medición y Mejoramiento de la Productividad",
            "Robótica Industrial",
            "Manufactura Flexible"
        ],
        "02": [
            "Diseño y Modelado",
            "Diseño Asistido por Computadora",
            "Tecnología y Taller 1",
            "Temas Selectos de Manufactura",
            "Core Tool",
            "Tecnología y Taller 2",
            "Medición y Mejoramiento de la Productividad",
            "Administración de los Sistemas de Producción de Calzado"
        ]
    }
}

@app.route("/carreras/<carrera_id>")
def get_carrera(carrera_id):
    carrera = next((carrera for carrera in carreras if carrera["id"] == carrera_id), None)
    if carrera:
        query = request.args.get('query')
        if query:
            carrera["query"] = query
        return jsonify(carrera), 200
    else:
        return jsonify({"error": "Carrera no encontrada"}), 404

@app.route("/carreras/<carrera_id>/especialidades")
def get_especialidades(carrera_id):
    if carrera_id in especialidades:
        return jsonify(especialidades[carrera_id]), 200
    else:
        return jsonify({"error": "No hay especialidades para esta carrera o carrera no encontrada"}), 404

@app.route("/carreras/<carrera_id>/especialidades/<int:index>")
def get_especialidad(carrera_id, index):
    if carrera_id in especialidades:
        if 0 <= index < len(especialidades[carrera_id]):
            return jsonify(especialidades[carrera_id][index]), 200
        else:
            return jsonify({"error": "Índice de especialidad fuera de rango"}), 404
    else:
        return jsonify({"error": "Carrera no encontrada"}), 404

@app.route("/carreras/<carrera_id>/materias")
def get_materias(carrera_id):
    if carrera_id in materias:
        return jsonify(materias[carrera_id]), 200
    else:
        return jsonify({"error": "No hay materias para esta carrera o carrera no encontrada"}), 404

@app.route("/carreras/<carrera_id>/especialidades/<especialidad_id>/materias")
def get_materias_especialidad(carrera_id, especialidad_id):
    if carrera_id in materias_especialidades and especialidad_id in materias_especialidades[carrera_id]:
        return jsonify(materias_especialidades[carrera_id][especialidad_id]), 200
    else:
        return jsonify({"error": "No hay materias para esta especialidad o especialidad no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
