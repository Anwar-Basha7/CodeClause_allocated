import tkinter as tk
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Email Application")

        self.sender_email = tk.StringVar()
        self.receiver_email = tk.StringVar()
        self.subject = tk.StringVar()

        ttk.Label(master, text="Sender Email:", foreground="blue").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(master, textvariable=self.sender_email).grid(row=0, column=1, columnspan=2, pady=5)

        ttk.Label(master, text="Receiver Email:", foreground="blue").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(master, textvariable=self.receiver_email).grid(row=1, column=1, columnspan=2, pady=5)

        ttk.Label(master, text="Subject:", foreground="blue").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Entry(master, textvariable=self.subject).grid(row=2, column=1, columnspan=2, pady=5)

        ttk.Label(master, text="Message:", foreground="blue").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.message_entry = tk.Text(master, height=10, width=40)
        self.message_entry.grid(row=3, column=1, columnspan=2, pady=5)

        ttk.Button(master, text="Send Email", command=self.send_email, style='Send.TButton').grid(row=4, column=1, pady=10)
        ttk.Button(master, text="Exit", command=master.destroy, style='Exit.TButton').grid(row=4, column=2, pady=10)

    def send_email(self):
        sender_email = self.sender_email.get()
        receiver_email = self.receiver_email.get()
        subject = self.subject.get()
        message = self.message_entry.get("1.0", tk.END)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            #here i have hidden login credentials for privacy pupose
            server.login('sendmedocument****@gmail.com', '*********************')
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()

            self.sender_email.set('')
            self.receiver_email.set('')
            self.subject.set('')
            self.message_entry.delete("1.0", tk.END)
            print("Email sent successfully!")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()

    style = ttk.Style()
    style.configure('Send.TButton', foreground='white', background='green', font=('Arial', 10, 'bold'))
    style.configure('Exit.TButton', foreground='white', background='red', font=('Arial', 10, 'bold'))

    app = EmailApp(root)
    root.mainloop()
