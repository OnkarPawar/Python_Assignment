#Q1 Write a program which accepts one charracter and checks whether it is vowel or consonant.
def Check_Vowel(ch):
    if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    else:
        return False

def main():
    Char = input("Enter the one character to check whether it is vowel or not: ")
    is_vowel = Check_Vowel(Char)
    if is_vowel:
        print(f"{Char} is vowel")
    else:
        print(f"{Char} is consonant")

if __name__ == "__main__":
    main()