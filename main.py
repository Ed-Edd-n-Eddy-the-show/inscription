with open("inscribed.txt", "w") as file_setup:
    file_setup.write("\nwe hope you enjoy learning Python with us!\n\nBest,\nTh3 31337 AP Computer Science Team")

def GetNameAndFile():
    name = input("Whom should I sign this to: ")
    file_name = input("Where shall I save it: ")
    return name, file_name

def InscriptANameOnAFile():
    name, file_name  = GetNameAndFile()
    with open("inscribed.txt", "r") as file:
        old_content = file.read()
    #print(old_content)

    name_adrested = "\nHi " + name
    new_content = name_adrested + old_content
    
    with open(file_name, "w") as file_to_write:
        file_to_write.write(new_content)
    return file_name    
 


file_name = InscriptANameOnAFile() 
with open(file_name, "r") as file:
    content = file.read()
    print(content)