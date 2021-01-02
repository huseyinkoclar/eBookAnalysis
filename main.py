import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from operator import itemgetter

stopWords = set(stopwords.words('english'))

punc = [',','.','?',':',';','-','!','(',')','/','>','<','=','#','+']

def choosen1(bookName1):
    file = open("deneme.txt", encoding="utf8")
    words = file.read()
    words = words.lower()
    file.close()
    return words

def choosen2(bookName1,bookName2):
    f = open("deneme.txt", "r")
    for x in f:
        print(x)

def cleanpunctuations(text):
    for i in range(len(text)):
        for j in range(len(punc)):
            if (i>=len(text)):
                break
            elif (text[i] == punc[j]): 
               text = text.replace(punc[j],'')
    return text.split()

def cleanstopwords(text):
    return [word for word in text if word not in stopWords]

def cleandigits(text):
    return [word for word in text if not word.isdigit()]

def countwords(text):
    freq_list = []
    words_list= []
    words2_list = []
    freq2_list = [] 
    freqtot_list = []
    for word in text:
            if word not in words_list:
                words_list.append(word)
                freq_list.append(text.count(word))
    sorted_list = sorted(zip(words_list, freq_list), key=itemgetter(1), reverse=True) 
    for i in range(len(sorted_list)):
            words_list[i] = sorted_list[i][0]
            freq_list[i] = sorted_list[i][1]
    return words_list,freq_list

def printlist(words_list,freq_list):
    for i in range(20):
        print(words_list[i] , freq_list[i])

def main():
    bookNumber = 0
    while bookNumber!=1 or bookNumber!=2:
        bookNumber = int(input("which you want book compare:  "))
        if bookNumber == 1:
            bookName1 = input("enter the book name:   ")
            words = choosen1(bookName1)
            words = cleanpunctuations(words)
            words = cleanstopwords(words)
            words = cleandigits(words)
            words_list,freq_list = countwords(words)
            printlist(words_list,freq_list)
            #print(words)
            break
        elif bookNumber == 2:
            bookName1 = input("enter the first book name")
            bookName2 = input("enter the second book name")
            choosen2(bookName1,bookName2)
            break
        else:
            print("try again")
main()