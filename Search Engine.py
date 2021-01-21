# Author = Kartik Kulshreshtha
# Purpose = Practicing Python Programs
# Date = 21/01/2021

def MatchingWords(Sentence1,Sentence2):
    Words1 = Sentence1.split(' ')
    Words2 = Sentence2.split(' ')
    score = 0
    for Word1 in Words1:
        for Word2 in Words2:
            if Word1.lower() == Word2.lower():
                score = score+1
    return score

if __name__ == '__main__':
    Query = input("Enter your query string\n")
    Sentences = ["Python is good","I Love Python",'My name is kartik','This is snake']

    #Get the number of score of each loop
    Scorces = [MatchingWords(Query,Sentence) for Sentence in Sentences]

    #Here we sort the scores with sentence in decreasing order
    SortSentScore = [sentscore for sentscore in sorted(zip(Scorces,Sentences),reverse=True) if sentscore[0] !=0]
    print(SortSentScore)

    #Here We print the number of scores found
    print(f"{len(SortSentScore)} results found")

    for scorce,item in SortSentScore:
        print(f'\"{item}\" with score of {scorce}')
