# KU ECE CGPA Calculator
 
credits = [20.5,21.5,24,25,24,23,15,12]
SGPA = []
BRANCH = input("Enter your Branch name (CSE,MINING,EEE,ECE,IT) : ")
NAME = input("NAME : ")
if((BRANCH.upper())=="ECE"):
    
    n=int(input("\nNo. of semesters = "))
    print()
    
    for i in range (0,n,1) :
        print("Enter the semester",i+1,"SGPA : ",end=" ");x=float(input())
        SGPA.append(x)
    
        if(i==(n-1)) :
            print("\nThe Sem SGPAs you entered are : ",SGPA)
            Reqcredits=credits[0:n]
            print("\nThe credits for the",n,"semesters are : ",Reqcredits)
        
            Den=0
            Num=0
            avg=0
            for j in range (0,n,1):
                Average = SGPA[j]/(n)
                avg=avg+Average
                SGPA_total=SGPA[j]*Reqcredits[j]
                Num=Num+SGPA_total
                Den=Den+Reqcredits[j]
                
                if (j==(n-1)):
                    print("\nThe average of",n,"Sems is : ",avg," ≈ ",round(avg,2))
                    CGPA=Num/Den
                    print("\nThe CGPA of",n,"Semesters is :",CGPA," ≈ ",round(CGPA,2))
                    percentage=(((round(CGPA,2))*10)-3.69)
                    print("\nThe percentage conversion of CGPA of ",n,"semesters is : ",percentage,"%"," ≈ ",round(percentage,2),"%")
                    
                
else :
    print("Only for ECE Students...")
    