import pyttsx3

eng = pyttsx3.init()

v1 = eng.getProperty('voices')[0].id
v2 = eng.getProperty('voices')[1].id

eng.setProperty("voice", v1)
eng.setProperty("rate", 120)

eng.say("Hello I'm jack. What is your name?")
eng.runAndWait()

name = input("Your name: ")

eng.say("Hi {}...You can chat with me or with my friend Jane".format(name))
eng.runAndWait()

eng.setProperty("voice", v2)
eng.say("Hi {}.".format(name))
eng.runAndWait()

eng.setProperty("voice", v1)
eng.say("You can select jane or me.".format(name))
eng.runAndWait()

agent = input("Select Jack or Jane (jack/jane):")

if agent.lower() == "jane":
    eng.setProperty("voice", v2)

eng.say("Hi {}...So what do you want to know about our company?".format(name))
eng.runAndWait()

ques = input()


def chat_check():
    global flag, ques
    while True:
        print("--------------------------------------------------------------------------------")
        eng.say("Do your want to know anything else?")
        eng.runAndWait()

        check = input("Continue (yes/no): ")
        if check.lower() == "yes":
            eng.say("Okay. What do your want to know ?")
            eng.runAndWait()

            ques = input()
            break
        elif check.lower() == "no":
            eng.say("Nice to chat with you. Have a nice day.")
            eng.runAndWait()

            flag = False
            break
        else:
            eng.say("Your input is invalid. Please check it.")
            eng.runAndWait()


flag = True

while flag:

    if all(i in ques.lower() for i in ["company", "name"]):
        eng.say("Our company is ABC private Limited.")
        eng.runAndWait()
        chat_check()

    elif all(i in ques.lower() for i in ["ceo", "name"]):
        eng.say("Our CEO if Mr. James Parker")
        eng.runAndWait()
        chat_check()

    elif any(i in ques.lower() for i in ["contact", "address", "telephone", "email", "mobile", "location"]):
        eng.say(
            "Our company address is 125 Srimath Anagarika Dharmapala Mawatha, Colombo 7. You can contact us via emails and via our hotline. Our email address is abc@gmail.com and the hotline is 0112111111.")
        eng.runAndWait()
        chat_check()

    elif any(i in ques.lower() for i in ["service", "product", "manufacture"]):
        eng.say("Our company is developing Artificial Intelligence based enterprise software products.")
        eng.runAndWait()
        chat_check()

    else:
        eng.say("Your question is not clear {}.".format(name))
        eng.runAndWait()
        chat_check()