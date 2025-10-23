string = input("ENTER THE STRING:")
first = string[0]
mod_str = first+string[1:].replace(first,'$')
print("Modified String:",mod_str)