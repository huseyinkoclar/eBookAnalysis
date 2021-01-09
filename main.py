import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from operator import itemgetter
from bs4 import BeautifulSoup
import urllib
import requests

bookNumber = 0

stopWords = set(stopwords.words('english'))

punc = [',','.','?',':',';','-','!','(',')','/','>','<','=','#','+','"','[',']',"'",'*','_','-']

#DELETING PUNCTIATIONS IN TEXT
def cleanpunctuations(text):
    for i in range(len(text)):
        for j in range(len(punc)):
            if (i>=len(text)):
                break
            elif (text[i] == punc[j]): 
               text = text.replace(punc[j],'')
    return text.split()

#DELETING STOP WORDS IN TEXT
def cleanstopwords(text):
    return [word for word in text if word not in stopWords]

#DELETING DIGITS IN THE TEXT
def cleandigits(text):
    return [word for word in text if not word.isdigit()]

#COUNTING OF WORDS
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

#TOTAL AND RANKING OF FREQUENCIES IN 2 BOOK OPTIONS
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
        print(i+1 , sumwords[i], "      " ,exfreq1 ,"     ", exfreq2, "     " , sumfreq[i])

#CREATING DISTINCT WORD TABLES WITH 2 BOOK OPTIONS
def distincWords(word_list,freq_list,word1_list,freq1_list):
    print("Book1:")
    counter = 0
    for i in range(len(word_list)):
        flag = 0
        for j in range(len(word1_list)):
            if(word_list[i]==word1_list[j]):
                flag = 1
                break
        if(flag == 0):
            counter += 1
            print(counter , word_list[i],"    ",freq_list[i])
        if counter == 20:
            break
    print("Book2:")
    counter = 0
    for i in range(len(word1_list)):
        flag = 0
        for j in range(len(word_list)):
            if(word1_list[i]==word_list[j]):
                flag = 1
                break
        if(flag == 0):
            counter += 1
            print(counter , word1_list[i],"    ",freq1_list[i])
        if counter == 20:
            break
        
#PRINT HIGHEST 20 FREQUENCY WORDS
def printlist1(words_list,freq_list):
    for i in range(20):
        print(words_list[i] , freq_list[i])

#WEB SCRAPING BY USER RECEIVED BOOK NAME
def webScraping(bookName,bookName2):
    #BOOK 1: Non-Programmer's Tutorial for Python 2.6
    website = "https://en.wikibooks.org/wiki/" + bookName + "/Print_version"
    website1 = "https://en.wikibooks.org/wiki/" + bookName2 + "/Print_version"
    if(bookName2==""):
        r = requests.get(website)
        if(r.status_code != 200):
            print("bulamadim")
        else:
            book = ""
            soup = BeautifulSoup(r.content,'html.parser')
            paragraphs = soup.find('div', {"class":"mw-parser-output"} ).find_all('p')
            for paragraph in paragraphs:
                book += " " + str(paragraph.text)
            paragraphs = soup.find('div', {"class":"mw-content-ltr"} ).find_all('span')
            for paragraph in paragraphs:
                book += " " + str(paragraph.text)
            print(book.lower())
            return book.lower()
    else:
        r1 = requests.get(website1)
        r = requests.get(website)
        if(r.status_code != 200 or r1.status_code != 200):
            print("bulamadim")
        else:
            book = ""
            book1 = ""
            soup = BeautifulSoup(r.content,'html.parser')
            soup1 = BeautifulSoup(r1.content,'html.parser')
            paragraphs = soup.find('div', {"class":"mw-parser-output"} ).find_all('p')
            for paragraph in paragraphs:
                book += " " + str(paragraph.text)
            paragraphs = soup.find('div', {"class":"mw-content-ltr"} ).find_all('span')
            for paragraph in paragraphs:
                book += " " + str(paragraph.text)
            paragraphs1 = soup1.find('div', {"class":"mw-parser-output"} ).find_all('p')
            for paragraph in paragraphs1:
                book1 += " " + str(paragraph.text)
            paragraphs1 = soup1.find('div', {"class":"mw-content-ltr"} ).find_all('span')
            for paragraph in paragraphs1:
                book1 += " " + str(paragraph.text)

            
            return book.lower(),book1.lower()

#TAKING BOOK NUMBER AND BOOK NAME FROM USER
def main():
    bookNumber=0
    while bookNumber!=1 or bookNumber!=2:
        bookNumber = int(input("which you want book compare:  "))
        if bookNumber == 1:
            bookName1 = input("enter the book name:   ")
            words = webScraping(bookName1,"")
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
            words,words1 = webScraping(bookName1,bookName2)
            words = cleanpunctuations(words)
            words = cleanstopwords(words)
            words = cleandigits(words)
            words1 = cleanpunctuations(words1)
            words1 = cleanstopwords(words1)
            words1 = cleandigits(words1)
            words_list,freq_list=countwords(words)
            words1_list,freq1_list=countwords(words1)
            sumOfFreq(words_list,freq_list,words1_list,freq1_list)
            distincWords(words_list,freq_list,words1_list,freq1_list)
            break
        else:
            print("try again")

main()