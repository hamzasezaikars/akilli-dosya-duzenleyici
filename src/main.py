import os
from datetime import datetime

LOG_KLASORU = "logs"
LOG_DOSYASI = os.path.join(LOG_KLASORU, "log.txt")


def log_yaz(mesaj):
    if not os.path.exists(LOG_KLASORU):
        os.makedirs(LOG_KLASORU)

    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_DOSYASI, "a", encoding="utf-8") as f:
        f.write(f"{zaman} | {mesaj}\n")


def benzersiz_yol_uret(hedef_klasor, dosya_adi, uzanti):
    sayac = 1
    hedef_yol = os.path.join(hedef_klasor, f"{dosya_adi}{uzanti}")

    while os.path.exists(hedef_yol):
        hedef_yol = os.path.join(
            hedef_klasor, f"{dosya_adi}_{sayac}{uzanti}"
        )
        sayac += 1

    return hedef_yol


def klasoru_tara(klasor_yolu="."):
    print(f"Klasör taranıyor: {klasor_yolu}\n")
    log_yaz(f"Klasör taraması başlatıldı: {klasor_yolu}")

    for eleman in os.listdir(klasor_yolu):
        tam_yol = os.path.join(klasor_yolu, eleman)

        if os.path.isfile(tam_yol):
            dosya_adi, uzanti = os.path.splitext(eleman)

            if not uzanti:
                continue

            klasor_adi = uzanti[1:].upper()
            hedef_klasor = os.path.join(klasor_yolu, klasor_adi)

            if not os.path.exists(hedef_klasor):
                os.makedirs(hedef_klasor)
                log_yaz(f"Klasör oluşturuldu: {hedef_klasor}")

            hedef_yol = benzersiz_yol_uret(
                hedef_klasor, dosya_adi, uzanti
            )

            os.rename(tam_yol, hedef_yol)

            log_yaz(
                f"Taşındı: {eleman} → {os.path.basename(hedef_yol)}"
            )

            print(f"Taşındı: {eleman} → {os.path.basename(hedef_yol)}")

    log_yaz("Klasör taraması tamamlandı")


if __name__ == "__main__":
    klasoru_tara()
