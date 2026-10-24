# grade_score > 90 then A+
# grade_score > 80 and <= 90 then A
# grade_score > 70 and <= 80 then B
# grade_score > 60 and <= 70 then C
# grade_score > 50 and <= 60 then D
# grade_score > 40 and <= 50 then E
# grade_score < 40 then F

Grade_Score = int(input("Enter Your Score = "))
if(Grade_Score > 90):
    print("Your Grade is A+!")
elif(Grade_Score > 80 and Grade_Score <= 90):
    print("Your Grade is A!")
elif(Grade_Score > 70 and Grade_Score <= 80):
   print("Your Grade is B!")
elif(Grade_Score > 60 and Grade_Score <= 70):
    print("Your Grade is C !")
elif(Grade_Score > 50 and Grade_Score <= 60):
    print("Your Grade is D !")
elif(Grade_Score > 40 and Grade_Score <= 50):
    print("Your Grade is E !")
else:
    print("Your Grade is F !")
