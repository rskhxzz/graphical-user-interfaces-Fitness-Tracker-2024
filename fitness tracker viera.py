from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def sistem_tracking():
    root = Tk()
    root.title("Input Data Pribadi")
    root.configure(bg="#96D2D9")
    root.attributes('-fullscreen', True)

    nama = StringVar()
    usia = StringVar()
    jenis_kelamin = StringVar()
    tinggi_badan = StringVar()
    berat_badan = StringVar()
    preferensi_aktivitas = StringVar()
    tekanan = StringVar()
    detak_jatung = StringVar()
    kalori = StringVar()

    def reset():
        nama.set("")
        usia.set("")
        jenis_kelamin.set("")
        tinggi_badan.set("")
        berat_badan.set("")
        preferensi_aktivitas.set("")

    def keluar_dari_sistem():
        root.destroy()

    def about_us():
        about_window = Toplevel(root)
        about_window.geometry("600x250")
        about_window.title("About Us")
        about_window.configure(bg="#F5F5F5")

        about_text = """         Anggota kelompok:
        1. Sri Endang Purnomo Wati - 182221007
        2. Maria Nathalia Zaneta - 182221031
        3. Erviera Rhohmatul Aini - 182221054
        4. Santi Dwi Kristiani - 182221079
             
        😃 Fisika Komputasi Mudah dan Menyenangkan Bukan!? 😃"""
        about_lbl = Label(about_window, text=about_text, font=('Calibri', 16, 'bold'), bg="#F5F5F5", fg="black", justify=LEFT)
        about_lbl.pack(padx=5, pady=20)

    def validasi_input2():
        try:
            tekananValue = tekanan.get()
            tekanan_value = int(tekananValue.split('/')[0])
            detak_jatung_value = int(detak_jatung.get())
            kalori_value = int(kalori.get())
            usia_value = int(usia.get())

            tekanan_status = ""
            tekanan_recommendation = ""
            if tekanan_value <= 89:
                tekanan_status = "Gawat! Tekanan darah anda rendah."
                tekanan_recommendation = ("<<Disarankan untuk meningkatkan asupan garam dan cairan.\n"
                "Konsumsi makanan yang kaya akan elektrolit seperti pisang.\n"
                "Hindari berdiri terlalu lama atau berdiri dengan cepat dari posisi duduk.\n"
                "Kenakan stoking kompresi.\n"
                "Konsultasi ke dokter jika perlu>>")
            elif  90 <= tekanan_value <= 139:
                tekanan_status = "Yeay! Tekanan darah normal."
                tekanan_recommendation = "Pertahankan gaya hidup sehat anda!"
            else:
                tekanan_status = "Gawat! Tekanan darah tinggi."
                tekanan_recommendation = ("<<Disarankan untuk mengurangi asupan garam dan lemak.\n"
                "Hindari makanan olahan dan berlemak.\n"
                "Perbanyak konsumsi buah, sayuran, dan biji-bijian.\n"
                "Rutin berolahraga, minimal 30 menit sehari.\n"
                "Hindari stres dan praktikkan teknik relaksasi.\n"
                "Berkonsultasi dengan dokter untuk penanganan lebih lanjut.>>")

            detak_jantung_status = ""
            detak_jantung_recommendation = ""
            if 1 <= usia_value <= 35:
                if 95 <= detak_jatung_value <= 170:
                    detak_jantung_status = "Detak jantung anda normal."
                    detak_jantung_recommendation = "Pertahankan gaya hidup sehat!"
                else:
                    detak_jantung_status = "Detak jantung anda tidak normal."
                    detak_jantung_recommendation = (
                    "<<Hindari stres dan praktikkan teknik relaksasi.\n"
                    "Rutin berolahraga ringan seperti berjalan atau bersepeda.\n"
                    "Hindari kafein dan alkohol.\n"
                    "Berkonsultasi dengan dokter untuk pemeriksaan lebih lanjut>>"
                )
            elif 35 < usia_value <= 50:
                if 85 <= detak_jatung_value <= 155:
                    detak_jantung_status = "Detak jantung anda normal."
                    detak_jantung_recommendation = "Pertahankan gaya hidup sehat."
                else:
                    detak_jantung_status = "Detak jantung anda tidak normal."
                    detak_jantung_recommendation = (
                    "<<Hindari stres dan praktikkan teknik relaksasi.\n"
                    "Rutin berolahraga ringan seperti berjalan atau bersepeda.\n"
                    "Hindari kafein dan alkohol.\n"
                    "Berkonsultasi dengan dokter untuk pemeriksaan lebih lanjut>>"
                )
            elif usia_value > 60:
                if 80 <= detak_jatung_value <= 130:
                    detak_jantung_status = "Detak jantung anda normal."
                    detak_jantung_recommendation = "Pertahankan gaya hidup sehat."
                else:
                    detak_jantung_status = "Detak jantung anda tidak normal."
                    detak_jantung_recommendation = (
                    "<<Hindari stres dan praktikkan teknik relaksasi.\n"
                    "Rutin berolahraga ringan seperti berjalan atau bersepeda.\n"
                    "Hindari kafein dan alkohol.\n"
                    "Berkonsultasi dengan dokter untuk pemeriksaan lebih lanjut>>"
                )
            else:
                detak_jantung_status = "Usia tidak valid untuk pengecekan detak jantung"
                detak_jantung_recommendation = "Periksa kembali data usia Anda."

            kalori_status = "Kalori normal" if 500 <= kalori_value <= 750 else "Kalori tidak normal"
            kalori_recommendation = "Pertahankan asupan kalori yang seimbang." if kalori_status == "Kalori normal" else ( "<<Disarankan untuk menyesuaikan asupan kalori sesuai kebutuhan harian.\n"
            "Konsultasikan dengan ahli gizi untuk rencana makan yang sesuai.\n"
            "Pastikan asupan makanan mengandung karbohidrat kompleks, protein, dan lemak sehat.\n"
            "Hindari makanan berkalori tinggi namun rendah nutrisi seperti junk food.>>"
        )

            messagebox.showinfo(
                "Info Kesehatan",
                f"{tekanan_status}\n{tekanan_recommendation}\n\n"
                f"{detak_jantung_status}\n{detak_jantung_recommendation}\n\n"
                f"{kalori_status}\n{kalori_recommendation}",
                icon='info'
            )

        except ValueError:
            messagebox.showerror("Error", "Tekanan, Detak Jantung, dan Kalori harus berupa angka positif!")

    def validasi_input():
        if not all([nama.get(), usia.get(), jenis_kelamin.get(), tinggi_badan.get(), berat_badan.get(), preferensi_aktivitas.get()]):
            messagebox.showerror("Error", "Isi semua data yang diperlukan untuk masuk!")
        else:
            try:
                usia_value = int(usia.get())
                tinggi_badan_value = int(tinggi_badan.get())
                berat_badan_value = int(berat_badan.get())

                if usia_value < 0 or tinggi_badan_value < 0 or berat_badan_value < 0:
                    raise ValueError("Nilai harus lebih besar dari 0")

                messagebox.showinfo("Validasi Sukses", "Data berhasil divalidasi!", icon='info')
                preferensi_aktivitas_lbl.grid_remove()
                preferensi_aktivitas_txt.grid_remove()
                nama_lbl.grid_remove()            
                nama_txt.grid_remove()
                usia_lbl.grid_remove()            
                usia_txt.grid_remove()            
                jenis_kelamin_lbl.grid_remove()
                jenis_kelamin_txt.grid_remove()
                tinggi_badan_lbl.grid_remove()
                tinggi_badan_txt.grid_remove()
                berat_badan_lbl.grid_remove()
                berat_badan_txt.grid_remove()
                about_btn.grid_remove()
                exit_btn.grid_remove()
                reset_btn.grid_remove()
                masuk_btn.grid_remove()

                tekanan_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Tekanan Darah (mmHg)", bd=3, anchor=W, bg="#96D2D9", fg="#233758")
                tekanan_lbl.grid(row=0, column=0, sticky='w', pady=10)
                tekanan_txt = Entry(frame_kiri, font=('Lucida Sans', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=tekanan, width=30)
                tekanan_txt.grid(row=0, column=1, pady=10, padx=(10, 0))

                detak_jatung_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Detak Jantung (bpm)", bd=3, anchor=W, bg="#96D2D9", fg="#233758")
                detak_jatung_lbl.grid(row=1, column=0, sticky='w', pady=10)
                detak_jatung_txt = Entry(frame_kiri, font=('Lucida Sans', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=detak_jatung, width=30)
                detak_jatung_txt.grid(row=1, column=1, pady=10, padx=(10, 0))

                kalori_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Kalori (kkal)", bd=3, anchor=W, bg="#96D2D9", fg="#233758")
                kalori_lbl.grid(row=2, column=0, sticky='w', pady=10)
                kalori_txt = Entry(frame_kiri, font=('Lucida Sans', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=kalori, width=30)
                kalori_txt.grid(row=2, column=1, pady=10, padx=(10, 0))

                tess_btn = Button(frame_kiri, font=('Cambria', 16, 'bold'), text="Tes", bg="#F1F1F1", fg="black", relief="ridge", bd=3, padx=6, pady=6, width=12, command=validasi_input2, overrelief="solid", highlightthickness=1, highlightbackground="#FFD39B")
                tess_btn.grid(row=3, column=3, pady=20, padx=(0, 10), sticky='w')

                keluar_btn = Button(frame_kiri, font=('Cambria', 16, 'bold'), text="Keluar", bg="#F1F1F1", fg="black", relief="ridge", overrelief="solid", bd=3, padx=6, pady=6, width=12, command=keluar_dari_sistem, highlightthickness=1, highlightbackground="#FFD39B")
                keluar_btn.grid(row=3, column=4, pady=20, padx=(0, 10), sticky='w')

            except ValueError:
                messagebox.showerror("Error", "Usia, Tinggi Badan, dan Berat Badan harus berupa angka positif!")

    frame_atas = Frame(root, width=1460, height=150, bg="#96D2D9")
    frame_atas.pack(padx=20, pady=20, fill=X)

    main_lbl = Label(frame_atas, font=('Georgia', 20, 'bold'), text="FITNESS TRACKING", fg="#233758", anchor=CENTER, bg="#96D2D9")
    main_lbl.grid(row=0, column=0, columnspan=2, sticky='ew', pady=10)

    path_gambar = "C:/Users/Rafly/Desktop/terus.jpg"
    gambar = Image.open(path_gambar)
    ukuran_baru = (1460, 120)
    gambar_terubah = gambar.resize(ukuran_baru)
    photo = ImageTk.PhotoImage(gambar_terubah)
    label_gambar = Label(frame_atas, image=photo)
    label_gambar.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10)

    frame_kiri = Frame(root, width=600, height=400, bg="#96D2D9")
    frame_kiri.pack(padx=20, pady=20, anchor='w')

    nama_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Nama", bd=3, anchor=W, bg="#96D2D9", fg="#233758")
    nama_lbl.grid(row=0, column=0, sticky='w', pady=10)
    nama_txt = Entry(frame_kiri, font=('Franklin Gothic Book', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=nama, width=30)
    nama_txt.grid(row=0, column=1, pady=10, padx=(10, 0))

    usia_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Usia", bd=3, anchor=W, bg="#96D2D9", fg="#233758")
    usia_lbl.grid(row=1, column=0, sticky='w', pady=10)
    usia_txt = Entry(frame_kiri, font=('Franklin Gothic Book', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=usia, width=30)
    usia_txt.grid(row=1, column=1, pady=10, padx=(10, 0))

    jenis_kelamin_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Jenis Kelamin (P/L)", bd=3, anchor=W, bg="#96D2D9", fg="#233758")
    jenis_kelamin_lbl.grid(row=2, column=0, sticky='w', pady=10)
    jenis_kelamin_txt = Entry(frame_kiri, font=('Franklin Gothic Book', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=jenis_kelamin, width=30)
    jenis_kelamin_txt.grid(row=2, column=1, pady=10, padx=(10, 0))

    tinggi_badan_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Tinggi Badan (cm)", bd=3, anchor=W, bg="#96D2D9", fg="#233758")
    tinggi_badan_lbl.grid(row=3, column=0, sticky='w', pady=10)
    tinggi_badan_txt = Entry(frame_kiri, font=('Franklin Gothic Book', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=tinggi_badan, width=30)
    tinggi_badan_txt.grid(row=3, column=1, pady=10, padx=(10, 0))

    berat_badan_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Berat Badan (kg)", bd=3, anchor=W, bg="#96D2D9", fg="#233758")
    berat_badan_lbl.grid(row=4, column=0, sticky='w', pady=10)
    berat_badan_txt = Entry(frame_kiri, font=('Franklin Gothic Book', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=berat_badan, width=30)
    berat_badan_txt.grid(row=4, column=1, pady=10, padx=(10, 0))

    preferensi_aktivitas_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Preferensi Aktivitas", bd=3, anchor=W, bg="#96D2D9", fg="#233758")
    preferensi_aktivitas_lbl.grid(row=5, column=0, sticky='w', pady=10)
    preferensi_aktivitas_txt = Entry(frame_kiri, font=('Franklin Gothic Book', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=preferensi_aktivitas, width=30)
    preferensi_aktivitas_txt.grid(row=5, column=1, pady=10, padx=(10, 0))

    about_btn = Button(frame_kiri, font=('Rockwell', 16, 'bold'), text="About Us", bg="#F1F1F1", fg="black", relief="ridge", bd=3, padx=6, pady=6, width=12, command=about_us, overrelief="solid", highlightthickness=1, highlightbackground="#FFD39B")
    about_btn.grid(row=6, column=0, pady=20, padx=(0, 10), sticky='w')

    exit_btn = Button(frame_kiri, font=('Rockwell', 16, 'bold'), text="Keluar", bg="#F1F1F1", fg="black", relief="ridge", overrelief="solid", bd=3, padx=6, pady=6, width=12, command=keluar_dari_sistem, highlightthickness=1, highlightbackground="#FFD39B")
    exit_btn.grid(row=6, column=1, pady=20, padx=(0, 10), sticky='w')

    reset_btn = Button(frame_kiri, font=('Rockwell', 16, 'bold'), text="Hapus", bg="#F1F1F1", fg="black", relief="ridge", bd=3, padx=6, pady=6, width=12, command=reset, overrelief="solid", highlightthickness=1, highlightbackground="#FFD39B")
    reset_btn.grid(row=6, column=2, pady=20, padx=(0, 10), sticky='w')

    masuk_btn = Button(frame_kiri, font=('Rockwell', 16, 'bold'), text="Masuk", bg="#F1F1F1", fg="black", relief="ridge", bd=3, padx=6, pady=6, width=12, command=validasi_input, overrelief="solid", highlightthickness=1, highlightbackground="#FFD39B")
    masuk_btn.grid(row=6, column=3, pady=20, padx=(0, 10), sticky='w')

    root.mainloop()

sistem_tracking()
