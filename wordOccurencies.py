#dependencies and libraries importation
import boto3
from pyspark import SparkContext
sc = SparkContext.getOrCreate()

#job initialization and declaration
rddf = sc.textFile("s3n://emrtestged/FAQ.pdf")#FAQ.pdf is te name of te file used
list = rddf.flatMap(lambda x:x.split(" ")).collect()#now we first of all split our list respecting space and also we transform our RDD job in a pyton list by means of collect()

dic = {}

#the following function can count the amount of words in the document and then displays it
def nbOfWords(list):
	s3 = boto3.resource("s3")
	s3.Object("wordcounterged-results", "results.txt").put(Body="Le nombre de mots est : " +str(len(list)))
	return print("Operation reussie")
#the following function can evaluate the amount of occurency for each word  and then displays it.
    
nbOfWords(list)

#countOccurencies(list)
#maxOccurencies(countOccurencies(list))
#minOccurencies(countOccurencies(list))

