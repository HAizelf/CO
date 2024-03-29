from error_updated import *
#paste error_updated wala part here
#2nd pass
Bin_reg = {"R0":"000", "R1":"001", "R2":"010", "R3":"011", "R4": "100", "R5": "101", "R6":"111"}
#converts given integer to 8 bit binary
def Binary(n):
    Bin=""
    while n:
        Bin=str(n%2)+Bin
        n=n//2
    while len(Bin)<8:
        Bin="0"+Bin
    return Bin

non_var_len = len(mem_addr)     
mem_addr = mem_addr + mem_add_var

def print_instruction(instruction_code,type):    
        machine_code="\n"
        i=0
        if type =="A":
            #ignore labels and find executable instruction
            while True:
                if(instruction_code[i] not in type_A.keys()):
                    i=i+1
                else: 
                    key=instruction_code[i]
                    break
            opcode=type_A[key]
            unused_bits="00"
            machine_code=opcode+unused_bits+Bin_reg[instruction_code[i+1]]+Bin_reg[instruction_code[i+2]]+Bin_reg[instruction_code[i+3]]

        elif type == 'B':
            while True:
                if(instruction_code[i] not in type_B.keys()):
                    i=i+1
                else: 
                    key=instruction_code[i]
                    break
            opcode=type_B[key]
            imm=Binary(int(instruction_code[i+2].replace("$","")))
            machine_code=opcode+Bin_reg[instruction_code[i+1]]+imm
            
        elif type == 'C':
            while True:
                if(instruction_code[i] not in type_A.keys()):
                    i=i+1
                else: 
                    key=instruction_code[i]
                    break
            opcode=type_C[key]
            machine_code = type_C[opcode]+ "00000" + Bin_reg[instruction_code[i+1]] + Bin_reg[instruction_code[i+2]]
            
         
        elif type == 'D':
            while True:
                if(instruction_code[i] not in type_A.keys()):
                    i=i+1
                else: 
                    key=instruction_code[i]
                    break
            opcode=type_D[key]
            var_mem_add = non_var_len + variable_names.index(instruction_code[i+1])
            machine_code = type_D[opcode] + Bin_reg[instruction_code[i+1]] + format(var_mem_add, '08b')
         
        elif type=="E":
            while True:
                if(instruction_code[i] not in type_E.keys()):
                    i=i+1
                else: 
                    key=instruction_code[i]
                    break
            opcode=type_E[key]
            unused_bits="000"
            label=instruction_code[1]
            mem_index= str(format(label_add[label], '08b'))
            machine_code=opcode+unused_bits+mem_index
            
        
        elif type=="F":
            while True:
                if(instruction_code[i] !="hlt"):
                    i=i+1
                else: 
                    break
            machine_code="1001100000000000"
    
        print(machine_code)
    
        

for instruction_code in Data_updated:
    type=check_type1(instruction_code)
    print_instruction(instruction_code,type)   
