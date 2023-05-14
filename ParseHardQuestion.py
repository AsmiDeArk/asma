class Question:
    number: str = 0
    text: str = ""
    answers: list[str] = []
    
    def __init__(self, number: str):
        self.answers = []
        self.number = number
    
    def print(self, file):
        if (len(self.answers) == 0):
            return
        
        file.write("::"+self.number+".::"+self.text+"\n")
        file.write("{\n")
        
        for i in self.answers:
            file.write("~"+i+"\n")
        
        file.write("}\n\n")
        

def read_next(text : str):
    splitText = text.split()
    result = Question(splitText[0])
    result.text = text[len(splitText[0]) + 1:].strip().capitalize()
    
    add = input()
    
    while add != "" and add != "exit":
        result.answers.append(" " + add[add.find(" "):].strip().capitalize())
        add = input()

    return result


file = open("result.txt", 'w')


if (__name__ == "__main__"):
    user = input("next:")
    
    while(user != 'exit'):
        if (user == ""):
            user = input("next:")
            continue
    
        value = read_next(user)
        value.print(file)
    
        user = input("next:")

    file.close()
