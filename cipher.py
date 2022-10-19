## This is an augmented version of the Caesar cipher, where the cipher shifts values after every letter making it harder to decrypt
## Also added a swap function to replace the encrypted letter with another letter

## ask user for a message to be encrypted
message = input("Enter a message to be encrypted: ")

## holds the encrypted message
encrypted = ""

## create a variable to hold the shift amount
shift = 0

## loop through each letter in the message (ignoring spaces and numbers) to be encrypted
for letter in message:
    if letter.isalpha():
        ## check the unicode to determine if its a letter
        value = ord(letter)
        ## add the shift amount to the unicode number
        value += shift
        ## Check if its uppercase
        if letter.isupper():
            ## if the value is greater than Z to reset to A
            if value > ord("Z"):
                value -= 26
            elif value < ord("A"):
                ## add 26 to the value
                value += 26
        ## if the letter is lowercase
        elif letter.islower():
            ## if the value is greater than z reset to a
            if value > ord("z"):
                value -= 26
                
            ## if the value is less than a
            elif value < ord("a"):
                value += 26

        ## convert the value back to a letter
        letter = chr(value)
        encrypted += letter
        shift += 1

    ## if the character is not a letter, add it to the encrypted message and do not shift
    else:
        encrypted += letter
        
## display the encrypted message
print(encrypted)

