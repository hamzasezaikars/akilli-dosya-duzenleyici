import os

def benzersiz_yol_uret(hedef_klasor, dosya_adi, uzanti):
    sayac = 1
    yeni_isim = f"{dosya_adi}{uzanti}"
    hedef_yol = os.path.join(hedef_klasor, yeni_isim)

    while os.path.exists(hedef_yol):
        yeni_isim = f"{dosya_adi}_{sayac}{uzanti}"
        hedef_yol = os.path.join(hedef_klasor, yeni_isim)
        sayac += 1

    return hedef_yol


def klasoru_tara(klasor_yolu="."):
    print(f"Klasör taranıyor: {klasor_yolu}\n")

    for eleman in os.listdir(klasor_yolu):
        tam_yol = os.path.join(klasor_yolu, eleman)

        if os.path.isfile(tam_yol):
            dosya_adi, uzanti = os.path.splitext(eleman)

            if uzanti:
                klasor_adi = uzanti[1:].upper()
                hedef_klasor = os.path.join(klasor_yolu, klasor_adi)

                if not os.path.exists(hedef_klasor):
                    os.makedirs(hedef_klasor)
                    print(f"Oluşturuldu: {hedef_klasor}")

                hedef_yol = benzersiz_yol_uret(
                    hedef_klasor, dosya_adi, uzanti
                )

                os.rename(tam_yol, hedef_yol)
                print(f"Taşındı: {eleman} → {os.path.basename(hedef_yol)}")

if __name__ == "__main__":
    klasoru_tara()
