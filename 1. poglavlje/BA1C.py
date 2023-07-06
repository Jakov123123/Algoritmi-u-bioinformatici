text = input()

def Reverse(text):
    Ctext = ""
    for i in range(len(text)):
        if text[i] == "A":
            Ctext += "T"
        elif text[i] == "T":
            Ctext += "A"
        elif text[i] == "C":
            Ctext += "G"
        elif text[i] == "G":
            Ctext += "C"
    RCtext = ""
    for i in range(len(text)-1,-1,-1):
        RCtext += Ctext[i]
    print(RCtext)

Reverse(text)
