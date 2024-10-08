def decoding_message():
     #look up for input and converts it to integer 
    n = int(input())
    #create an empty stirng to store the decoded meassage 
    decoded_message  ="" 
    #look up for n inputs 
    for i in range(n):
        #accept input each time the loop trigers 
        c = int(input())
        
        if c == 0 :
           decoded_message += " "
        else : 
           decoded_message += chr( c + 96)
    print(decoded_message)

decoding_message()


