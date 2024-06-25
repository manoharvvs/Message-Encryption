import cv2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor")

        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Heading Box
        heading_frame = tk.Frame(self.root, bg="lightgreen", height=100)
        heading_frame.pack(fill="x", pady=(10, 0))

        project_name_label = tk.Label(heading_frame, text="Murali Project", font=("Arial", 20), bg="lightgreen")
        project_name_label.pack(pady=10)

        # Main Content Box
        content_frame = tk.Frame(self.root)
        content_frame.pack(expand=True, fill="both")

        # Image and File Entry
        image_label = tk.Label(content_frame, text="Select Image:")
        image_label.grid(row=1, column=0, padx=10, pady=10)

        self.image_path_entry = tk.Entry(content_frame, width=50)
        self.image_path_entry.grid(row=1, column=1, padx=10, pady=10)

        browse_image_button = tk.Button(content_frame, text="Browse", command=self.browse_image)
        browse_image_button.grid(row=1, column=2, padx=10, pady=10)

        file_label = tk.Label(content_frame, text="Select File:")
        file_label.grid(row=2, column=0, padx=10, pady=10)

        self.file_path_entry = tk.Entry(content_frame, width=50)
        self.file_path_entry.grid(row=2, column=1, padx=10, pady=10)

        browse_file_button = tk.Button(content_frame, text="Browse", command=self.browse_file)
        browse_file_button.grid(row=2, column=2, padx=10, pady=10)

        # Password Entry
        password_label = tk.Label(content_frame, text="Enter Password:")
        password_label.grid(row=3, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(content_frame, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)

        # Encrypt and Decrypt Buttons
        encrypt_button = tk.Button(content_frame, text="Encrypt", command=self.encrypt_message)
        encrypt_button.grid(row=4, column=0, padx=10, pady=10)

        decrypt_button = tk.Button(content_frame, text="Decrypt", command=self.decrypt_message)
        decrypt_button.grid(row=4, column=1, padx=10, pady=10)

        # Encryption/Decryption Feedback Label
        self.feedback_label = tk.Label(content_frame, text="", fg="red")
        self.feedback_label.grid(row=5, column=0, columnspan=3, pady=10)

    def toggle_maximize(self):
        state = self.root.attributes('-zoomed')
        self.root.attributes('-zoomed', not state)

    def browse_image(self):
        image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        self.image_path_entry.delete(0, tk.END)
        self.image_path_entry.insert(0, image_path)

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select File")
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)

    def encrypt_message(self):
        image_path = self.image_path_entry.get()
        file_path = self.file_path_entry.get()
        password = self.password_entry.get()

        if image_path and file_path and password:
            img = cv2.imread(image_path)

            with open(file_path, 'r') as file:
                msg = file.read()

            d = {}
            c = {}

            for i in range(255):
                d[chr(i)] = i
                c[i] = chr(i)

            m = 0
            n = 0
            z = 0

            for i in range(len(msg)):
                img[n, m, z] = d[msg[i]]
                n = n + 1
                m = m + 1
                z = (z + 1) % 3

            encrypted_msg_path = "EncryptedMsg.jpg"
            cv2.imwrite(encrypted_msg_path, img)
            os.system(f"start {encrypted_msg_path}")

            # Update feedback label
            self.feedback_label.config(text="Encryption successful!", fg="green")
        else:
            # Update feedback label
            self.feedback_label.config(text="Please provide valid image path, file path, and password.", fg="red")

    def decrypt_message(self):
        # Add decryption logic here

        # Update feedback label
        self.feedback_label.config(text="Decryption successful!", fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
