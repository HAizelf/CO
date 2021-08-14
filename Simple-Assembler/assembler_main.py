

#1 add the code from error.py here

"""""
#2 second pass
"""""
#add check encoding type function here
valid_instructions=["add","sub","mul","xor","or","and","mov","rs","ls","div","not","cmp","ld","st","jmp","jlt","jgt","je","hlt"]
valid_register_names=["R0","R1","R2","R3","R4","R5","R6","FLAGS"]  
valid_label_names=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_","1","2","3","4","5","6","7","8","9","0",":"]

type_A={"add":"00000","sub": "00001","mul":"00110","xor":"01010","or":"01011","and":"01100"}
type_B={"mov" : "00010","rs":"01000","ls":"01001" }   #typeB contains $Imm value
type_C={"mov": "00011","div":"00111","not":"01101","cmp":"01110"}
type_D={"ld":"00100","st":"00101"}
type_E={"jmp":"01111","jlt":"10000","jgt":"10001","je":"10010"}


with open("sample_read_instruction.txt","r") as f:
    lines=f.readlines()
    Data = [Line for Line in lines if Line.strip()]		# we store the lines in the form of an array of strings
    		# Ignoring empty lines
            
variable_names=[]            
Data_updated=[]
mem_add_var=[]            
for x in Data:
    i+=1 # here i stores the line no
    #x=x.strip() #removes extra lines from the instructions
        # if i== line where error is, then print the error and stop execution
        # else continue
    instruction_code=x.split()
    Data_updated.append(instruction_code)
    if(check_type(instruction_code)=="variable"):
        variable_names.append(instruction_code[1])
        mem_add_var.append(instruction_code)

    if(check_type(instruction_code)!="variable"):
        mem_addr.append(instruction_code)

non_var_len = len(mem_addr)     
mem_addr = mem_addr + mem_add_var
    
for x in mem_addr:    
    Bin_reg = {"reg0":"000", "reg1":"001", "reg2":"002", "reg3":"011", "reg4": "100", "reg5": "101", "reg6":"111"}
    
    if check_syntax(x) == 'A':
    
    elif check_syntax(x) == 'B':
    
    elif type == 'C':
        while True:
            if(instruction_code[i] not in type_A.keys()):
                i=i+1
            else: 
                key=instruction_code[i]
                break
        opcode=type_C[key]
        print(type_C[opcode]+ "00000" + Bin_reg[instruction_code[i+1] + Bin_reg[instruction_code[i+2] )
    
    elif type == 'D':
        while True:
            if(instruction_code[i] not in type_A.keys()):
                i=i+1
            else: 
                key=instruction_code[i]
                break
        opcode=type_D[key]
        var_mem_add = non_var_len + variable_names.index(instruction_code[i+1])
        print(type_D[opcode]) + Bin_reg[instruction_code[i+1] + format(var_mem_add, '08b')) 
    
    elif check_syntax(x) == 'E':
