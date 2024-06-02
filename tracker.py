from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def sistem_tracking():
    root = Tk()
    root.geometry("600x400")
    root.title("Input Data Pribadi")
    root.configure(bg="#233758")
    root.attributes('-fullscreen', True)

    nama = StringVar()
    usia = StringVar()
    jenis_kelamin = StringVar()
    tinggi_badan = StringVar()
    berat_badan = StringVar()
    preferensi_aktivitas = StringVar()

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

                messagebox.showinfo("Validasi Sukses", "Data berhasil divalidasi!")

            except ValueError:
                messagebox.showerror("Error", "Usia, Tinggi Badan, dan Berat Badan harus berupa angka positif!")

    frame_atas = Frame(root, width=600, height=150, bg="#233758")
    frame_atas.pack(padx=20, pady=20, fill=X)

    main_lbl = Label(frame_atas, font=('Helvetica', 25, 'bold'), text="FITNESS TRACKING", fg="#FFFFFF", anchor=CENTER, bg="#233758")
    main_lbl.grid(row=0, column=0, columnspan=2, sticky='ew', pady=10)

    path_gambar = "C:/Users/Rafly/Desktop/lari.jpg"
    gambar = Image.open(path_gambar)
    ukuran_baru = (1400, 120)
    gambar_terubah = gambar.resize(ukuran_baru)
    photo = ImageTk.PhotoImage(gambar_terubah)
    label_gambar = Label(frame_atas, image=photo)
    label_gambar.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10)

    frame_kiri = Frame(root, width=600, height=400, bg="#233758")
    frame_kiri.pack(padx=20, pady=20, anchor='w')

    nama_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Nama Lengkap", bd=3, anchor=W, bg="#233758", fg="white")
    nama_lbl.grid(row=0, column=0, sticky='w', pady=10)
    nama_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=nama, width=30)
    nama_txt.grid(row=0, column=1, pady=10, padx=(10, 0))

    usia_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Usia", bd=3, anchor=W, bg="#233758", fg="white")
    usia_lbl.grid(row=1, column=0, sticky='w', pady=10)
    usia_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=usia, width=30)
    usia_txt.grid(row=1, column=1, pady=10, padx=(10, 0))

    jenis_kelamin_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Jenis Kelamin", bd=3, anchor=W, bg="#233758", fg="white")
    jenis_kelamin_lbl.grid(row=2, column=0, sticky='w', pady=10)
    jenis_kelamin_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=jenis_kelamin, width=30)
    jenis_kelamin_txt.grid(row=2, column=1, pady=10, padx=(10, 0))

    tinggi_badan_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Tinggi Badan (cm)", bd=3, anchor=W, bg="#233758", fg="white")
    tinggi_badan_lbl.grid(row=3, column=0, sticky='w', pady=10)
    tinggi_badan_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=tinggi_badan, width=30)
    tinggi_badan_txt.grid(row=3, column=1, pady=10, padx=(10, 0))

    berat_badan_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Berat Badan (kg)", bd=3, anchor=W, bg="#233758", fg="white")
    berat_badan_lbl.grid(row=4, column=0, sticky='w', pady=10)
    berat_badan_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=berat_badan, width=30)
    berat_badan_txt.grid(row=4, column=1, pady=10, padx=(10, 0))

    preferensi_aktivitas_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Preferensi Aktivitas", bd=3, anchor=W, bg="#233758", fg="white")
    preferensi_aktivitas_lbl.grid(row=5, column=0, sticky='w', pady=10)
    preferensi_aktivitas_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=preferensi_aktivitas, width=30)
    preferensi_aktivitas_txt.grid(row=5, column=1, pady=10, padx=(10, 0))

    about_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="About Us", bg="#F1F1F1", fg="black", relief="ridge", bd=3, padx=6, pady=6, width=12, command=about_us, overrelief="solid", highlightthickness=1, highlightbackground="#FFD39B")
    about_btn.grid(row=6, column=0, pady=20, padx=(0, 10), sticky='w')

    exit_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="Keluar", bg="#F1F1F1", fg="black", relief="ridge", overrelief="solid", bd=3, padx=6, pady=6, width=12, command=keluar_dari_sistem, highlightthickness=1, highlightbackground="#FFD39B")
    exit_btn.grid(row=6, column=1, pady=20, padx=(0, 10), sticky='w')

    reset_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="Hapus", bg="#F1F1F1", fg="black", relief="ridge", bd=3, padx=6, pady=6, width=12, command=reset, overrelief="solid", highlightthickness=1, highlightbackground="#FFD39B")
    reset_btn.grid(row=6, column=2, pady=20, padx=(0, 10), sticky='w')

    masuk_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="Masuk", bg="#F1F1F1", fg="black", relief="ridge", bd=3, padx=6, pady=6, width=12, command=validasi_input, overrelief="solid", highlightthickness=1, highlightbackground="#FFD39B")
    masuk_btn.grid(row=6, column=3, pady=20, padx=(0, 10), sticky='w')

    root.mainloop()

sistem_tracking()