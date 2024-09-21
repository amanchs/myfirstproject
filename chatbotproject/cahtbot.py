import time
now = time.ctime()
qna = {
    "hi" :"hello",
    "how are you?" : "I am fine.",
    "what is your name" : "I am Chatbot of I-tech.",
    "how old are you?" : "I am 3days old",
    "what is the shape of the Earth" : "The Earth is approximately a sphere.",
    "what is the capital of India" : "New Delhi",
    "what is the capital of USA?" : "Washinton D.C.",
    "wealthiest counntry in the world" : "Luxembourg is the world's wealthiest country, with a GDP per capita of $143,742 thousand, according to the IMF.",
    "what is the time right now?" : now,
}

while True:
    qs = input()
    if (qs == "quit"):
        break
    else:
        print(qna[qs])
