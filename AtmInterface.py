# Code By :- Shripad Kulkarni 
# Date:- 27/02/2024
# --------------------------------------ATM INTERFACE--------------------------------------

class AtmInterface:
    AccountBalance1= 600000;
    print("Welcome To BANK OF INDIA");
    
    print("Kindly Choose Your Language");
    
    print("1.English\n2.Hindi\n3.Marathi");
    
    LangInp=int(input());
     
    if (LangInp==1):
        print("Please Insert Your Card");
        print("Please DO NOT REMOVE CARD DURING TRANSECTION");
        print("Please Enter Your 4 Digit Pin");
        AtmPin=int(input());
        if(AtmPin==1234):
            print("Choose The Following Option\n1.Withdrawl\n2.Account Balance\n3.Change Pin\n4.Exit ");
            UserInput1=int(input());
            if(UserInput1==1):
             print("Please Enter The Amount In Multiple Of 100");
             WithdrawAmount=int(input());
             if(WithdrawAmount%100==0):
               if(WithdrawAmount<AccountBalance1):
                 print("Please Wait While Your Transection has been proceed");
                 print("Please Collect the cash");
                 print("Press \n1.Exit\n2.Check Account Balance");
                 UserInput2=int(input());
                 if(UserInput2==2):
                     AccountBalanceRemaining= AccountBalance1-WithdrawAmount;
                     print("Your Account Balance is RS."+str(AccountBalanceRemaining)+"/-Only :) ");
                 elif(UserInput2==1):
                     print("Thank You For Visiting BANK OF INDIA \n Visit Again :) ");
                 else:
                     print("Option Invalid");
               else:
                   print("Insufficient Account Balance");
                   exit()
             else:
                 print("INVALID AMOUNT Please Enter Amount in Multiple Of 100");
                 exit()
            elif(UserInput1==2):
                print("Your Account Balance is RS."+str(AccountBalance1)+"/- Only Thank You Visit Again");
                exit()
            elif(UserInput1==3):
                print("please enter your new pin");
                AtmPin=int(input());
                print("pin successfully changed Thank You Visit Again");
            elif(UserInput1==4):
                print("Thank You For Visiting BANK OF INDIA \n Visit Again :)");
                exit()
            else:
                print("Invalid Option Kindly Try again");
                exit()
        else:
                print("Invalid Pin 3 Attempts Left");
                exit()
    else:
        print("Our ATM Currently Only Support with English \n Sorry For Inconvenience");
        exit()
            
                
                    
                 
                 
            
    
              
               