codes = {'a':'`','b':'~','c':'!','d':'@','e':'#','f':'$','g':'%','h':'^','i':'**','j':'*','k':'(','l':')','m':'_','n':'-','o':'=','p':'+',
            'q':'|','r':';','s':',','t':'<','u':'.','v':'>','w':'?','x':'/','y':'1','z':'2','.':'3','E':'4','C':'5','E':'6','R':'7','O':'8',
            'I':'9','S':'0',':': 'xx', ' ': '!!'}

def main():
    infile = open('info_security.txt', 'r')
    filecontents = infile.read()
    infile.close

    outfile = open('encrypted_code.txt', 'w')

    for letter in filecontents:
        outfile.write(codes[letter])

    outfile.close

main()






