def parser(sentence):
    print("=========================================")
    print("=======       PROSES PARSER       =======")
    print("========================================= \n")

    tokens = sentence.lower().split()
    tokens.append('EOS')

    non_terminals = ['S', 'SB', 'VB', 'OB']
    terminals = ['amang', 'inang', 'au', 'hami', 'mangan', 'maniop', 'mamonggol', 'boras', 'dekke', 'sibuk']

    parse_table = {}

    parse_table[('S', 'amang')]     = ['SB', 'VB', 'OB']
    parse_table[('S', 'inang')]     = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'au')]        = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'hami')]      = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'mangan')]    = ['error']
    parse_table[('S', 'maniop')]    = ['error'] 
    parse_table[('S', 'mamonggol')] = ['error'] 
    parse_table[('S', 'boras')]     = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'dekke')]     = ['SB', 'VB', 'OB'] 
    parse_table[('S', 'sibuk')]     = ['SB', 'VB', 'OB']  
    parse_table[('S', 'EOS')]       = ['error'] 

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

    while(len(stack) > 0):
        top = stack[ len(stack) - 1 ]
        print('TOP    = ', top)
        print('SYMBOL = ', symbol)
        if top in terminals:
            print('TOP ADALAH SYMBOL TERMINAL')
            if top == symbol:
                stack.pop()
                index_token = index_token + 1
                symbol = tokens[index_token]
                if symbol == "EOS":
                    stack.pop()
                    print('ISI STACK:', stack)
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
        print('ISI STACK: ', stack)
        print()

    print()
    if symbol == 'EOS' and len(stack) == 0:
        print('Inputan String ', '"', sentence, '"', 'Diterima, Sesuai Grammar')
    else:
        print('ERROR, Inputan String:', '"', sentence, '"', ', Tidak Diterima, Tidak Sesuai Grammar')  
    
    return parser

#Main Program Parser
print("============= TERMINAL =============")
print("SUBJECT : amang, inang, hami, au")
print("VERB    : mangan, maniop, mamonggol")
print("OBJECT  : boras, dekke, sibuk")
print("==================================== \n ")
sentence = input("MASUKKAN INPUT : ")
input_string = sentence.lower()+'#'
parser(sentence)