def res_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            if not words:
                return "Fayl bo'sh"
            longest_word = max(words, key=len)
            return longest_word
    except FileNotFoundError:
        return "Fayl topilmadi"
    except Exception as e:
        return str(e)


file = 'file.txt'
longest_word = res_file(file)
print(f"Filedagi eng uzun so'z: {longest_word}")
