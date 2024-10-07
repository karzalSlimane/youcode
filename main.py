def decoding_message():
    n =  int(input())
    decoded_message  ="" 
    for i in range(n):
        c = int(input())
        if c == 0 :
           decoded_message += " "
        else : 
           decoded_message += chr( c + 96)
    print(decoded_message)

decoding_message()