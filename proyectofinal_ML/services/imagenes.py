import openai
from PIL import Image, ImageDraw, ImageFont
import re
from services.powerpoint import *
from pptx import Presentation
from services.promt import ejercicios


def create_ej(filename: str) -> (str, str):
    gpt_prompt = (
        "Hola, soy un profesor de programacion y necesito que generes un ejercicio complejo de examen que se tenga "
        "que resolver usando arreglos de numpy. El ejercicio debe ser para estudiantes que ya saben programar. "
        "El ejercicio debe ser de crear arreglos con np.array, np.random, np.zeros o np.reshape, y realizar varias "
        "operaciones entre arreglos (suma, resta, multiplicacion), reshape, etc. Utiliza el siguiente formato: Ejercicio: "
        "aqui va el ejercicio\nPregunta: aqui va la pregunta\nSolución: aqui va la solucion (codigo)\nSalida: aqui va la "
        "salida\nExplicaciòn: aqui va la explicacion. En la sección de salida no pongas una respuesta muy larga, que se "
        "pasa de la diapositiva. La salida debe ser un escalar, una matriz o un arreglo de menor a 20 elementos.")
    response = ejercicios(gpt_prompt)

    ejercicio = re.split("Soluci[óo]n:", response, flags=re.IGNORECASE)

    operation = re.split("Explicaci[óo]n:", ejercicio[1], flags=re.IGNORECASE)
    # ejercicio = re.sub(r'^[.\n]*E', 'E', ejercicio[0])

    ejercicio = re.split("Ejercicio:", ejercicio[0])[1]
    text = operation[0]
    text = re.sub(r"\#.*", " ", text)
    explicacion = operation[1]
    font_filepath = "arial.ttf"
    font_size = 20
    val = re.split("Salida:", text, flags=re.IGNORECASE)
    try:
        if len(val[1]) > 30:
            text = val[0]
    except:
        val = text

    font = ImageFont.truetype(font_filepath, size=font_size)
    box = font.getsize_multiline(text)
    img = Image.new(mode="RGBA", size=(box[0], box[1]), color="white")
    draw = ImageDraw.Draw(img)
    draw_point = (0, 0)
    draw.multiline_text(draw_point, text, font=font, fill=(0, 0, 0), align="left")

    img.save(filename)

    return ejercicio, explicacion