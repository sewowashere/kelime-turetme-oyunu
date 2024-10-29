import random

kelimeler = ["armut", "beton", "cereyan", "çiçek", "dolap", "ezik", "fotoğraf", "gezi",
            "halı", "ışık", "insan", "jetski", "kola", "lale", "metafor", "nane",
            "otoyol", "öküz", "peri", "rosto", "sinek", "şelale", "taşıt", "uzuv", "üzengi", "votka", "yatak", "zincir"]

def start():
    user_input = input("\n\nKELİME TÜRETMECE\nbaşlamak için yaz: başla\n")
    if user_input.lower() == "başla":
        print("oyun başladı.")
        return random.choice(kelimeler)
    else:
        print("\n\noyun başlatılamadı. tekrar dene.\n")
        return start()

def word_pick(word):
    return next((kelime for kelime in kelimeler if kelime.startswith(word)), None)

def main():
    current_word = start()
    print(f"\nverilen kelime: {current_word}")
    
    while True:
        gamers_w = input(f"\nsenin kelimen: ")

        if not gamers_w:
            print("kelime girilmedi.")
            break

        last_letter = gamers_w.lower()[-1]

        new_word = word_pick(last_letter)

        if new_word:
            print(f"\nyeni kelime: {new_word}")
            current_word == new_word
        else:
            print("bu kelimeye karşılık bir kelime bulunamadı.")

main()