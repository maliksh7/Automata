import re 
  
regular_expression = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
       
def chk_Email(str):  
  
    if(re.search(regular_expression,str)):  
        ans = "Valid Email Address"
        return ans  
          
    else:  
        ans = "Invalid Email Address"
        return ans         
      
  
 
if __name__ == "__main__": 
    pass  
      
  
print("case 1:")
print(chk_Email("saadmalik-326@gmail.com")) 

print("case 2:") 
print(chk_Email("sh123@gmail.com"))

print("case 3:")
print(chk_Email("my.own_form@yahoo.org")) 

print("case 4:")  
print(chk_Email("my.ms123office@hotmail.org"))

print("case 5:")
print(chk_Email("my-website786@wordpress.com"))

print("case 6:")
print(chk_Email("myschool786.com"))

print("case 7:")
print(chk_Email("myschool786@com"))

