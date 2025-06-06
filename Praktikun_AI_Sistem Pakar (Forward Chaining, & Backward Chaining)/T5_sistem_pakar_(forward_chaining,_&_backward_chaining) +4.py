# -*- coding: utf-8 -*-
"""Tugas Sistem Pakar (Forward Chaining, & Backward Chaining).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TpK8a9LIQRFFbFfk1febJ_dUKbpKQqDB
"""

from experta import *

class Diagnosis(KnowledgeEngine):

    @Rule(Fact(batuk=True) & Fact(demam=True) & Fact(kelelahan=True))
    def flu(self):
        print("Diagnosis: Kamu mungkin terkena Flu.")

    @Rule(Fact(batuk=True) & Fact(demam=True) & Fact(sesak_napas=True))
    def pneumonia(self):
        print("Diagnosis: Kamu mungkin terkena Pneumonia.")

    @Rule(Fact(bersin=True) & Fact(hidung_berair=True) & Fact(batuk=False))
    def pilek(self):
        print("Diagnosis: Kamu mungkin terkena Pilek.")

    @Rule(Fact(sakit_tenggorokan=True) & Fact(demam=True))
    def infeksi_tenggorokan(self):
        print("Diagnosis: Kamu mungkin mengalami Infeksi Tenggorokan.")

    # === Penyakit Tambahan ===
    @Rule(Fact(batuk=True) & Fact(demam=True) & Fact(kelelahan=True) & Fact(kehilangan_penciuman=True))
    def covid(self):
        print("Diagnosis: Kamu mungkin terkena COVID-19.")

    @Rule(Fact(bersin=True) & Fact(mata_gatal=True) & Fact(hidung_berair=True))
    def alergi(self):
        print("Diagnosis: Kamu mungkin mengalami Alergi.")

    @Rule(Fact(batuk=True) & Fact(demam=True) & Fact(penurunan_bb=True) & Fact(demam_berkepanjangan=True))
    def tbc(self):
        print("Diagnosis: Kamu mungkin terkena TBC (Tuberkulosis).")

    @Rule(Fact(demam=True) & Fact(ruam_kulit=True) & Fact(nyeri_sendi=True))
    def dbd(self):
        print("Diagnosis: Kamu mungkin terkena DBD (Demam Berdarah Dengue).")

    @Rule(
        Fact(batuk=False), Fact(demam=False), Fact(kelelahan=False), Fact(sesak_napas=False),
        Fact(bersin=False), Fact(hidung_berair=False), Fact(sakit_tenggorokan=False),
        Fact(kehilangan_penciuman=False), Fact(mata_gatal=False), Fact(penurunan_bb=False),
        Fact(demam_berkepanjangan=False), Fact(ruam_kulit=False), Fact(nyeri_sendi=False)
    )
    def sehat(self):
        print("Diagnosis: Kondisi kamu tampaknya sehat.")

def input_gejala():
    """Fungsi untuk menanyakan gejala ke pengguna."""
    def tanya(pertanyaan):
        return input(pertanyaan + " (ya/tidak): ").strip().lower() == "ya"

    return {
        "batuk": tanya("Apakah kamu batuk?"),
        "demam": tanya("Apakah kamu demam?"),
        "kelelahan": tanya("Apakah kamu merasa kelelahan?"),
        "sesak_napas": tanya("Apakah kamu mengalami sesak napas?"),
        "bersin": tanya("Apakah kamu bersin-bersin?"),
        "hidung_berair": tanya("Apakah kamu mengalami hidung berair?"),
        "sakit_tenggorokan": tanya("Apakah kamu sakit tenggorokan?"),
        "kehilangan_penciuman": tanya("Apakah kamu kehilangan indra penciuman?"),
        "mata_gatal": tanya("Apakah kamu mengalami mata gatal?"),
        "penurunan_bb": tanya("Apakah berat badanmu menurun drastis?"),
        "demam_berkepanjangan": tanya("Apakah kamu demam selama berminggu-minggu?"),
        "ruam_kulit": tanya("Apakah kamu memiliki ruam atau bintik merah di kulit?"),
        "nyeri_sendi": tanya("Apakah kamu merasakan nyeri pada sendi?")
    }

if __name__ == "__main__":
    print("=== Sistem Pakar Diagnosa Penyakit ===")
    print("Silakan jawab pertanyaan berikut dengan 'ya' atau 'tidak':")
    gejala = input_gejala()

    engine = Diagnosis()
    engine.reset()

    for nama, nilai in gejala.items():
        engine.declare(Fact(**{nama: nilai}))

    engine.run()

!pip install frozendict==2.3.4
!pip install experta --no-deps

!pip install experta --no-deps