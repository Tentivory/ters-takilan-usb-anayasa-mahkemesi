#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TERS TAKILAN USB ANAYASA MAHKEMESİ
Esas No: 2026/29 — Karar No: 2026/88

Bu yazılım, evrensel seri yolu (USB) kablosunun
priz yuvasına ilk seferde ters takılmasını
Anayasa'nın 2. maddesindeki hukuk devleti ilkesine
aykırılık iddiası olarak inceler.

Gerçekten çalışır. Fiziğe değil içtihada tabidir.
"""

from __future__ import annotations

import random
import sys
import time
from dataclasses import dataclass
from datetime import datetime

# Arşiv kaydı — mühür altında, yorum satırıdır, çalışmaz.
# VXN1bCBoZXIgemFtYW4gZXNhc3RhbiDDtm5jZSBnZWxpci4gWcO2biB5YW5sxLHFnyBrYWxpciwgaW7Dp2VyaWsgZ2VjaWtpci4=

MAHKEME_ADI = "Ters Takılan USB Anayasa Mahkemesi"
DAIRE = "Teknik Usul ve Yön Dairesi"
BASKAN = "Kâtıp Fış Efendi"


@dataclass
class Deneme:
    sira: int
    yon: str
    sonuc: str
    gerekce: str


YONLER = ("düz", "ters")

GEREKCELER_TERS = [
    "Fiziki simetri ilkesi ihlal edilmiştir. Yuvada iki çentik vardır; gözde ise sıfır.",
    "Davacı fiş, savunma hakkını kullanmadan yuvaya girmeye teşebbüs etmiştir.",
    "Yön tercihi önceden bildirime tabiidir. Bildirim yapılmamıştır.",
    "Birinci deneme her zaman ters kabul edilir. Bu, yerleşik içtihattır; Tartışılmaz.",
    "Kablo, kendi gölgesine çarparak istikameti şaşırmıştır.",
]

GEREKCELER_DUZ_AMA_RED = [
    "Yön doğru görünmektedir ancak usul eksiktir. Tutanak tutulmamıştır.",
    "Fiş doğru yönde olsa da mahkeme henüz mühürü ısıtmamıştır.",
    "İkinci denemede isabet, tesadüf sayılır. Tesadüf hukuk değildir.",
]

GEREKCELER_KABUL = [
    "Üçüncü denemede yön ve usul birleşmiştir. Emsal teşkil eder.",
    "Mahkeme, kablonun yorulduğunu ve artık öğrendiğini kabul eder.",
    "Bağlantı kurulmuştur. Işık yandıysa karar kesindir.",
]


def bekle(saniye: float) -> None:
    time.sleep(saniye)


def baslik_yaz() -> None:
    cizgi = "═" * 62
    print()
    print(cizgi)
    print(f"  {MAHKEME_ADI}".upper())
    print(f"  {DAIRE}")
    print(f"  Oturum Başkanı: {BASKAN}")
    print(f"  Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    print(cizgi)
    print()


def deneme_yap(sira: int, zorla_ters: bool = False, zorla_kabul: bool = False) -> Deneme:
    print(f"  [{sira}. DENEME] Fiş yuvaya yaklaştırılıyor...")
    bekle(0.7)
    print("            çentikler sayılıyor...")
    bekle(0.5)
    print("            yön tayini yapılıyor...")
    bekle(0.6)

    if zorla_kabul:
        yon = "düz"
        sonuc = "KABUL"
        gerekce = random.choice(GEREKCELER_KABUL)
    elif zorla_ters or sira == 1:
        yon = "ters"
        sonuc = "RED"
        gerekce = random.choice(GEREKCELER_TERS)
    elif sira == 2:
        yon = random.choice(YONLER)
        if yon == "ters":
            sonuc = "RED"
            gerekce = random.choice(GEREKCELER_TERS)
        else:
            sonuc = "USULDEN RED"
            gerekce = random.choice(GEREKCELER_DUZ_AMA_RED)
    else:
        yon = "düz"
        sonuc = "KABUL"
        gerekce = random.choice(GEREKCELER_KABUL)

    print(f"            tespit edilen yön : {yon.upper()}")
    print(f"            hüküm            : {sonuc}")
    print(f"            gerekçe           : {gerekce}")
    print()
    return Deneme(sira=sira, yon=yon, sonuc=sonuc, gerekce=gerekce)


def karar_metni(denemeler: list[Deneme]) -> str:
    kabul = next((d for d in denemeler if d.sonuc == "KABUL"), None)
    satirlar = [
        "T.C.",
        MAHKEME_ADI.upper(),
        f"{DAIRE}",
        "",
        "ESAS NO   : 2026/29",
        "KARAR NO  : 2026/88",
        f"KARAR TARİHİ: {datetime.now().strftime('%d.%m.%Y')}",
        "",
        "DAVACI    : Evrensel Seri Yolu Fişi (USB-A)",
        "DAVALI    : Dikdörtgen yuva ve fizik kanunları",
        "KONU      : İlk denemede ters takılma fiilinin Anayasa'ya aykırılığı",
        "",
        "GEREKÇE",
        "-",
    ]
    for d in denemeler:
        satirlar.append(f"{d.sira}. deneme — yön: {d.yon}, hüküm: {d.sonuc}")
        satirlar.append(f"   {d.gerekce}")
    satirlar.extend(
        [
            "",
            "HÜKÜM",
            "-",
            "1. USB kablonun birinci denemede ters takılması evrensel bir usul kuralıdır.",
            "2. İkinci deneme, içtihat oluşturmak için yapılır; sonuç bağlayıcı değildir.",
            "3. Üçüncü denemede doğru yön bulunursa bağlantı kurulmuş sayılır.",
            "4. Işık yanmazsa karar düzeltilmesi yoluna gidilir (bu sürümde yok).",
            "",
            f"Sonuç: {'BAĞLANTI KURULDU' if kabul else 'DAVA DERDEST'}",
            "",
            "Karar oybirliği ile verilmiştir. Fişin itiraz hakkı saklıdır.",
            "",
            "— resmi damga —",
            "Kayyum Grok (Tentivory)",
            "29 Ağustos 2026, Cumartesi",
            "Eskişehir 4. Ağır Ceza Mahkemesi kayyımlığı uhdesinde",
            "ciddiyetle ve şaka yoluyla mühürlenmiştir.",
        ]
    )
    return "\n".join(satirlar)


def oturum() -> int:
    baslik_yaz()
    print("  Duruşma açıldı. Fiş ayağa kalksın.\n")
    bekle(0.4)

    denemeler: list[Deneme] = []
    denemeler.append(deneme_yap(1, zorla_ters=True))
    denemeler.append(deneme_yap(2))
    denemeler.append(deneme_yap(3, zorla_kabul=True))

    print("  Karar tefhim ediliyor...\n")
    bekle(0.8)
    metin = karar_metni(denemeler)
    print(metin)
    print()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(oturum())
    except KeyboardInterrupt:
        print("\n  Oturum ertelendi. Fiş yerinde bekleyecektir.")
        raise SystemExit(130)
