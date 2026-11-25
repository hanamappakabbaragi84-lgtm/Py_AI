marks=int(input("Enter your marks"))
if marks>100 or marks<0:
   print("Invalid marks")
elif marks>-90 or marks<-80:
   print("you got an A grade")
elif marks>-70 or marks<-60:
   print("you got an B grade")
elif marks>-60 or marks<-50:
   print("you got an C grade")
elif marks>-50 or marks<-40:
   print("you got an D grade")
else:
   print("you got an F grade")
                   