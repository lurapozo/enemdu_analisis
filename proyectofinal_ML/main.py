from services.imagenes import create_ej
from services.text_speech import *
from services.powerpoint import *
from services.promt import *
from pptx import Presentation
import openai
import re

if __name__ == "__main__":

    API_KEY = ""  # Ingresar API_KEY
    openai.api_key = API_KEY

    # Pedirle al GPT que cree las diapositivas con un formato
    gpt_prompt = "Hola, soy un profesor de fundamentos de programacion y necesito que generes una diapositiva , el tema es de arreglos en numpy. Necesito que escribas el texto que va a aparecer en cada diapositiva. Escribelo con el siguiente formato 'Diapositiva 1: titulo de la diapositiva -- tema 1 -- tema 2', has que tenga 4 diapositivas."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.8,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=-1.0
    )
    f = open("./diapositivas.txt", "w")
    f.write(response['choices'][0]['text'])
    f.close()

    f = open("./diapositivas.txt", "r+")
    presentation = f.read()
    presentation = re.split("Diapositiva ", presentation, flags=re.IGNORECASE)

    f.close()
    promts = []
    # Creacion de diapositivas
    diapositivas = []
    pos = 0
    prs = Presentation()
    gen_presentacion(prs, pos, '', '')
    for diapo in presentation:
        if len(diapo) > 4:
            pos += 1
            promt = re.split("[0-9]*:", diapo)
            promt = promt[1]
            promts.append(promt)
            mostrar = promt.split('--')
            gen_presentacion(prs, pos, mostrar[0], '\n'.join(mostrar[1:]))

    # Ejercicios
    ejercicio1, explicacion1 = create_ej("./ejercicio1.png")
    gen_presentacion(prs, 1, '', ejercicio1)
    gen_img(prs, "./ejercicio1.png")
    ejercicio2, explicacion2 = create_ej("./ejercicio2.png")
    gen_presentacion(prs, 1, '', ejercicio2)
    gen_img(prs, "./ejercicio2.png")
    # Cargar Presentacion
    init_presentetation("clase.pptx")
    for promt in promts:
        gpt_prompt = f"Dame una version explicada de la siguiente diapositiva: \n{promt}"
        change_slide()
        explicar(gpt_prompt)

    # Ejercicios
    change_slide()
    text_to_speech(ejercicio1)
    change_slide()
    text_to_speech(explicacion1)
    change_slide()
    text_to_speech(ejercicio2)
    change_slide()
    text_to_speech(explicacion2)

    end_presentation()
