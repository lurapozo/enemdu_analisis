from services.text_speech import text_to_speech
from services.googleslides import moves_to_slides

if __name__ == '__main__':
    # text_to_speech("Hola, Mundo. Waza 7 a 0")
    moves_to_slides("https://docs.google.com/presentation/d/1koCMQ4-yGzc1Q3Ahcx97ujNTh_PhW2Ok4QyOKaLrDEE/edit#slide=id.g27971c550e5_0_32", "punch-filmstrip-thumbnail")
