import random

def randomGen(len):
    specVal = int(0.2 * len)
    numVal = int(0.4 * len)
    textVal = len - numVal - specVal
    passGen = []
    for i in range(numVal):
        ASCIIval = random.randint(48, 57)
        passGen.append(chr(ASCIIval))
    for i in range(textVal):
        ASCIIval = random.choice([random.randint(97, 122),random.randint(65,90)])
        passGen.append(chr(ASCIIval))
    for i in range(specVal):
        ASCIIval = random.choice([random.randint(33, 47), random.randint(58, 64),random.randint(91, 96) , random.randint(123, 126)])
        passGen.append(chr(ASCIIval))
    random.shuffle(passGen)
    passGenFinal = ""
    for charc in passGen:
        passGenFinal += charc
    return passGenFinal


