def abc():
    def createMessage(name):
        msg = 'Hello '+ name
        return msg

    name = input("enter your name: ")
    msg = createMessage(name)
    print(msg)
    
if __name__ == '__main__':
    abc()