def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift if mode == 'encrypt' else ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def brute_force(text):
    print("\nBrute-force natijalari:")
    for shift in range(1, 26):
        print(f"Shift {shift}: {caesar_cipher(text, shift, 'decrypt')}")

# Foydalanish misoli
text = "salom"
shift = 3

# Shifrlash
encrypted = caesar_cipher(text, shift, 'encrypt')
print(f"Shifrlangan: {encrypted}")  # "vdorp"

# Dekodlash
decrypted = caesar_cipher(encrypted, shift, 'decrypt')
print(f"Dekodlangan: {decrypted}")  # "salom"

# Bruteforce (kalitni topish)
brute_force("vdorp")  # Shift 3: "salom" ko'rinadi
Qanday ishlatish?
Matnni shifrlash:

python
Copy
caesar_cipher("salom", 3, 'encrypt')  # "vdorp"
Shifrni ochish:

python
Copy
caesar_cipher("vdorp", 3, 'decrypt')  # "salom"
Kalitni bilmasangiz (Brute-force):

python
Copy
brute_force("vdorp")  # Barcha shiftlarni tekshiradi
Misol:
Kiritish (text = "Python 3.10", shift = 5):

Shifrlangan: "Udymts 3.10" (faqat harflar siljidi)

Dekodlangan: "Python 3.10"

Agar kodga o‘zgartirishlar kiritmoqchi bo‘lsangiz yoki tushunmovchilik bo‘lsa, ayting! 😊

masalan qandaudir raqalar orqali bosibozim tanlay
Agar siz raqamlar orqali kalitni tanlash (shift miqdorini kiritish) va matnni shifrlash/ochish imkoniyatini qo'shmoqchi bo'lsangiz, quyidagi kodda bu funktsiyalarni birlashtirib beraman.

📜 To'liq Kod: Sezar Shifri + Raqamli Kalit Tanlash
python
Copy
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift if mode == 'encrypt' else ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    print("🔐 Sezar Shifrlash Dasturi 🔓")
    print("1. Shifrlash (Encrypt)")
    print("2. Dekodlash (Decrypt)")
    print("3. Bruteforce (Hamma kalitlarni tekshirish)")
    
    choice = input("Tanlovni kiriting (1/2/3): ")
    text = input("Matnni kiriting: ")
    
    if choice in ['1', '2']:
        try:
            shift = int(input("Kalit (shift soni, 1-25): "))
            if shift < 1 or shift > 25:
                raise ValueError
        except ValueError:
            print("⚠ Xato! Kalit 1 dan 25 gacha bo'lgan butun son bo'lishi kerak.")
            return
        
        if choice == '1':
            encrypted = caesar_cipher(text, shift, 'encrypt')
            print(f"🔒 Shifrlangan matn: {encrypted}")
        else:
            decrypted = caesar_cipher(text, shift, 'decrypt')
            print(f"🔓 Dekodlangan matn: {decrypted}")
    
    elif choice == '3':
        print("\n🔎 Bruteforce natijalari:")
        for shift in range(1, 26):
            print(f"Shift {shift}: {caesar_cipher(text, shift, 'decrypt')}")
    
    else:
        print("⚠ Noto'g'ri tanlov! 1, 2 yoki 3 ni tanlang.")

if __name__ == "__main__":
    main()