class ConditionalStatement:
     print("Enter The First Value");
     a=int(input());
     print("Enter The Second Value");
     b=int(input());
     print("Enter The Third Value")
     c=int(input());
     
     if(a>b):
         
             if (a>c):
                 print("a is greater");
                 
             else:
                 print("c is greater");
            
     elif(a<b):
          if(b<c):
            print("c is greater");
          else:
            print("b is greater");
            
     elif (a<c):
          if(b<c):
           print("c is greater");
          else:
            print("b is greater");
            
        
            
     else:
         print("all are same");