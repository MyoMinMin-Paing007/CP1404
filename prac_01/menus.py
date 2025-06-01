"""
CP1404 - Practical
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
menu=["(H)ello" , "(G)oodbye" , "(Q)uit"]
name=input("Enter name:")
print(menu)
choice=input(">>>").upper()
while choice!="Q":
    if choice=="H":
        print("Hello")
    elif choice=="G":
        print("Goodbye")
    else:
        print("Invalid message")
    print(menu)
    choice=input(">>>").upper()

print("Finished!")