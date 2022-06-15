print("===========================================================")
print("========== TUGAS BESAR TEORI BAHASA DAN AUTOMATA ==========")
print("===========================================================")
print("===========     LEXICAL ANALYZER dan PARSER     ===========")
print("===========================================================")
print("============   KELOMPOK 14 || KELAS IF-44-10   ============")
print("===                                                     ===")
print("===  Berlian Muhammad Galin Al Awienoor   (1301204378)  ===")
print("===  Kiki Dwi Prasetyo                    (1301204027)  ===")
print("===  Eric Nur Rahman                      (1301200010)  ===")
print("===                                                     ===")
print("===========================================================")
print("                                                           ")

import string

#Fungsi Lexical Analysis
def lexical(sentence):

    #Initialization || menginialisasi semua state
    alphabet_list = list(string.ascii_lowercase) #mengubah semua huruf ke lowercase
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 
                'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 
                'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29']

    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = "error"
            transition_table[(state, "#")]      = "error"
            transition_table[(state, " ")]      = "error"

    #Initial State (start)
    transition_table["q0", " "]    = "q0"

    #Finish State (FS)
    transition_table[("q28", "#")] = "accept"
    transition_table[("q28", " ")] = "q29"

    transition_table[("q29", "#")] = "accept"
    transition_table[("q29", " ")] = "q29"

    #Subject
    #String "amang"
    transition_table[("q0", "a")]  = "q1"
    transition_table[("q2", "m")]  = "q4"
    transition_table[("q4", "a")]  = "q5"
    transition_table[("q5", "n")]  = "q6"
    transition_table[("q6", "g")]  = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "a")] = "q2"

    #String "inang"
    transition_table[("q0", "i")]  = "q1"
    transition_table[("q1", "n")]  = "q4"
    transition_table[("q4", "a")]  = "q5"
    transition_table[("q5", "n")]  = "q6"
    transition_table[("q6", "g")]  = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "i")] = "q1"

    #String "hami"
    transition_table[("q0", "h")]  = "q3"
    transition_table[("q3", "a")]  = "q2"
    transition_table[("q2", "m")]  = "q4"
    transition_table[("q4", "i")]  = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "h")] = "q3"

    #String "au"
    transition_table[("q0", "a")]  = "q2"
    transition_table[("q2", "u")]  = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "a")] = "q2"
    
    #Verb
    #String "mangan"
    transition_table[("q0", "m")]  = "q7"
    transition_table[("q7", "a")]  = "q8"
    transition_table[("q8", "n")]  = "q9"
    transition_table[("q9", "g")]  = "q10"
    transition_table[("q10", "a")] = "q11"
    transition_table[("q11", "n")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "m")] = "q7"

    #String "maniop"
    transition_table[("q0", "m")]  = "q7"
    transition_table[("q7", "a")]  = "q8"
    transition_table[("q8", "n")]  = "q9"
    transition_table[("q9", "i")]  = "q12"
    transition_table[("q12", "o")] = "q13"
    transition_table[("q13", "p")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "m")] = "q7"

    #String "mamonggol"
    transition_table[("q0", "m")]  = "q7"
    transition_table[("q7", "a")]  = "q8"
    transition_table[("q8", "m")]  = "q14"
    transition_table[("q14", "o")] = "q15"
    transition_table[("q15", "n")] = "q9"
    transition_table[("q9", "g")]  = "q10"
    transition_table[("q10", "g")] = "q10"
    transition_table[("q10", "o")] = "q16"
    transition_table[("q16", "l")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "m")] = "q7"
    
    #Object
    #String "dekke"
    transition_table[("q0", "d")]  = "q17"
    transition_table[("q17", "e")] = "q18"
    transition_table[("q18", "k")] = "q19"
    transition_table[("q19", "k")] = "q19"
    transition_table[("q19", "e")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "d")] = "q17"

    #String "boras"
    transition_table[("q0", "b")]  = "q20"
    transition_table[("q20", "o")] = "q21"
    transition_table[("q21", "r")] = "q22"
    transition_table[("q22", "a")] = "q23"
    transition_table[("q23", "s")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "b")] = "q20"

    #String "sibuk"
    transition_table[("q0", "s")]  = "q24"
    transition_table[("q24", "i")] = "q25"
    transition_table[("q25", "b")] = "q26"
    transition_table[("q26", "u")] = "q27"
    transition_table[("q27", "k")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "s")] = "q24"

    #Lexical Analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    print("                                         ")
    print("=========================================")
    print("===      PROSES LEXICAL ANALYZER      ===")
    print("========================================= \n")
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q28':
            print('CURRENT TOKEN  : ', current_token, ', valid')
            current_token = ''
        if state =="error":
            print('ERROR')
            break
        idx_char = idx_char + 1

    #Conclusion || state yang di accept
    if state == "accept":
        print('SEMUA TOKEN YANG DIINPUT : ', sentence, ', valid')
        status = True
    else:
        status = False
    
    return status


#Fungsi Parser
def parser(sentence):
    print("                                         ")
    print("=========================================")
    print("===           PROSES PARSER           ===")
    print("========================================= \n")

    tokens = sentence.lower().split()
    tokens.append('EOS')

    non_terminals = ['S', 'SB', 'VB', 'OB']
    terminals = ['amang', 'inang', 'au', 'hami', 'mangan', 'maniop', 'mamonggol', 'boras', 'dekke', 'sibuk']

    parse_table = {}

    #Parse Table S
    parse_table[('S', 'amang')]      = ['SB', 'VB', 'OB']
    parse_table[('S', 'inang')]      = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'au')]         = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'hami')]       = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'mangan')]     = ['error']
    parse_table[('S', 'maniop')]     = ['error'] 
    parse_table[('S', 'mamonggol')]  = ['error'] 
    parse_table[('S', 'boras')]      = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'dekke')]      = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'sibuk')]      = ['SB', 'VB', 'OB']  
    parse_table[('S', 'EOS')]        = ['error'] 

    #Parse Table SB
    parse_table[('SB', 'amang')]     = ['amang']
    parse_table[('SB', 'inang')]     = ['inang']  
    parse_table[('SB', 'au')]        = ['au'] 
    parse_table[('SB', 'hami')]      = ['hami']
    parse_table[('SB', 'mangan')]    = ['error'] 
    parse_table[('SB', 'maniop')]    = ['error'] 
    parse_table[('SB', 'mamonggol')] = ['error'] 
    parse_table[('SB', 'boras')]     = ['error'] 
    parse_table[('SB', 'dekke')]     = ['error'] 
    parse_table[('SB', 'sibuk')]     = ['error'] 
    parse_table[('SB', 'EOS')]       = ['error'] 
    
    #Parse Table VB
    parse_table[('VB', 'amang')]     = ['error']
    parse_table[('VB', 'inang')]     = ['error']
    parse_table[('VB', 'au')]        = ['error']
    parse_table[('VB', 'hami')]      = ['error']
    parse_table[('VB', 'mangan')]    = ['mangan'] 
    parse_table[('VB', 'maniop')]    = ['maniop'] 
    parse_table[('VB', 'mamonggol')] = ['mamonggol'] 
    parse_table[('VB', 'boras')]     = ['error'] 
    parse_table[('VB', 'dekke')]     = ['error'] 
    parse_table[('VB', 'sibuk')]     = ['error'] 
    parse_table[('VB', 'EOS')]       = ['error'] 

    #Parse Table OB
    parse_table[('OB', 'amang')]     = ['error']
    parse_table[('OB', 'inang')]     = ['error']
    parse_table[('OB', 'au')]        = ['error']
    parse_table[('OB', 'hami')]      = ['error']
    parse_table[('OB', 'mangan')]    = ['error'] 
    parse_table[('OB', 'maniop')]    = ['error'] 
    parse_table[('OB', 'mamonggol')] = ['error'] 
    parse_table[('OB', 'boras')]     = ['boras'] 
    parse_table[('OB', 'dekke')]     = ['dekke']
    parse_table[('OB', 'sibuk')]     = ['sibuk'] 
    parse_table[('OB', 'EOS')]       = ['error'] 

    stack = []
    stack.append('#')
    stack.append('S')

    index_token = 0
    symbol = tokens[index_token]

    #Parser
    while(len(stack) > 0):
        top = stack[ len(stack) - 1 ]
        print('TOP    : ', top)
        print('SYMBOL : ', symbol)
        if top in terminals:
            print('TOP ADALAH SYMBOL TERMINAL')
            if top == symbol:
                stack.pop()
                index_token = index_token + 1
                symbol = tokens[index_token]
                if symbol == "EOS":
                    stack.pop()
                    print('ISI STACK : ', stack)
            else:
                print('ERROR')
                break;
        elif top in non_terminals:
            print('TOP ADALAH SYMBOL NON-TERMINAL')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbol_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbol_to_be_pushed)-1, -1, -1):
                    stack.append(symbol_to_be_pushed[i])
            else:
                print('ERROR')
                break;
        else:
            print('ERROR')
            break;
        print('ISI STACK : ', stack)
        print()
    print()

    #Conclusion || Hasil Akhir dari Proses Parser 
    if symbol == 'EOS' and len(stack) == 0:
        print('Inputan String ', '"', sentence, '"', 'Diterima, Sesuai Grammar')
    else:
        print('ERROR, Inputan String:', '"', sentence, '"', ', Tidak Diterima, Tidak Sesuai Grammar')  
    
    return parser


#Main Program 
print("===============    TERMINAL    ===============")
print("===   SUBJECT : amang, inang, hami, au     ===")
print("===   VERB    : mangan, maniop, mamonggol  ===")
print("===   OBJECT  : boras, dekke, sibuk        ===")
print("============================================== \n ")
sentence = input("MASUKKAN INPUT : ",)
input_string = sentence.lower()+'#'

if lexical(sentence):
    parser(sentence)
else:
    print("\n=========================================")
    print("===        LEXICAL TIDAK VALID        ===")
    print("===    TIDAK AKAN DILAKUKAN PARSER    ===")
    print("=========================================")
