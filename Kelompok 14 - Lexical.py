print("===========================================================")
print("========== TUGAS BESAR TEORI BAHASA DAN AUTOMATA ==========")
print("===========================================================")
print("===================== LEXICAL ANALYZER ====================")
print("============== KELOMPOK 14 || KELAS IF-44-10 ==============")
print("===                                                     ===")
print("===  Berlian Muhammad Galin Al Awienoor   (1301204378)  ===")
print("===  Kiki Dwi Prasetyo                    (1301204027)  ===")
print("===  Eric Nur Rahman                      (1301200010)  ===")
print("===                                                     ===")
print("===========================================================")
print("                                                           ")

import string

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
    
    return lexical

#Main Program Lexical
print("======== TERMINAL ========")
print("amang, inang, hami, au")
print("mangan, maniop, mamonggol")
print("boras, dekke, sibuk")
print("========================== \n ")
sentence = input("MASUKKAN INPUT : ",)
input_string = sentence.lower()+'#'
lexical(sentence)