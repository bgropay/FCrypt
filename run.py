import os
import base64

while True:
    print("\n===== MENU =====")
    print("1. Enkripsi file")
    print("2. Dekripsi file")
    print("3. Keluar")
    print("================")
    
    choice = input("Pilih opsi (1/2/3): ")
    
    if choice == "1":
        directory = input("[»] Masukkan jalur ke folder yang ingin dienkripsi: ")
        
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            
            # Membaca file asli
            with open(filepath, "rb") as file:
                file_data = file.read()
            
            # Mengenkripsi data file dan nama file
            encrypted_data = base64.b64encode(file_data)
            encrypted_filename = base64.b64encode(filename.encode()).decode()
            
            # Menulis data terenkripsi ke file baru dengan nama terenkripsi
            with open(os.path.join(directory, encrypted_filename), "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
            
            # Menghapus file asli
            os.remove(filepath)
            
            # Menampilkan pesan status
            print(f"[*] Mengenkripsi {filename}...")
            print(f"[+] File {filename} berhasil dienkripsi menjadi {encrypted_filename}")
    
    elif choice == "2":
        directory = input("Masukkan path direktori: ")
        
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            
            try:
                # Mendekripsi nama file
                decrypted_filename = base64.b64decode(filename).decode()
                
                # Membaca file terenkripsi
                with open(filepath, "rb") as file:
                    encrypted_data = file.read()
                
                # Mendekripsi data file
                decrypted_data = base64.b64decode(encrypted_data)
                
                # Menulis data dekripsi ke file baru dengan nama dekripsi
                with open(os.path.join(directory, decrypted_filename), "wb") as decrypted_file:
                    decrypted_file.write(decrypted_data)
                
                # Menghapus file terenkripsi
                os.remove(filepath)
                
                # Menampilkan pesan status
                print(f"Mendekripsi {filename}...")
                print(f"File {filename} berhasil didekripsi menjadi {decrypted_filename}")
                
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
    
    elif choice == "3":
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
