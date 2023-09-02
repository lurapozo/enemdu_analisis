def explicar(gpt_prompt: str) -> str:
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
    f.write("------------------------------")
    f.write("------------------------------\n")
    f.close()
    # Aqui deberia hablar, cuando termine de hablar deberia cambiar de diapositiva, quitar lo de open write y close
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
    
    f = open("./diapositivas.txt", "r")
    presentation = f.read()
    presentation = re.split("Diapositiva ", presentation, flags=re.IGNORECASE)
    f.close()
    promts = []
    #Creacion de diapositivas
    for diapo in presentation:
        if len(diapo) > 4:
            promt = re.split("[0-9]*:", diapo)
            promt = promt[1]
            promts.append(promt)
            mostrar = promt.split('--')
            # El primero es el titulo, el resto los subtitulos
            # Hay que ponerlo en las diapositivas
    
    for promt in promts:
        gpt_prompt = f"Dame una version explicada de la siguiente diapositiva: \n{promt}"
        explicar(gpt_prompt)
    
    codigo = explicar("solo muestra un codigo de python que use numpy. No escribas nada mas")
    # Lo que esta en codigo debe ser una diapositiva extra, la ultima, en la que se explica un ejemplo de un codigo con arreglos
    explicar(f"Explica el siguiente codigo, linea por linea, sin decir las lineas del codigo {codigo}") # Explica el codigo
    # Aqui deberia haber una parte extra de preguntas y respuestas, si se puede
