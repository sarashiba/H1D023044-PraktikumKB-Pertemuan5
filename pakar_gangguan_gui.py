from tkinter import *
from tkinter import messagebox
from pyswip import Prolog

prolog = Prolog()
prolog.consult("pakar_gangguan_gui.pl")  # File Prolog

gejala_list = [
    "sedih", "kehilangan_minat", "gangguan_tidur", "lelah", "pikiran_bunuh_diri",
    "cemas_berlebihan", "jantung_berdebar", "sulit_bernapas", "sulit_konsentrasi",
    "suasana_hati_naik_turun", "impulsif", "sangat_aktif", "depresi",
    "halusinasi", "delusi", "bicara_kacau", "menarik_diri",
    "makan_berlebihan", "muntah_dipaksa", "tidak_makan",
    "pikiran_berulang", "perilaku_berulang", "tidak_nyaman_jika_tidak_dilakukan",
    "mimpi_buruk", "kilas_balik", "hindari_situasi", "waspada_berlebihan"
]

index = 0

def mulai_diagnosa():
    global index
    index = 0
    tanya()

def keluar():
    root.quit()

def tanya():
    global index
    if index < len(gejala_list):
        pertanyaan.set(f"Apakah Anda mengalami gejala: {gejala_list[index].replace('_', ' ')}?")
        btn_ya.config(command=ya)
        btn_tidak.config(command=tidak)
    else:
        diagnosa()

def ya():
    global index
    prolog.assertz(f"gejala({gejala_list[index]})")
    index += 1
    tanya()

def tidak():
    global index
    index += 1
    tanya()

def diagnosa():
    hasil = list(prolog.query("gangguan(G).", maxresult=1))
    if hasil:
        gangguan = hasil[0]['G']
        saran = list(prolog.query(f"saran({gangguan}, S)."))[0]['S']
        messagebox.showinfo(
            "Hasil Diagnosa", 
            f"Anda kemungkinan mengalami:\n\n{gangguan.replace('_', ' ').title()}\n\nSaran:\n{saran}"
        )
    else:
        messagebox.showinfo(
            "Hasil Diagnosa", 
            "Tidak ditemukan gangguan mental berdasarkan gejala yang Anda pilih."
        )
    root.quit()

# GUI Setup
root = Tk()
root.title("Sistem Pakar Diagnosa Gangguan Mental")
root.geometry("500x300")

pertanyaan = StringVar()
pertanyaan.set("Mulai diagnosa?")

judul = Label(root, text="Sistem Pakar Diagnosa Gangguan Mental", font=("Arial", 14, "bold"), pady=10)
judul.pack()

label = Label(root, textvariable=pertanyaan, wraplength=400, font=("Arial", 12), pady=20)
label.pack()

frame_btn = Frame(root)
frame_btn.pack(pady=10)

btn_ya = Button(frame_btn, text="Ya", width=10, command=mulai_diagnosa)
btn_ya.pack(side=LEFT, padx=20)

btn_tidak = Button(frame_btn, text="Tidak", width=10, command=keluar)
btn_tidak.pack(side=RIGHT, padx=20)

root.mainloop()
