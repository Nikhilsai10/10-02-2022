stname=input("Enter student name:")
stno=int(input("Enter the student rno:"))
stgroup=input("Enter the student group:")
sub01=int(input("Enter the OS marks:"))
sub02=int(input("Enter the Java marks:"))
sub03=int(input("Enter the AFM marks:"))
sub04=int(input("Enter the Hindi marks:"))
sub05=int(input("Enter the English marks:"))
sub06=int(input("Enter the Analytical skills marks:"))
if  sub01>=35 and sub02>=35 and sub03>=35 and sub04>=35 and sub05>=35 and sub06>=35:
    print("-----PASS")
else: 
    print("-----FAIL")
