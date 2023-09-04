from services.text_speech import *
from services.powerpoint import *
from services.zoom import *
from pptx import Presentation
import openai
import re


def explicar(gpt_prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.8,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    text_to_speech(response['choices'][0]['text'])


def codigo(gpt_prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.8,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']

if __name__ == "__main__":

    API_KEY = "" # Ingresar API_KEY
    openai.api_key = API_KEY
    
    #Pedirle al GPT que cree las diapositivas con un formato
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
    codigo = codigo("solo muestra un codigo de python que use numpy donde se realize operaciones aritmeticas entre arreglos. No escribas nada mas")
    f.write("\nDiapositiva 5: Ejemplo de Código con arreglos de numpy --" + codigo)
    f.close()
    promts = []
    #Creacion de diapositivas
    diapositivas = []
    pos = 0
    prs = Presentation()
    gen_presentacion(prs, pos,'','')
    for diapo in presentation:
        if len(diapo) > 4:
            pos += 1
            promt = re.split("[0-9]*:", diapo)
            promt = promt[1]
            promts.append(promt)
            mostrar = promt.split('--')
            gen_presentacion(prs, pos, mostrar[0],'\n'.join(mostrar[1:]))
            diapositivas.append(mostrar)

    diapositivas.append(['Ejemplo de Código con arreglos de numpy', codigo])
    gen_presentacion(prs, 1,'Ejemplo de Código con arreglos de numpy',codigo)
    print(diapositivas)
    # Conectar Zoom
    # Nota: Debes ser el link con el enlace tu cuenta, si ingresas otro link y la reunion no esta habilitada. Se caera el programa
    connect_zoom("875 214 5082", "6C2Txy")
    sleep(2)
    write_chat("Bienvenidos a la clase, comenzamos en segundos en 3s !!!")
    sleep(3)
    share_screen()
    sleep(2)
    # Cargar Presentacion
    init_presentetation("test.pptx")
    sleep(2)
    for promt in promts:
        gpt_prompt = f"Dame una version explicada de la siguiente diapositiva: \n{promt}"
        change_slide()
        explicar(gpt_prompt)
    change_slide()
    explicar(f"Explica el siguiente codigo, linea por linea, sin decir las lineas del codigo pero sí el número de la línea (no cuentes las lineas con espacios): {codigo}") # Explica el codigo
    # Aqui deberia haber una parte extra de preguntas y respuestas, si se puede
    end_presentation()
    # Experimental
    mensaje = "Comenzar"
    num_preguntas = 0
    text_to_speech("Para finalizar la clase, tienen algunas duda, queja, inconformidad o pregunta referente a la clase?")
    while len(mensaje) != 0 or mensaje == "no" or num_preguntas > 1:
        mensaje = speech_to_text()
        if len(mensaje) > 0:
            explicar(mensaje)
            num_preguntas += 1
        sleep(1)
        text_to_speech("Siguiente pregunta o no hay mas dudas?")
    sleep(1)