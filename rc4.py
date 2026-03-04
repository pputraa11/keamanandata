# =====================================================================
# TUGAS KRIPTOGRAFI: Implementasi RC4 Interaktif (From Scratch)
# =====================================================================

def ksa(key):
    """Key-Scheduling Algorithm (KSA) untuk mengacak array State S."""
    key_length = len(key)
    S = list(range(256)) 
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i] 
    return S

def prga(S, text_length):
    """Pseudo-Random Generation Algorithm (PRGA) untuk membuat keystream."""
    i = j = 0
    keystream = []
    for _ in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i] 
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return keystream

def rc4_process(text_bytes, key_string):
    """Fungsi inti untuk Enkripsi/Dekripsi RC4."""
    key_bytes = [ord(c) for c in key_string]
    S = ksa(key_bytes)
    keystream = prga(S, len(text_bytes))
    
    result = []
    for i in range(len(text_bytes)):
        # Operasi XOR antara byte data dan byte keystream
        result.append(text_bytes[i] ^ keystream[i])
        
    return result, keystream

# =====================================================================
# MAIN PROGRAM (Input Terminal)
# =====================================================================
if __name__ == "__main__":
    print("="*45)
    print("   PROGRAM ENKRIPSI & DEKRIPSI RC4   ")
    print("="*45)

    # 1. Input dari Pengguna
    plaintext = input("Masukkan Teks (Plaintext) : ")
    key = input("Masukkan Kunci (Key)       : ")

    if not plaintext or not key:
        print("\n[!] Error: Teks dan Kunci tidak boleh kosong!")
    else:
        # Konversi plaintext ke bytes (ASCII)
        pt_bytes = [ord(c) for c in plaintext]

        # --- PROSES ENKRIPSI ---
        print("\n" + "-"*20)
        print("PROSES ENKRIPSI")
        print("-"*20)
        
        ciphertext_bytes, k_enc = rc4_process(pt_bytes, key)
        ciphertext_hex = "".join([f"{b:02X}" for b in ciphertext_bytes])
        
        print(f"Step 1: Plaintext diubah ke ASCII Bytes: {pt_bytes}")
        print(f"Step 2: Keystream yang dihasilkan      : {k_enc}")
        print(f"Step 3: Hasil XOR (Ciphertext Hex)     : {ciphertext_hex}")

        # --- PROSES DEKRIPSI ---
        print("\n" + "-"*20)
        print("PROSES DEKRIPSI")
        print("-"*20)
        
        # Masukkan hasil enkripsi tadi (ciphertext_bytes) ke fungsi yang sama
        decrypted_bytes, k_dec = rc4_process(ciphertext_bytes, key)
        decrypted_text = "".join([chr(b) for b in decrypted_bytes])
        
        print(f"Step 1: Ciphertext Bytes yang diterima : {ciphertext_bytes}")
        print(f"Step 2: Keystream yang sama digunakan  : {k_dec}")
        print(f"Step 3: Hasil Dekripsi (Teks Asli)     : {decrypted_text}")

        # --- VALIDASI AKHIR ---
        print("\n" + "="*45)
        if plaintext == decrypted_text:
            print("STATUS: ✅ Berhasil mengembalikan data asli.")
        else:
            print("STATUS: ❌ Gagal mengembalikan data.")
        print("="*45)