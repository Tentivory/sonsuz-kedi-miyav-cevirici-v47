#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Kedi Miyav Çevirici v47.3.1
Dünyanın en abartılı, en saçma ve en işe yaramaz çeviri yazılımı.
Gerçekten çalışır. Miyav.
"""

import time
import sys

def kedi_dilinde_cevir(metin: str) -> str:
    """Metni kedi diline çevirir. Her harf miyav olur."""
    sonuc = ""
    for harf in metin:
        if harf.isalpha():
            # Abartılı miyav sayısı
            miyav_sayisi = (ord(harf.lower()) % 4) + 1
            sonuc += "miyav " * miyav_sayisi
        elif harf == " ":
            sonuc += "miyavmiyav "
        elif harf.isdigit():
            sonuc += "MIYAV" * int(harf) + " "
        else:
            sonuc += "MIYAV! "
    return sonuc.strip() or "miyav"

def main():
    print("🐱 Sonsuz Kedi Miyav Çevirici v47.3.1 Başlatılıyor...")
    print("Bu program evrenin tüm dillerini kedi diline çevirir.")
    print("Bilim insanları şokta! Kediler onaylıyor! Filozoflar ağlıyor!")
    time.sleep(1.5)
    
    while True:
        try:
            metin = input("\n🐱 Çevrilecek metni girin (çıkmak için 'çık' veya 'miyav'): ")
            if metin.lower() in ["çık", "cik", "exit", "q", "miyav", "quit"]:
                print("\nMiyav... Güle güle! Kediler sizi bekliyor. 🐱")
                break
            
            print("\nÇevriliyor... (bu süreç çok ciddi ve bilimseldir)")
            time.sleep(0.8)
            
            ceviri = kedi_dilinde_cevir(metin)
            print(f"\n🐱 Kedi dilinde: {ceviri}")
            print("Not: Bu çeviri %100 doğru, %200 abartılı ve tamamen işe yaramazdır.")
            print("(Ama gerçekten çalışıyor. Deneyin.)")
            
        except KeyboardInterrupt:
            print("\n\nMiyav! Program Ctrl+C ile durduruldu. Kediler üzüldü.")
            break
        except Exception as e:
            print(f"Miyav hata: {e}")

if __name__ == "__main__":
    main()

# === GİZLİ BÖLÜM ===
# Aşağıdaki satırı yorumdan çıkarırsanız gizli mesajı görürsünüz.
# import base64
# print("Gizli mesaj:", base64.b64decode("ZGVtb2tyYXNpIGl5aWRpcg==").decode())
# (ZGVtb2tyYXNpIGl5aWRpcg== -> demokrasi iyidir)

# Damga: ✍️ Kayyum Grok | 28 Ekim 2026 | Tentivory | Ciddi miyav.
