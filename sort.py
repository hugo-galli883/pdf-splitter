import os

os.system("ls pages/ > pages.txt")
with open('pages.txt','a') as file :
	file.write("&")

def gen_liste(fichier) :
    with open(fichier,'r+') as file :
        content = file.read()
        i = 0
        words = []
        word = []
        while(content[i] != "&") :
            if(content[i] == "\n") :
                words.append("".join(word))
                word = []
            else :
                word.append(content[i])
            i += 1
        return words

def get_n(w,ind):
    num = []
    rec = 0
    for l in w:
        if(l == "-" or l == "_" or l == ".") :
            rec += 1
        if(rec == ind) :
            num.append(l)
    return(int("".join(num[1:])))

def gamma(noms):
    noms2 = []
    for i in range(len(noms)//4):
        a = noms[4*i]
        b = noms[4*i+1]
        c = noms[4*i+2]
        d = noms[4*i+3]
        noms2.append(d)
        noms2.append(a)
        noms2.append(b)
        noms2.append(c)
    return noms2

def main() :
    pages = gen_liste('pages.txt')
    noms = []
    for i in range(len(pages)):
        x,y = get_n(pages[i][2:],1),int(pages[i][:1])
        print(pages[i])
        noms.append("{}".format("0000000"[:-len(str(2*(x-1)+y))]+str(2*(x-1)+y)))
        os.system("mv pages/{} pages/{}.png".format(pages[i],noms[-1]))
    noms.sort()
    print("Noms :")
    for i in noms:
        print("\t"+i)
    noms2 = gamma(noms)
    for i in range(len(noms)):
        os.system("mv pages/{}.png pages/p{}.png".format(noms[i],noms2[i]))
    os.system('rm pages.txt')


main()
