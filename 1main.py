def count_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            text = file.read()
            return len(text)
    except FileNotFoundError:
        return "Xatolik"
    except Exception as e:
        return str(e)


file = 'file.txt'
word_count = count_file(file)
print(f"Filedagi so'zlar soni: {word_count}")
