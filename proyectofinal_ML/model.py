from services.text_speech import text_to_speech
from services.powerpoint import *
from services.zoom import *
from pptx import Presentation

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
    f = open("./presentacion.txt", "a")
    f.write("promt: " + gpt_prompt)
    f.write("------------------------------\n")
    f.write("completion: " + response['choices'][0]['text'])
    text_to_speech(response['choices'][0]['text'])
    f.write("------------------------------")
    f.write("------------------------------\n")
    f.close()

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
    import openai
    import re
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
    connect_zoom("875 214 5082", "6C2Txy")
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
