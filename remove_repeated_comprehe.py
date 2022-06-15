#to remove repeated characters in string using list

def main():
    str=input("enter name")
    new=''.join([c for i,c in enumerate(str) if c not in str[:i]])
    print(new)
main()

#