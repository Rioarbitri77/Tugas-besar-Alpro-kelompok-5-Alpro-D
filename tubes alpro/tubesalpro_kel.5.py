import tkinter as tk
from tkinter import messagebox
from tkinter import *
from datetime import datetime, timedelta

class BioskopApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Tiket.tix")
        self.window.geometry("600x600")  # Ukuran jendela yang lebih besar
        self.window.configure(bg="#FFFFFF")  # Warna latar belakang putih agar terlihat lebih bersih

        self.selected_seats = []  # Menyimpan kursi yang dipilih
        self.total_harga = 0  # Total harga yang harus dibayar

        self.show_login()  # Tampilkan frame login saat aplikasi dimulai

    def show_login(self):
        # Hapus frame sebelumnya jika ada
        self.clear_frame()

        # Tampilkan frame login
        self.login_frame = tk.Frame(self.window, bg="#FFFFFF")
        self.login_frame.pack(padx=20, pady=20)

        # Label judul Selamat Datang
        self.label_welcome = tk.Label(self.login_frame, text="Welcome to Tiket.tix", bg="#FFFFFF", fg="#000000", font=("Arial", 18, "bold"))
        self.label_welcome.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Label judul Login
        self.label_title = tk.Label(self.login_frame, text="Log In", bg="#FFFFFF", fg="#000000", font=("Arial", 24, "bold"))
        self.label_title.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # Tambahkan elemen-elemen login
        self.label_username = tk.Label(self.login_frame, text="Username", bg="#FFFFFF", fg="#888888", font=("Arial", 12))
        self.label_username.grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
        self.entry_username = tk.Entry(self.login_frame, font=("Arial", 12), bg="#F0F0F0", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.entry_username.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 20), ipadx=5, ipady=5)

        self.label_password = tk.Label(self.login_frame, text="Kata Sandi", bg="#FFFFFF", fg="#888888", font=("Arial", 12))
        self.label_password.grid(row=4, column=0, columnspan=2, sticky="w", padx=10)
        self.entry_password = tk.Entry(self.login_frame, show="*", font=("Arial", 12), bg="#F0F0F0", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.entry_password.grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 20), ipadx=5, ipady=5)

        # Tombol Lupa Kata Sandi
        self.button_forgot_password = tk.Button(self.login_frame, text="Lupa kata sandi?", bg="#FFFFFF", fg="#1E90FF", font=("Arial", 10), relief="flat", cursor="hand2", command=self.forgot_password)
        self.button_forgot_password.grid(row=6, column=0, columnspan=2, pady=(0, 20), sticky="e", padx=10)

        # Tombol Login
        self.button_login = tk.Button(self.login_frame, text="Log In", command=self.login, bg="#1E90FF", fg="white", font=("Arial", 12), relief="flat", cursor="hand2", padx=10, pady=10)
        self.button_login.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

        # Tombol Register
        self.button_register = tk.Button(self.login_frame, text="Register", command=self.register, bg="#FFFFFF", fg="#1E90FF", font=("Arial", 12), relief="flat", cursor="hand2", padx=10, pady=10)
        self.button_register.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username and password:  # Hanya contoh sederhana
            messagebox.showinfo("Login", f"Logged in as {username}")
            self.show_ticket_booking_menu()  # Tampilkan menu pemesanan tiket setelah login berhasil
        else:
            messagebox.showerror("Login Failed", "Please enter both username and password")

    def register(self):
        messagebox.showinfo("Register", "Registrasi berhasil!")

    def forgot_password(self):
        messagebox.showinfo("Lupa Kata Sandi", "Fitur lupa kata sandi belum tersedia.")

    def clear_frame(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def show_ticket_booking_menu(self):
        self.clear_frame()

        self.booking_frame = tk.Frame(self.window, bg="#F4F4F4")  # Ubah warna latar belakang
        self.booking_frame.pack(padx=20, pady=20)

        # Judul
        title_label = tk.Label(self.booking_frame, text="Now Showing on Cinemas", bg="#F4F4F4", fg="#333333", font=("Arial", 20, "bold"))  # Ubah warna teks
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="nsew")  # Perbaiki grid layout

        movies = [
            {"title": "Barbie", "poster": "Barbie poster.png", "rating": "4.5", "synopsis": "Barbie adalah seorang putri yang penuh dengan petualangan fantastis dan cerita menarik.", "age_rating": "SU",
            "producer": "margot robbie, tom ackerley and robbie brenner", "director": "Greta gerwig", "writer": "Greta gerwig and Noah baumbach", "cast": ["Ryan gosling", "Margot robbie"], "distributor": ""},
            {"title": "Oppenheimer", "poster": "Oppenheimer poster.png", "rating": "4.8", "synopsis": "Oppenheimer adalah seorang fisikawan teoretis Amerika yang dikenal karena memimpin pengembangan bom atom selama Perang Dunia II.", "age_rating": "17+",
            "producer": "Emma thomas, charles roven, christopher nolan", "director": "Christhopher Nolan", "writer": "Kai bird and martin J. sherwin", "cast": ["Cillian murphy", "Emily blunt"], "distributor": "Universal pictures"},
            {"title": "Interstellar", "poster": "interstelar poster.png", "rating": "4.9", "synopsis": "Interstellar adalah film fiksi ilmiah yang disutradarai oleh Christopher Nolan, mengikuti sekelompok penjelajah antariksa dalam pencarian planet baru untuk manusia.", "age_rating": "13+",
            "producer": "Emma thomas, Christopher Nolan and Lynda obst", "director": "Christopher Nolan", "writer": "Jonathan nolan and christopher Nolan", "cast": ["Matthew McConaughey", "Anne hathaway"], "distributor": "Paramount pictures"},
        ]
        
        # Loop untuk menampilkan setiap film
        for i, movie in enumerate(movies):
            # Tampilkan gambar poster film
            poster_image = self.load_image(movie["poster"])
            if poster_image:
                poster_image = poster_image.subsample(3)  # Sesuaikan ukuran poster
                poster_button = tk.Button(self.booking_frame, image=poster_image, bg="#FFFFFF", bd=2, relief="groove", command=lambda m=movie: self.show_movie_info(m))
                poster_button.grid(row=i // 3 + 1, column=i % 3, padx=10, pady=10)
                poster_button.image = poster_image
                poster_button.config(cursor="hand2")  # Ubah kursor saat dihover

                # Tampilkan judul film
                title_label = tk.Label(self.booking_frame, text=movie["title"], bg="#F4F4F4", fg="#333333", font=("Arial", 12, "bold"))  # Ubah warna teks
                title_label.grid(row=i // 3 + 2, column=i % 3, sticky="nsew")

        # Konfigurasi ukuran kolom dan baris
        self.booking_frame.grid_columnconfigure(tuple(range(3)), weight=1)
        self.booking_frame.grid_rowconfigure(tuple(range(len(movies) // 3 + 2)), weight=1)

    def show_movie_info(self, movie):
        messagebox.showinfo("Movie Info", f"Title: {movie['title']}\nSynopsis: {movie['synopsis']}")

    def load_image(self, filename):
        try:
            image = tk.PhotoImage(file=filename)
            return image
        except tk.TclError:
            print(f"Error: Unable to load image: {filename}")
            return None

    def show_movie_info(self, selected_movie):
        # Hapus frame sebelumnya jika ada
        self.clear_frame()

        # Tampilkan frame informasi film
        self.movie_info_frame = tk.Frame(self.window, bg="#FFFFFF")
        self.movie_info_frame.pack(padx=20, pady=20)

        # Tampilkan poster film di sebelah kiri
        poster_image = self.load_image(selected_movie["poster"]).subsample(4)  # Ukuran poster menjadi lebih kecil
        self.poster_label = tk.Label(self.movie_info_frame, image=poster_image, bg="#FFFFFF")
        self.poster_label.grid(row=0, column=0, rowspan=5, padx=(0, 20))
        self.poster_label.image = poster_image

        # Tampilkan judul
        self.label_title = tk.Label(self.movie_info_frame, text=f"{selected_movie['title']}", bg="#FFFFFF", fg="#333333", font=("Arial", 24, "bold"))
        self.label_title.grid(row=0, column=1, columnspan=2, sticky="w", pady=(0, 10))

        # Tampilkan sinopsis
        self.label_synopsis = tk.Label(self.movie_info_frame, text=f"{selected_movie['synopsis']}", bg="#FFFFFF", fg="#666666", font=("Arial", 14), wraplength=400, justify="left")
        self.label_synopsis.grid(row=1, column=1, columnspan=2, sticky="w", pady=(0, 10))

        # Tampilkan informasi tambahan tentang film
        additional_info = f"Produser: {selected_movie.get('producer', 'N/A')}\n" \
                        f"Sutradara: {selected_movie.get('director', 'N/A')}\n" \
                        f"Penulis: {selected_movie.get('writer', 'N/A')}\n" \
                        f"Pemain: {', '.join(selected_movie.get('cast', ['N/A']))}\n" \
                        f"Distributor: {selected_movie.get('distributor', 'N/A')}"
        self.label_additional_info = tk.Label(self.movie_info_frame, text=additional_info, bg="#FFFFFF", fg="#666666", font=("Arial", 14), justify="left")
        self.label_additional_info.grid(row=2, column=1, columnspan=2, sticky="w", pady=(0, 10))

        # Tampilkan tombol pilih tempat
        self.button_select_cinema = tk.Button(self.movie_info_frame, text="Pilih Tempat", bg="#1E90FF", fg="#FFFFFF", font=("Arial", 16, "bold"), command=lambda: self.show_cinema_selection(selected_movie))
        self.button_select_cinema.grid(row=3, column=1, pady=(10, 0), padx=(0, 10), sticky="w")

        # Tampilkan tombol kembali
        back_button = tk.Button(self.movie_info_frame, text="Kembali", bg="#FF0000", fg="#FFFFFF", font=("Arial", 16, "bold"), command=self.show_ticket_booking_menu)
        back_button.grid(row=3, column=2, pady=(10, 0), sticky="e")

    def show_cinema_selection(self, selected_movie):
        # Hapus frame sebelumnya jika ada
        self.clear_frame()

        # Tampilkan frame pilihan tempat
        self.cinema_frame = tk.Frame(self.window)
        self.cinema_frame.pack(padx=20, pady=20)

        # Tampilkan label tempat
        self.label_cinema = tk.Label(self.cinema_frame, text="Pilih Tempat:", fg="black", font=("Arial", 16, "bold"))
        self.label_cinema.grid(row=0, columnspan=2, pady=10)

        # Tampilkan daftar bioskop
        cinemas = [
            {"name": "E-WALK XXI", "location": "Jl. Basuki Rahmat No. 8, Surabaya"},
            {"name": "PENTACITY XXI", "location": "Jl. Pemuda No. 123, Surabaya"}
        ]
        for i, cinema in enumerate(cinemas):
            cinema_button = tk.Button(self.cinema_frame, text=cinema["name"], font=("Arial", 14, "bold"),
                                    command=lambda c=cinema["name"], loc=cinema["location"]: self.show_showtime_selection(selected_movie, c, loc))
            cinema_button.grid(row=i+1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
            location_label = tk.Label(self.cinema_frame, text=cinema["location"], fg="#555555", font=("Arial", 12))
            location_label.grid(row=i+1, column=2, padx=(0, 10), pady=5, sticky="w")

    def show_showtime_selection(self, selected_movie, selected_cinema, cinema_location):
        self.clear_frame()

        self.showtime_frame = tk.Frame(self.window)
        self.showtime_frame.pack(padx=20, pady=20)

        self.label_title_cinema = tk.Label(self.showtime_frame, text=f"{selected_movie['title']} di {selected_cinema}", fg="black", font=("Arial", 16, "bold"))
        self.label_title_cinema.grid(row=0, columnspan=2, pady=10)

        self.label_location = tk.Label(self.showtime_frame, text=f"({cinema_location})", fg="#555555", font=("Arial", 12))
        self.label_location.grid(row=0, column=2, padx=(0, 10), pady=10, sticky="w")

        self.label_showtime = tk.Label(self.showtime_frame, text="Pilih Waktu:", fg="black", font=("Arial", 14))
        self.label_showtime.grid(row=1, columnspan=3, pady=10)

        # Mengambil tanggal 1 hari dari sekarang
        tomorrow = datetime.now() + timedelta(days=1)
        date_str = tomorrow.strftime("%d %B %Y")

        self.label_date = tk.Label(self.showtime_frame, text=f"Tanggal: {date_str}", fg="black", font=("Arial", 12))
        self.label_date.grid(row=2, columnspan=3, pady=5)

        showtimes = ["10:00", "13:00", "15:00", "18:00", "21:00"]
        for i, time in enumerate(showtimes):
            time_button = tk.Button(self.showtime_frame, text=time, font=("Arial", 14, "bold"), bg="#FFA500", fg="white",
                                    command=lambda t=time: self.show_seat_selection(selected_movie, selected_cinema, cinema_location, t))
            time_button.grid(row=i+3, columnspan=3, padx=10, pady=5, sticky="ew")

    def show_seat_selection(self, selected_movie, selected_cinema, cinema_location, selected_showtime):
        self.clear_frame()

        self.seat_frame = tk.Frame(self.window)
        self.seat_frame.pack(padx=20, pady=20)

        self.label_seat = tk.Label(self.seat_frame, text="Pilih Kursi:", fg="black", font=("Arial", 14))
        self.label_seat.grid(row=0, columnspan=8, pady=10)

        rows = 6
        columns = 8
        self.seat_buttons = {}

        for row in range(rows):
            for col in range(columns):
                seat_num = f"{chr(65 + row)}{col + 1}"
                seat_button = tk.Button(self.seat_frame, text=seat_num, width=4, height=2, bg="green", fg="white", 
                                        command=lambda s=seat_num: self.select_seat(selected_movie, selected_cinema, selected_showtime, s))
                seat_button.grid(row=row + 1, column=col, padx=5, pady=5)
                self.seat_buttons[seat_num] = seat_button

        screen_label = tk.Label(self.seat_frame, text="Layar Bioskop", bg="#FFFFFF", fg="#000000", font=("Arial", 10), width=10, height=2, relief="solid")
        screen_label.grid(row=rows + 1, columnspan=columns, pady=10)

    def select_seat(self, selected_movie, selected_cinema, selected_showtime, selected_seat):
            if selected_seat not in self.selected_seats:
                self.selected_seats.append(selected_seat)
                self.seat_buttons[selected_seat].config(bg="red", state="disabled")

            for widget in self.seat_frame.winfo_children():
                widget.destroy()

            self.label_selected_seats = tk.Label(self.seat_frame, text="Kursi Dipilih:", fg="black", font=("Arial", 14))
            self.label_selected_seats.grid(row=0, columnspan=8, pady=10)

            selected_seats_str = ", ".join(self.selected_seats)
            self.label_seats = tk.Label(self.seat_frame, text=selected_seats_str, fg="black", font=("Arial", 12))
            self.label_seats.grid(row=1, columnspan=8, pady=5)

            continue_button = tk.Button(self.seat_frame, text="Lanjutkan", command=lambda: self.show_payment(selected_movie, selected_cinema, selected_showtime))
            continue_button.grid(row=2, columnspan=8, pady=10)

            # Tampilkan ulang tombol kursi yang telah dipilih
            for seat_num, seat_button in self.seat_buttons.items():
                seat_button.grid(row=int(seat_num[1:]) + 1, column=ord(seat_num[0]) - 65, padx=5, pady=5)
                if seat_num in self.selected_seats:
                    seat_button.config(bg="red", state="disabled")

    def clear_frame(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def show_payment(self, selected_movie, selected_cinema, selected_showtime):
        self.clear_frame()

        self.total_harga = len(self.selected_seats) * 50000

        # Buat frame untuk pembayaran
        self.payment_frame = tk.Frame(self.window, bg="white")
        self.payment_frame.pack(padx=20, pady=20)

        # Tampilkan label untuk memilih metode pembayaran
        label_payment = tk.Label(self.payment_frame, text="Pilih Metode Pembayaran:", fg="black", font=("Arial", 14), bg="white")
        label_payment.grid(row=0, columnspan=2, pady=10)

        # Daftar metode pembayaran
        payment_methods = ["Cash", "Debit"]
        for i, method in enumerate(payment_methods):
            payment_button = tk.Button(self.payment_frame, text=method, font=("Arial", 12),
                                    command=lambda m=method: self.show_payment_details(selected_movie, selected_cinema, selected_showtime, m))
            payment_button.grid(row=i+1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Tombol untuk kembali ke halaman utama
        home_button = tk.Button(self.payment_frame, text="Kembali ke Halaman Utama", font=("Arial", 12), command=self.show_ticket_booking_menu)
        home_button.grid(row=len(payment_methods)+1, column=0, columnspan=2, pady=10, sticky="ew")

    def show_payment_details(self, selected_movie, selected_cinema, selected_showtime, selected_method):
        self.clear_frame()

        # Buat frame untuk detail pembayaran
        self.payment_details_frame = tk.Frame(self.window, bg="white")
        self.payment_details_frame.pack(padx=20, pady=20)

        # Tampilkan label detail pembayaran
        label_payment_details = tk.Label(self.payment_details_frame, text="Detail Pembayaran:", fg="black", font=("Arial", 14), bg="white")
        label_payment_details.grid(row=0, columnspan=2, pady=10)

        # Tampilkan jumlah kursi yang dipilih dan total harga
        label_selected_seats = tk.Label(self.payment_details_frame, text=f"Jumlah Kursi: {len(self.selected_seats)}", fg="black", font=("Arial", 12), bg="white")
        label_selected_seats.grid(row=1, columnspan=2, pady=5)
        label_total_harga = tk.Label(self.payment_details_frame, text=f"Total Harga: Rp {self.total_harga}", fg="black", font=("Arial", 12), bg="white")
        label_total_harga.grid(row=2, columnspan=2, pady=5)

        # Tampilkan tanggal dan waktu penayangan
        showtime_date = (datetime.now() + timedelta(days=1)).strftime('%d-%m-%Y')
        label_showtime = tk.Label(self.payment_details_frame, text=f"Tanggal dan Waktu: {showtime_date} {selected_showtime}", fg="black", font=("Arial", 12), bg="white")
        label_showtime.grid(row=3, columnspan=2, pady=5)

        # Tombol untuk konfirmasi pembayaran dan kembali
        confirm_button = tk.Button(self.payment_details_frame, text="Konfirmasi Pembayaran", font=("Arial", 12),
                                command=lambda: self.confirm_payment(selected_movie, selected_cinema, selected_showtime, selected_method))
        confirm_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        back_button = tk.Button(self.payment_details_frame, text="Kembali", font=("Arial", 12), command=lambda: self.show_payment(selected_movie, selected_cinema, selected_showtime))
        back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")


    def confirm_payment(self, selected_movie, selected_cinema, selected_showtime, selected_method):
        self.clear_frame()

        self.confirmation_frame = tk.Frame(self.window, bg="white")
        self.confirmation_frame.pack(padx=20, pady=20)

        confirmation_text = (
            f"Film: {selected_movie['title']}\n"
            f"Bioskop: {selected_cinema}\n"
            f"Tanggal dan Waktu: {(datetime.now() + timedelta(days=1)).strftime('%d-%m-%Y')} {selected_showtime}\n"
            f"Kursi: {', '.join(self.selected_seats)}\n"
            f"Metode Pembayaran: {selected_method}\n"
            f"Total Harga: Rp {self.total_harga}"
        )

        label_confirmation = tk.Label(self.confirmation_frame, text="Pembayaran Berhasil", fg="black", font=("Arial", 14), bg="white")
        label_confirmation.grid(row=0, columnspan=2, pady=10)

        label_confirmation_details = tk.Label(self.confirmation_frame, text=confirmation_text, fg="black", font=("Arial", 12), bg="white")
        label_confirmation_details.grid(row=1, columnspan=2, pady=5)

        home_button = tk.Button(self.confirmation_frame, text="Kembali ke Halaman Utama", font=("Arial", 12), command=self.destroy_confirmation_frame)
        home_button.grid(row=2, columnspan=2, pady=10, sticky="ew")

    def destroy_confirmation_frame(self):
        if hasattr(self, 'confirmation_frame'):
            self.confirmation_frame.destroy()
        self.show_ticket_booking_menu()


    def clear_frame(self):
        # Hapus semua frame yang aktif
        if hasattr(self, 'login_frame'):
            self.login_frame.destroy()
        if hasattr(self, 'booking_frame'):
            self.booking_frame.destroy()
        if hasattr(self, 'movie_info_frame'):
            self.movie_info_frame.destroy()
        if hasattr(self, 'cinema_frame'):
            self.cinema_frame.destroy()
        if hasattr(self, 'showtime_frame'):
            self.showtime_frame.destroy()
        if hasattr(self, 'seat_frame'):
            self.seat_frame.destroy()
        if hasattr(self, 'payment_frame'):
            self.payment_frame.destroy()
        if hasattr(self, 'payment_details_frame'):
            self.payment_details_frame.destroy()



def main():
    window = tk.Tk()
    window.geometry("800x600")  # Ubah ukuran window agar cukup besar untuk menampilkan poster dan informasi film
    window.configure(bg="#1E90FF")  # Atur warna latar belakang
    app = BioskopApp(window)
    window.mainloop()
                           

if __name__ == "__main__":
    main()
