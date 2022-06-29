"""
Головоломка
(Время: 1 сек. Память: 16 Мб Сложность: 35%)
Головоломка
Петя разгадывает головоломку, которая устроена следующим образом. Дана квадратная таблица размера N×N,
 в каждой клетке которой записана какая-нибудь английская буква. Кроме того, дан список ключевых слов.
  Пете нужно, взяв очередное ключевое слово, найти его в таблице. То есть найти в таблице все буквы этого слова,
  причем они должны быть расположены так, чтобы клетка, в которой расположена каждая последующая буква слова,
  была соседней с клеткой, в которой записана предыдущая буква (клетки называются соседними, если они имеют
  общую сторону — то есть соседствуют по вертикали или по горизонтали). Например, на рисунке показано,
   как может быть расположено в таблице слово olympiad.

Когда Петя находит слово, он вычеркивает его из таблицы. Использовать уже вычеркнутые буквы в других ключевых словах
 нельзя. После того, как найдены и вычеркнуты все ключевые слова, в таблице остаются еще несколько букв, из которых
  Петя должен составить слово, зашифрованное в головоломке.

Помогите Пете в решении этой головоломки, написав программу, которая по данной таблице и списку ключевых слов выпишет,
 из каких букв Петя должен сложить слово, то есть какие буквы останутся в таблице после вычеркивания ключевых слов.

Входные данные
Во входном файле INPUT.TXT записаны два числа N (1 ≤ N ≤ 10) и M (0 ≤ M ≤ 100).
Следующие N строк по N заглавных английских букв описывают ребус. Следующие M строк содержат слова.
Слова состоят только из заглавных английских букв, каждое слово имеет длину от 1 до 100 символов.
Гарантируется, что в таблице можно найти и вычеркнуть по описанным выше правилам все ключевые слова.

Выходные данные
В выходной файл OUTPUT.TXT выведите в алфавитном порядке оставшиеся в таблице буквы.

Примеры
INPUT.TXT
5 3
POLTE
RWYMS
OAIPT
BDANR
LEMES
OLYMPIAD
PROBLEM
TEST
OUTPUT.TXT
AENRSW



INPUT.TXT
3 2
ISQ
ABC
IQW
I
IS

OUTPUT.TXT
ABCQQW
"""


def puzzleAnswer():
    fin = open("input.txt")
    fout = open("output.txt", "w")

    inputData = fin.readlines()
    linesCount, searchWordsCount = inputData[0].split(" ")

    searchChars = []
    for i in range(int(linesCount) + 1, len(inputData)):
        line = inputData[i].replace("\n", "")
        for j in range(0, len(line)):
            searchChars.append(line[j])

    chars = []
    for i in range(1, int(linesCount) + 1):

        line = inputData[i].replace("\n", "")
        for j in range(0, len(line)):
            if (line[j] not in searchChars):
                chars.append(line[j])
            else:
                searchChars.remove(line[j])

    key = sorted(chars)
    fout.write(''.join(key))



puzzleAnswer()

