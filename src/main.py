import os

def klasoru_tara(klasor_yolu="."):
    print(f"Klasör taranıyor: {klasor_yolu}\n")

    for eleman in os.listdir(klasor_yolu):
        tam_yol = os.path.join(klasor_yolu, eleman)

        if os.path.isfile(tam_yol):
            dosya_adi, uzanti = os.path.splitext(eleman)
            print(f"Dosya: {dosya_adi} | Uzantı: {uzanti}")

if __name__ == "__main__":
    klasoru_tara()
