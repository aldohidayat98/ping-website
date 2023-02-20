import tkinter as tk
from ping3 import ping
import threading
import time

class PingApp:
    def __init__(self, root):  
        self.root = root
        self.label = tk.Label(self.root, text="Waiting for ping...", font=("Arial", 11))
        self.label.pack(padx=10, pady=10)
        self.label1 = tk.Label(self.root, text="Waiting for ping...", font=("Arial", 11))
        self.label1.pack(padx=10, pady=10)
        self.label2 = tk.Label(self.root, text="Waiting for ping...", font=("Arial", 11))
        self.label2.pack(padx=10, pady=10)
        self.label3 = tk.Label(self.root, text="Waiting for ping...", font=("Arial", 11))
        self.label3.pack(padx=10, pady=10)
        self.ping_thread = threading.Thread(target=self.run_ping, daemon=True)
        self.ping_thread.start()
        

    def run_ping(self):
        # website yang akan di Ping
        website = ["nms.scm.co.id", "tt.scm.co.id", "pm.scm.co.id", "nis.scm.co.id"]

        #Waktu Sekarang
        current_time = time.strftime("%B %Y", time.localtime())

        # Membuka file notepad dengan mode write
        file = open(f"Log-Website-{current_time}.txt", 'w')

        while True:
            #Waktu Sekarang
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            
            #respon website
            response_time = ping(website[0])
            response_time1 = ping(website[1])
            response_time2 = ping(website[2])
            response_time3 = ping(website[3])
            
            if response_time is not None:
                f_response_time = "{:.4f}".format(response_time)
                hasil = (f"{current_time} | {website[0]} | Connected | {f_response_time} ms")
                self.label.config(text=hasil, fg="green")
            else:
                hasil = (f"{current_time} | {website[0]} | Lost Connected ")
                self.label.config(text=hasil, fg="red")
                
            if response_time1 is not None:
                f_response_time1 = "{:.4f}".format(response_time1)
                hasil1 = (f"{current_time} | {website[1]} | Connected | {f_response_time1} ms")
                self.label1.config(text=hasil1, fg="green")
            else:
                hasil1 = (f"{current_time} | {website[1]} | Lost Connected ")
                self.label1.config(text=hasil1, fg="red")
                
            if response_time2 is not None:
                f_response_time2 = "{:.4f}".format(response_time2)
                hasil2 = (f"{current_time} | {website[2]} | Connected | {f_response_time2} ms")
                self.label2.config(text=hasil2, fg="green")
            else:
                hasil2 = (f"{current_time} | {website[2]} | Lost Connected ")
                self.label2.config(text=hasil2, fg="red")
                
            if response_time3 is not None:
                f_response_time3 = "{:.4f}".format(response_time3)
                hasil3 = (f"{current_time} | {website[3]} | Connected | {f_response_time3} ms")
                self.label3.config(text=hasil3, fg="green")
            else:
                hasil3 = (f"{current_time} | {website[3]} | Lost Connected ")
                self.label3.config(text=hasil3, fg="red")
            
            # Mengambil teks yang ingin disimpan ke notepad
            data = (f"{hasil}\n{hasil1}\n{hasil2}\n{hasil3}\n")

            # Menyimpan teks ke dalam notepad
            file.write(data)
            file.flush()
    
            time.sleep(30)

root = tk.Tk()
app = PingApp(root)

# Atur Title dan Ukuran Maxsize
root.title("PING WEBSITE NMS TT PM NIS")
root.minsize(450, 180)
root.maxsize(450, 180)
root.resizable(False, False)

root.mainloop()
