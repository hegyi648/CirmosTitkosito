#!/usr/bin/python3
#coding: utf-8
"""
A programot készítette: Hegyi István
Titkosító program ciromos titkosítási nyelvhez.
2021.12.19
"""

masolasVagolapra = True 

from termcolor import cprint, colored
import pyperclip


hashes = ['vfg32t5zhz', 'vr0pwm27fz', 'ecwo2kvtbz', 'ejlt46xq0x', 'v77te7fcj2', '8d4pzgqryl', 'yqpdueugq8',
          'ap25fe693s', 'lkmonueb6r', 'lwjfc2okwg', 'bdex2k7qcs', '9jg2iguazm', '7nh73ofirm', '0pognn2fdg',
          '5f2ycqodny', '3ubglj4cpd', '6gypfqmq85', '1bahqhtevy', 'zlxu9novj5', 'b0x54w2e8u', '06reqgir2l',
          'kyfnusgvke', 'eam03q1yzd', 'oo3lwb9mku', 'zwohw10ggu', 'ffn1k8f2ck', 'x4x20jme3k', 'bdj2rcfamw',
          '8vm79snvjo', 'vlf700vzj0', 'ny33u857ig', 'sz5jkzf7eb', 'pa6jx6e8j6', 'e1ikbtfsow', 'gfzx4spco0',
          '6fuqdffiym', 'p95par29pm', 'k57trv6rfi', 'pr3mjjlj58', 'vt9eueaq3q', 'fwmrztvyhn', 'bnqpnvkuzy',
          'o04s7swzwr', 'nd83q3pqdn', 'njg3aryog6', 'wgwgs8gk5x', 'cte4rngd00', 'noh60bgc81', 'r8xy20hzfr',
          'pq2jaqddu1', 'dtsk5lk28l', 'kpgnw11095', 'jvl4e5n8fm', 'l1plut31qk', 's6liiwrd6w', 'pt1wcsdf53',
          '8j4fbdgnw0', '0uktr12age', 'amemk9z73t', 'lmew09uxoj', '7x3ur2arfd', '634vv428rs', 'zom0o9kylb',
          'hhz1rpz2x5', 'yflbhumq4t', 'rxtr0rdtd8', 'mwdsq82jom', '7ocbt0b6it', 'v52yq5b37l', 'k88d5lknfg',
          'e80e7ou5i5', '81rzsvevx4', 'adb0ub6sww', '2a7vrfneg5', 'fvoiiwc455', '7b9wci6r2v', 'zrp22z4f3q',
          'ij3u9wfw1z', 'ri0jcr5vgi', 'm2fowbkh37', 'cw6oidxt24', 'enxt7pgw8l', 'oevugt9ha8', 'khagvx5t0u',
          'hm1q0xy4mb', 'y2u177mct8', 'mqng0demqr', 'icapwv6eh7', '8s9iea2mdt', 'au4799lvfv', 'kdeb3uo2fz',
          'mkrqbmulsw', '5hkw4wrw4y', 'ije0dl87t8', '5ojlxca2wv', 'pig1yk8lk1', '7fee9chzsv', 'c6r7ws5pqv',
          'm1tnh17otl', 'qsuozaeilc']


def drawMainMenu():
    print("\033c", end="")
    print()
    cprint("----------------Cirmos Titkosító----------------", "yellow")
    cprint("1 - Titkosítás", "green")
    cprint("2 - Dekódolás", "green")
    cprint("3 - Kilépés", "red")


def encryptFunction():
    print("\033c", end="")
    print()
    cprint("-------------------Titkosítás-------------------", "yellow")
    cprint("Titkosítandó szöveg:", "cyan")
    text=input()
    encryptedText=""
    # region Titkosítás
    for i in range(len(text)):
        if text[i] == "a":
            encryptedText = encryptedText + hashes[0]
        elif text[i] == "b":
            encryptedText = encryptedText + hashes[1]
        elif text[i] == "c":
            encryptedText = encryptedText + hashes[2]
        elif text[i] == "d":
            encryptedText = encryptedText + hashes[3]
        elif text[i] == "e":
            encryptedText = encryptedText + hashes[4]
        elif text[i] == "f":
            encryptedText = encryptedText + hashes[5]
        elif text[i] == "g":
            encryptedText = encryptedText + hashes[6]
        elif text[i] == "h":
            encryptedText = encryptedText + hashes[7]
        elif text[i] == "i":
            encryptedText = encryptedText + hashes[8]
        elif text[i] == "j":
            encryptedText = encryptedText + hashes[9]
        elif text[i] == "k":
            encryptedText = encryptedText + hashes[10]
        elif text[i] == "l":
            encryptedText = encryptedText + hashes[11]
        elif text[i] == "m":
            encryptedText = encryptedText + hashes[12]
        elif text[i] == "n":
            encryptedText = encryptedText + hashes[13]
        elif text[i] == "o":
            encryptedText = encryptedText + hashes[14]
        elif text[i] == "p":
            encryptedText = encryptedText + hashes[15]
        elif text[i] == "q":
            encryptedText = encryptedText + hashes[16]
        elif text[i] == "r":
            encryptedText = encryptedText + hashes[17]
        elif text[i] == "s":
            encryptedText = encryptedText + hashes[18]
        elif text[i] == "t":
            encryptedText = encryptedText + hashes[19]
        elif text[i] == "u":
            encryptedText = encryptedText + hashes[20]
        elif text[i] == "v":
            encryptedText = encryptedText + hashes[21]
        elif text[i] == "w":
            encryptedText = encryptedText + hashes[22]
        elif text[i] == "x":
            encryptedText = encryptedText + hashes[23]
        elif text[i] == "y":
            encryptedText = encryptedText + hashes[24]
        elif text[i] == "z":
            encryptedText = encryptedText + hashes[25]
        elif text[i] == "A":
            encryptedText = encryptedText + hashes[26]
        elif text[i] == "B":
            encryptedText = encryptedText + hashes[27]
        elif text[i] == "C":
            encryptedText = encryptedText + hashes[28]
        elif text[i] == "D":
            encryptedText = encryptedText + hashes[29]
        elif text[i] == "E":
            encryptedText = encryptedText + hashes[30]
        elif text[i] == "F":
            encryptedText = encryptedText + hashes[31]
        elif text[i] == "G":
            encryptedText = encryptedText + hashes[32]
        elif text[i] == "H":
            encryptedText = encryptedText + hashes[33]
        elif text[i] == "I":
            encryptedText = encryptedText + hashes[34]
        elif text[i] == "J":
            encryptedText = encryptedText + hashes[35]
        elif text[i] == "K":
            encryptedText = encryptedText + hashes[36]
        elif text[i] == "L":
            encryptedText = encryptedText + hashes[37]
        elif text[i] == "M":
            encryptedText = encryptedText + hashes[38]
        elif text[i] == "N":
            encryptedText = encryptedText + hashes[39]
        elif text[i] == "O":
            encryptedText = encryptedText + hashes[40]
        elif text[i] == "P":
            encryptedText = encryptedText + hashes[41]
        elif text[i] == "Q":
            encryptedText = encryptedText + hashes[42]
        elif text[i] == "R":
            encryptedText = encryptedText + hashes[43]
        elif text[i] == "S":
            encryptedText = encryptedText + hashes[44]
        elif text[i] == "T":
            encryptedText = encryptedText + hashes[45]
        elif text[i] == "U":
            encryptedText = encryptedText + hashes[46]
        elif text[i] == "V":
            encryptedText = encryptedText + hashes[47]
        elif text[i] == "W":
            encryptedText = encryptedText + hashes[48]
        elif text[i] == "X":
            encryptedText = encryptedText + hashes[49]
        elif text[i] == "Y":
            encryptedText = encryptedText + hashes[50]
        elif text[i] == "Z":
            encryptedText = encryptedText + hashes[51]
        elif text[i] == "0":
            encryptedText = encryptedText + hashes[52]
        elif text[i] == "1":
            encryptedText = encryptedText + hashes[53]
        elif text[i] == "2":
            encryptedText = encryptedText + hashes[54]
        elif text[i] == "3":
            encryptedText = encryptedText + hashes[55]
        elif text[i] == "4":
            encryptedText = encryptedText + hashes[56]
        elif text[i] == "5":
            encryptedText = encryptedText + hashes[57]
        elif text[i] == "6":
            encryptedText = encryptedText + hashes[58]
        elif text[i] == "7":
            encryptedText = encryptedText + hashes[59]
        elif text[i] == "8":
            encryptedText = encryptedText + hashes[60]
        elif text[i] == "9":
            encryptedText = encryptedText + hashes[61]
        elif text[i] == "!":
            encryptedText = encryptedText + hashes[62]
        elif text[i] == "#":
            encryptedText = encryptedText + hashes[63]
        elif text[i] == "$":
            encryptedText = encryptedText + hashes[64]
        elif text[i] == "%":
            encryptedText = encryptedText + hashes[65]
        elif text[i] == "&":
            encryptedText = encryptedText + hashes[66]
        elif text[i] == "'":
            encryptedText = encryptedText + hashes[67]
        elif text[i] == "(":
            encryptedText = encryptedText + hashes[68]
        elif text[i] == ")":
            encryptedText = encryptedText + hashes[69]
        elif text[i] == "*":
            encryptedText = encryptedText + hashes[70]
        elif text[i] == "+":
            encryptedText = encryptedText + hashes[71]
        elif text[i] == ",":
            encryptedText = encryptedText + hashes[72]
        elif text[i] == "-":
            encryptedText = encryptedText + hashes[73]
        elif text[i] == ".":
            encryptedText = encryptedText + hashes[74]
        elif text[i] == "/":
            encryptedText = encryptedText + hashes[75]
        elif text[i] == ":":
            encryptedText = encryptedText + hashes[76]
        elif text[i] == ";":
            encryptedText = encryptedText + hashes[77]
        elif text[i] == "<":
            encryptedText = encryptedText + hashes[78]
        elif text[i] == "=":
            encryptedText = encryptedText + hashes[79]
        elif text[i] == ">":
            encryptedText = encryptedText + hashes[80]
        elif text[i] == "?":
            encryptedText = encryptedText + hashes[81]
        elif text[i] == "@":
            encryptedText = encryptedText + hashes[82]
        elif text[i] == "[":
            encryptedText = encryptedText + hashes[83]
        elif text[i] == "]":
            encryptedText = encryptedText + hashes[84]
        elif text[i] == "^":
            encryptedText = encryptedText + hashes[85]
        elif text[i] == "_":
            encryptedText = encryptedText + hashes[86]
        elif text[i] == "`":
            encryptedText = encryptedText + hashes[87]
        elif text[i] == "{":
            encryptedText = encryptedText + hashes[88]
        elif text[i] == "|":
            encryptedText = encryptedText + hashes[89]
        elif text[i] == "}":
            encryptedText = encryptedText + hashes[90]
        elif text[i] == "~":
            encryptedText = encryptedText + hashes[91]
    # endregion
    if masolasVagolapra == True:
        pyperclip.copy(encryptedText)
    print()
    cprint(encryptedText, "cyan")
    cprint("\nEnter a továbblépéshez.", "red")
    input()
    start()


def decryptFunction():
    print("\033c", end="")
    print()
    cprint("-------------------Dekódolás--------------------", "yellow")
    cprint("Visszafejtendő szöveg:", "cyan")
    encryptedText=input()
    text=""
    # region Dekódolás
    for i in range(0, int(len(encryptedText)), 10):
        if encryptedText[i:i + 10] == hashes[0]:
            text = text + "a"
        elif encryptedText[i:i + 10] == hashes[1]:
            text = text + "b"
        elif encryptedText[i:i + 10] == hashes[2]:
            text = text + "c"
        elif encryptedText[i:i + 10] == hashes[3]:
            text = text + "d"
        elif encryptedText[i:i + 10] == hashes[4]:
            text = text + "e"
        elif encryptedText[i:i + 10] == hashes[5]:
            text = text + "f"
        elif encryptedText[i:i + 10] == hashes[6]:
            text = text + "g"
        elif encryptedText[i:i + 10] == hashes[7]:
            text = text + "h"
        elif encryptedText[i:i + 10] == hashes[8]:
            text = text + "i"
        elif encryptedText[i:i + 10] == hashes[9]:
            text = text + "j"
        elif encryptedText[i:i + 10] == hashes[10]:
            text = text + "k"
        elif encryptedText[i:i + 10] == hashes[11]:
            text = text + "l"
        elif encryptedText[i:i + 10] == hashes[12]:
            text = text + "m"
        elif encryptedText[i:i + 10] == hashes[13]:
            text = text + "n"
        elif encryptedText[i:i + 10] == hashes[14]:
            text = text + "o"
        elif encryptedText[i:i + 10] == hashes[15]:
            text = text + "p"
        elif encryptedText[i:i + 10] == hashes[16]:
            text = text + "q"
        elif encryptedText[i:i + 10] == hashes[17]:
            text = text + "r"
        elif encryptedText[i:i + 10] == hashes[18]:
            text = text + "s"
        elif encryptedText[i:i + 10] == hashes[19]:
            text = text + "t"
        elif encryptedText[i:i + 10] == hashes[20]:
            text = text + "u"
        elif encryptedText[i:i + 10] == hashes[21]:
            text = text + "v"
        elif encryptedText[i:i + 10] == hashes[22]:
            text = text + "w"
        elif encryptedText[i:i + 10] == hashes[23]:
            text = text + "x"
        elif encryptedText[i:i + 10] == hashes[24]:
            text = text + "y"
        elif encryptedText[i:i + 10] == hashes[25]:
            text = text + "z"
        elif encryptedText[i:i + 10] == hashes[26]:
            text = text + "A"
        elif encryptedText[i:i + 10] == hashes[27]:
            text = text + "B"
        elif encryptedText[i:i + 10] == hashes[28]:
            text = text + "C"
        elif encryptedText[i:i + 10] == hashes[29]:
            text = text + "D"
        elif encryptedText[i:i + 10] == hashes[30]:
            text = text + "E"
        elif encryptedText[i:i + 10] == hashes[31]:
            text = text + "F"
        elif encryptedText[i:i + 10] == hashes[32]:
            text = text + "G"
        elif encryptedText[i:i + 10] == hashes[33]:
            text = text + "H"
        elif encryptedText[i:i + 10] == hashes[34]:
            text = text + "I"
        elif encryptedText[i:i + 10] == hashes[35]:
            text = text + "J"
        elif encryptedText[i:i + 10] == hashes[36]:
            text = text + "K"
        elif encryptedText[i:i + 10] == hashes[37]:
            text = text + "L"
        elif encryptedText[i:i + 10] == hashes[38]:
            text = text + "M"
        elif encryptedText[i:i + 10] == hashes[39]:
            text = text + "N"
        elif encryptedText[i:i + 10] == hashes[40]:
            text = text + "O"
        elif encryptedText[i:i + 10] == hashes[41]:
            text = text + "P"
        elif encryptedText[i:i + 10] == hashes[42]:
            text = text + "Q"
        elif encryptedText[i:i + 10] == hashes[43]:
            text = text + "R"
        elif encryptedText[i:i + 10] == hashes[44]:
            text = text + "S"
        elif encryptedText[i:i + 10] == hashes[45]:
            text = text + "T"
        elif encryptedText[i:i + 10] == hashes[46]:
            text = text + "U"
        elif encryptedText[i:i + 10] == hashes[47]:
            text = text + "V"
        elif encryptedText[i:i + 10] == hashes[48]:
            text = text + "W"
        elif encryptedText[i:i + 10] == hashes[49]:
            text = text + "X"
        elif encryptedText[i:i + 10] == hashes[50]:
            text = text + "Y"
        elif encryptedText[i:i + 10] == hashes[51]:
            text = text + "Z"
        elif encryptedText[i:i + 10] == hashes[52]:
            text = text + "0"
        elif encryptedText[i:i + 10] == hashes[53]:
            text = text + "1"
        elif encryptedText[i:i + 10] == hashes[54]:
            text = text + "2"
        elif encryptedText[i:i + 10] == hashes[55]:
            text = text + "3"
        elif encryptedText[i:i + 10] == hashes[56]:
            text = text + "4"
        elif encryptedText[i:i + 10] == hashes[57]:
            text = text + "5"
        elif encryptedText[i:i + 10] == hashes[58]:
            text = text + "6"
        elif encryptedText[i:i + 10] == hashes[59]:
            text = text + "7"
        elif encryptedText[i:i + 10] == hashes[60]:
            text = text + "8"
        elif encryptedText[i:i + 10] == hashes[61]:
            text = text + "9"
        elif encryptedText[i:i + 10] == hashes[62]:
            text = text + "!"
        elif encryptedText[i:i + 10] == hashes[63]:
            text = text + "#"
        elif encryptedText[i:i + 10] == hashes[64]:
            text = text + "$"
        elif encryptedText[i:i + 10] == hashes[65]:
            text = text + "%"
        elif encryptedText[i:i + 10] == hashes[66]:
            text = text + "&"
        elif encryptedText[i:i + 10] == hashes[67]:
            text = text + "'"
        elif encryptedText[i:i + 10] == hashes[68]:
            text = text + "("
        elif encryptedText[i:i + 10] == hashes[69]:
            text = text + ")"
        elif encryptedText[i:i + 10] == hashes[70]:
            text = text + "*"
        elif encryptedText[i:i + 10] == hashes[71]:
            text = text + "+"
        elif encryptedText[i:i + 10] == hashes[72]:
            text = text + ","
        elif encryptedText[i:i + 10] == hashes[73]:
            text = text + "-"
        elif encryptedText[i:i + 10] == hashes[74]:
            text = text + "."
        elif encryptedText[i:i + 10] == hashes[75]:
            text = text + "/"
        elif encryptedText[i:i + 10] == hashes[76]:
            text = text + ":"
        elif encryptedText[i:i + 10] == hashes[77]:
            text = text + ";"
        elif encryptedText[i:i + 10] == hashes[78]:
            text = text + "<"
        elif encryptedText[i:i + 10] == hashes[79]:
            text = text + "="
        elif encryptedText[i:i + 10] == hashes[80]:
            text = text + ">"
        elif encryptedText[i:i + 10] == hashes[81]:
            text = text + "?"
        elif encryptedText[i:i + 10] == hashes[82]:
            text = text + "@"
        elif encryptedText[i:i + 10] == hashes[83]:
            text = text + "["
        elif encryptedText[i:i + 10] == hashes[84]:
            text = text + "]"
        elif encryptedText[i:i + 10] == hashes[85]:
            text = text + "^"
        elif encryptedText[i:i + 10] == hashes[86]:
            text = text + "_"
        elif encryptedText[i:i + 10] == hashes[87]:
            text = text + "`"
        elif encryptedText[i:i + 10] == hashes[88]:
            text = text + "{"
        elif encryptedText[i:i + 10] == hashes[89]:
            text = text + "|"
        elif encryptedText[i:i + 10] == hashes[90]:
            text = text + "}"
        elif encryptedText[i:i + 10] == hashes[91]:
            text = text + "~"
    # endregion
    if masolasVagolapra == True:
        pyperclip.copy(text)
    print()
    cprint(text, "cyan")
    cprint("\nEnter a továbblépéshez.", "red")
    input()
    start()


def start():
    drawMainMenu()
    selector = int(input())
    if selector == 1:
        encryptFunction()
    if selector == 2:
        decryptFunction()
    if selector == 3:
        print("\033c", end="")
        quit()


start()
