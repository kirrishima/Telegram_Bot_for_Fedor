import pyperclip

s = input("Введи свою строку с текстом и программа сама превратит его в код, а так же сразу скопирует результат в буфер обмена ")
with open('count.txt', 'r+') as file:
    count = int(file.readlines()[-1])
    count += 1
    with open('text_.txt', 'r+') as f:
        text_ = f.readlines()[-1]
        text_ += f", text_{count}"
        f.write('\n' + text_)
        print(text_ + ']')
    main = f"text_{count}" + " = {\n\t'amount_of_articles': "
    file.write('\n' + str(count))


s1 = s.split()
articles = "'articles': ["
n = 0
n += s.lower().count(' an ')
n += s.lower().count(' the ')
n += s.lower().count(' a ')


for i in range(len(s1)):
    if s1[i].lower() in ['an', 'a', 'the']:
        articles += "'" + s1[i] + "'" + ', '
        s1[i] = "___"
else:
    articles = articles[:-2] + "]"
text = " ".join(s1)
main += str(n) + ",\n\t" + "'text': " + f"'{text}',\n\t" + f"{articles}\n" + "}\n\n"

print('\n' + main)
pyperclip.copy(main)
