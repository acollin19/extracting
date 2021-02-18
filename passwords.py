
import zipfile
from itertools import product

def extract_zip(zip_filename, password):
    '''
    Parameter: a string corresponding to a zip filename,
           and a string corresponding to a password.
    Return value: boolean indicating whether the password unlocked the zip file.
    '''
    zip_file = zipfile.ZipFile(zip_filename)
    try: 
        zip_file.extractall(pwd=password.encode())
        return True
    except:
        return False

def get_alphabet_combinations(pass_length):
    '''
    Parameter: an integer corresponding to a password length
    Return value: a list of all possible combinations of the lowercase letters a-z
                  of the given length.
    '''
    return [''.join(pw) for pw in product('qwertyuiopasdfghjklzxcvbnm', repeat=pass_length)]    

def brute_force(zip_filename):
# Set password to False so that it doesnt find the password in the loop it will print it 'No password..." and keep running
    password_found=False
# For the password length to run until it reaches length 4
    for pass_length in range(1,5):
        combination=get_alphabet_combinations(pass_length)
# If there is a letter match in the combination then check if extract_zip confirms if it opens the file
        for match in combination:
            if extract_zip(zip_filename, match):
# If it opens the file then print the password match
                password_found=True
                print("Password found: ", match)
                break
# If it does not match then the password has not ben found and it reruns through loop            
        if password_found==False:
            print("No password found of length", pass_length)
                               

def dictionary(zip_filename, dict_filename):    
    password_found=False
    fobj=open(dict_filename, "r")
# Open the file and turn it into list of strings
    file_contents=fobj.read().split()
    fobj.close()
# For each string in the list of strings 
    for word in range(len(file_contents)):
# If at the index of a string in the list of strings it opens the zipfile then print
        if extract_zip(zip_filename, file_contents[word]):
# Take the word at the index that opens the file
            password=file_contents[word]
            password_found=True
            print("Password found: ", password)
# If none of the strings in the list of strings opens the file then print this                        
    if password_found==False:
        print("No password found.")
            

def test_password_strength(password, dict_filename):
# Checking brute-force attack
    password_found=False
# For the combinations of letters from length 1-4
    for pass_length in range(1,5):
        combination=get_alphabet_combinations(pass_length)
# If the password is in this combination then password is found and print statement
        for password in combination:
            password_found=True
    print ("Password is susceptible to brute-force attack.")

# Testing dictionary attack 
    password_found=False
    fobj=open(dict_filename, "r")
    file_contents=fobj.read().split()
    fobj.close()
# If the password is in the file_contents then print statement
    if password in file_contents:
        password_found=True
    print ("Password is susceptible to dictionary attack.")
        
# Print introductory sentences and allow user to input choice
def menu():
    print("Welcome to the Passwords Program.")
    print("Note: Unauthorized use of computer in Canada is a federal crime under the Criminal Code (R.S.C.,1985,c.C-46) Section 342.1. If found guilty, maximun penalty for violation of  this law is imprisonment for up to 10 years.")
    print("What would you like to do?")
    print("1) Test a password")
    print("2) Find a password for zip file using brute-force")
    print("3) Find a password for zip file using dictionary")
    print("4) Exit")
    user_input=int(input())

# If user inputs 1, they get the test_password_strength function
    if user_input==1:
        password=input("Enter a password: ")
        dict_filename=input("Enter dictionary file name: ")
        test_password_strength(password, dict_filename)
# If user inputs 2, they get the brute force function         
    elif user_input==2:
        zip_filename=input("Enter zip file name: ")
        brute_force(zip_filename)
# If the user inputs 3, they get the dictionary attack function       
    elif user_input==3:
        zip_filename=input("Enter zip file name: ")
        dict_filename=input("Enter dictionary file name: ")
        dictionary(zip_filename, dict_filename)
# If user inputs 4 or other they exit the program or get to reinput a choice        
    elif user_input==4:
        print("See ya!")
    else:
        print("Invalid input.")
        menu()
        

# Please do not alter anything below this line.
if __name__ == '__main__':
    menu()

