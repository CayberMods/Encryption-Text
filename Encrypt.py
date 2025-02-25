def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

choice = input("モードを選択してください (1 = 暗号化, 2 = 復号化): ")
text = input("テキストを入力してください: ")
shift = int(input("シフト値を入力してください: "))

if choice == "1":
    print(f"暗号化されたテキスト: {encrypt(text, shift)}")
elif choice == "2":
    print(f"復号化されたテキスト: {decrypt(text, shift)}")
else:
    print("無効な選択です！")
