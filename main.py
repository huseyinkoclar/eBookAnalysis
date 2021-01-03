import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from operator import itemgetter

bookNumber = 0

stopWords = set(stopwords.words('english'))

punc = [',','.','?',':',';','-','!','(',')','/','>','<','=','#','+']

def choosen1(bookName1):
    file = open(bookName1, encoding="utf8")
    words = file.read()
    words = words.lower()
    file.close()
    return words

def choosen2(bookName1,bookName2):
    file = open(bookName1, encoding="utf8")
    words = file.read()
    words = words.lower()
    file.close()
    file = open(bookName2,encoding="utf8")
    words1 = file.read()
    words1 = words1.lower()
    file.close()
    return words, words1

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
    for word in text:
            if word not in words_list:
                words_list.append(word)
                freq_list.append(text.count(word))
    sorted_list = sorted(zip(words_list, freq_list), key=itemgetter(1), reverse=True) 
    for i in range(len(sorted_list)):
            words_list[i] = sorted_list[i][0]
            freq_list[i] = sorted_list[i][1]
    return words_list,freq_list

def sumOfFreq(word_list,freq_list,word1_list,freq1_list):
    sumwords = []
    sumfreq = []
    exfreq1 = 0
    exfreq2 = 0
    for i in range(len(word_list)):
        sumwords.append(word_list[i])
        for j in range(len(word1_list)):
            if(word1_list[j] == word_list[i]):
                sumfreq.append(freq1_list[j]+freq_list[i])
    sorted_list = sorted(zip(sumwords, sumfreq), key=itemgetter(1), reverse=True) 
    for i in range(len(sorted_list)):
            sumwords[i] = sorted_list[i][0]
            sumfreq[i] = sorted_list[i][1]
    print("NO   WORD   FREQ_1   FREQ_2   FREQ_SUM")
    for i in range(20):
        for j in range(len(word_list)):
            if (word_list[j] == sumwords[i]):
                exfreq1 = freq_list[j]
                break
        for k in range(len(word1_list)):
            if(word1_list[k] == sumwords[i]):
                exfreq2 = freq1_list[k]
                break
        print(i , sumwords[i], "      " ,exfreq1 ,"     ", exfreq2, "     " , sumfreq[i])





def printlist1(words_list,freq_list):
    for i in range(20):
        print(words_list[i] , freq_list[i])



def main():
    bookNumber=0
    while bookNumber!=1 or bookNumber!=2:
        bookNumber = int(input("which you want book compare:  "))
        if bookNumber == 1:
            bookName1 = input("enter the book name:   ")
            words = choosen1(bookName1)
            words = cleanpunctuations(words)
            words = cleanstopwords(words)
            words = cleandigits(words)
            words_list,freq_list = countwords(words)
            printlist1(words_list,freq_list)
            #print(words)
            break
        elif bookNumber == 2:
            bookName1 = input("enter the first book name:   ")
            bookName2 = input("enter the second book name:   ")
            words,words1 = choosen2(bookName1,bookName2)
            words = cleanpunctuations(words)
            words = cleanstopwords(words)
            words = cleandigits(words)
            words1 = cleanpunctuations(words1)
            words1 = cleanstopwords(words1)
            words1 = cleandigits(words1)
            words_list,freq_list=countwords(words)
            words1_list,freq1_list=countwords(words1)
            sumOfFreq(words_list,freq_list,words1_list,freq1_list)
            break
        else:
            print("try again")
main()