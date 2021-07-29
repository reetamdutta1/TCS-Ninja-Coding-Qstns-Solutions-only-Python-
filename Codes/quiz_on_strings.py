#quiz_on_strings
#Consider the following list of pan card numbers:
#What is the output of the below two print statements?

pancard_list=["AABGT6715H", "UFFAC4352T", "IFSBD9163K", "JOOEC1225H","RWXAFE187B"] 

print(pancard_list[3][6], end=" ")

print(pancard_list[4][3:])

#What is the output of the code given below?

message="welcome to Mysore"
word=message[-7:]
if(word=="mysore"):
    print("got it")
else:
    message=message[3:14]
    print(message)

#What is the output of the below code?

song="JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
song_words=song.split()
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)