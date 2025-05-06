% pakar_gangguan_gui.pl
:- dynamic gejala/1.

% Diagnosa berdasarkan gejala (minimal terpenuhi sebagian)

gangguan(depresi) :-
    gejala_terpenuhi([sedih, kehilangan_minat, gangguan_tidur, lelah, pikiran_bunuh_diri], 3).

gangguan(gangguan_kecemasan) :-
    gejala_terpenuhi([cemas_berlebihan, jantung_berdebar, sulit_bernapas, sulit_konsentrasi], 3).

gangguan(bipolar) :-
    gejala_terpenuhi([suasana_hati_naik_turun, impulsif, sangat_aktif, depresi], 3).

gangguan(skizofrenia) :-
    gejala_terpenuhi([halusinasi, delusi, bicara_kacau, menarik_diri], 2).

gangguan(gangguan_makan) :-
    gejala_terpenuhi([makan_berlebihan, muntah_dipaksa, tidak_makan], 2).

gangguan(ocd) :-
    gejala_terpenuhi([pikiran_berulang, perilaku_berulang, tidak_nyaman_jika_tidak_dilakukan], 2).

gangguan(ptsd) :-
    gejala_terpenuhi([mimpi_buruk, kilas_balik, hindari_situasi, waspada_berlebihan], 2).

% Saran untuk tiap gangguan

saran(depresi, "Konsultasikan dengan psikolog dan pertimbangkan terapi atau obat.").
saran(gangguan_kecemasan, "Lakukan latihan relaksasi dan terapi kognitif.").
saran(bipolar, "Diperlukan penanganan medis dari psikiater dan manajemen suasana hati.").
saran(skizofrenia, "Memerlukan pengobatan jangka panjang dan dukungan sosial.").
saran(gangguan_makan, "Konsultasi dengan dokter gizi dan psikolog sangat dianjurkan.").
saran(ocd, "Terapi perilaku dan medikasi bisa membantu.").
saran(ptsd, "Terapi trauma dan konseling sangat dianjurkan.").

% Fungsi bantu: gejala_terpenuhi(ListGejala, MinimalJumlah)

gejala_terpenuhi(List, Min) :-
    findall(X, (member(X, List), gejala(X)), Ditemukan),
    length(Ditemukan, N),
    N >= Min.
