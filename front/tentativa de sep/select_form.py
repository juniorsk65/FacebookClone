import os

def select(title, options):
    os.system("clear")
    print("#"*50)
    print("\t" + title)
    print("#"*50, "\n\n")
    for i in  range(len(options)):
        print(i+1, ' - ', options[i])
    user_input = input('>> ')
    return user_input

def form(inputs):
    accumulator = dict(inputs)
    for i in inputs: 
        os.system("clear")
        print("#"*50)
        print("\tDigite os dados abaixo:")
        for j in inputs:
            print(j, ":", accumulator[j])
        print("#"*50, "\n\n")
        accumulator[i] = input(str(i) + " >> ")

    os.system("clear")
    print("#"*50)
    print("\tConfirma a entrada com os campos abaixo?")
    for j in inputs:
        print(j, ":", accumulator[j])
    print("#"*50, "\n\n")
    confirm = input("[s/n] >> ")
    if confirm == 's':
        return accumulator
    else:
        return 0