import base64

instruments = [
    {
        "name": "Korg X5D",
        "description": "El Korg X5D es un sintetizador compacto y versátil con teclas sensibles a la velocidad, ofreciendo una amplia variedad de sonidos gracias a su síntesis de tabla de ondas. Su diseño intuitivo facilita la creación y manipulación de sonidos en tiempo real, brindando una experiencia expresiva a los músicos. La capacidad de programación permite la creación de patches únicos, y su conectividad MIDI facilita la integración en estudios y actuaciones en vivo. La opción de alimentación por baterías mejora su portabilidad, y su diseño atractivo y ergonómico, que se puede llevar sobre el hombro, proporciona una presencia visual impactante en el escenario.",
        "image": "https://files.soniccdn.com/images/products/original/218/korg-x5d-23218.jpg",
        "artist": ["Amerika'n Sound", "Grupo Alegria"],
        "glbModel": "",
        "demo":"https://www.synthmania.com/Korg%2005RW/Audio/PROG/A21%20Last%20Tango.mp3"
    },
    {
        "name": "Roland D-50",
        "description": """
            El Roland D-50, pionero de la década de 1980 en la música electrónica,
            es un sintetizador emblemático. Su revolucionaria síntesis lineal fusiona tecnologías de síntesis digital y modelado,
            generando una amplia gama de sonidos expresivos. Con 61 teclas sensibles y aftertouch,
            garantiza una interpretación dinámica, mientras su interfaz gráfica simplifica la creación de sonidos personalizados.

            Reconocido por sus característicos "patches", que incluyen desde campanas hasta cuerdas,
            el D-50 emite un sonido digital distintivo y cálido. Sus salidas de audio estéreo, puertos MIDI y
            capacidad de almacenamiento mediante tarjeta de memoria aseguran conectividad avanzada. Aunque ha sido sucedido,
            su legado perdura, siendo codiciado por músicos y productores por su singularidad y
            contribución fundamental a la evolución de la música electrónica.""",
        "image": "https://static.roland.com/assets/images/products/gallery/rc_d-50_gal.jpg?_ga=2.175881890.1631167708.1693943851-1259623013.1693943851",
        "artist": ["Amerika'n Sound", "Grupo Alegria", "Mr President"],
        "glbModel": "",
        "demo":"https://www.synthmania.com/Roland%20D-50/Audio/Factory%20preset%20demos/15%20Horn%20Section.mp3"
    },
    {
        "name": "Yamaha DX7",
        "description": """
            El Yamaha DX7, lanzado en 1983, es un icónico sintetizador digital que introdujo la síntesis de modulación de frecuencia (FM).
            Con 61 teclas sensibles a la velocidad, ofrece una experiencia dinámica de interpretación. 
            Aunque su panel de control inicialmente desafiante permitía esculpir sonidos complejos mediante síntesis FM,
            el DX7 destacó por su capacidad para reproducir sonidos realistas de instrumentos acústicos y texturas electrónicas.

            Este sintetizador tuvo un impacto significativo en la música de la década de 1980 y se convirtió en uno de los más vendidos de todos los tiempos.
            Su conectividad MIDI avanzada facilitó su integración en estudios y actuaciones en vivo. Aunque la programación inicial podía ser compleja,
            el legado duradero del DX7 se debe a su sonido distintivo y su influencia en la evolución de la música electrónica.""",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/YAMAHA_DX7.jpg/1024px-YAMAHA_DX7.jpg",
        "artist": ["A-ha", "Toto", "Michael Jackson"],
        "glbModel": "",
        "demo":"https://www.synthmania.com/Yamaha%20DX7/Audio/INT/INT02%20BRASS%20%20%202.mp3"
    },
    {
        "name": "Roland AX-1",
        "description": "El Roland AX-1 es un keytar diseñado para músicos en movimiento, con un diseño ergonómico que permite llevarlo cómodamente sobre el hombro. Este controlador MIDI cuenta con teclas sensibles a la velocidad, una variedad de botones asignables para la manipulación en tiempo real de parámetros de sonido, y se conecta a dispositivos externos a través de MIDI. Su portabilidad se ve reforzada por la opción de alimentación mediante baterías, y su forma única se asemeja a una guitarra para ofrecer una experiencia visualmente impactante en el escenario.",
        "image": "https://synth.market/media/shop_items/roland_ax_1_1.jpg",
        "artist": ["Damas Gratis", "Rafaga", "Amar Azul"],
        "glbModel": "ROLAND-AX1-RED-V1.glb",
        "demo":None
    },
]

glb_file_path = "media/glbModels/ROLAND-AX1-RED-V1.glb"


def read_and_encode_glb(file_path):
    with open(file_path, "rb") as file:
        glb_data = file.read()
        base64_data = base64.b64encode(glb_data).decode("utf-8")
        return "data:text/plain;charset=utf-8;base64," + base64_data


def get_base64():
    base64_data = read_and_encode_glb(glb_file_path)
    print(base64_data)
