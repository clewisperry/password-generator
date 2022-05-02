# generate and store passwords
# this is not a secure way to store passwords, 
# it is intended to be imported into your favorite password manager

# import pandas for creating dataframe and storing to csv
# import random for random generation
import pandas as pd
import random



service = input('Enter name of service: ') # ask for site or service name
uname = input('Enter Username: ') # ask for username
pwd_len = int(input('Desired password length? (Default: 8): ') or 8) # ask for desired pw length, return default value on emty string

l_case = "abcdefghijklmnopqrstuvwxyz" # lowercase chars
u_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # uppercase chars
num = "0123456789" # integers
sym = "@#$%^&*/\?" # symbols
fname = f'{uname}@{service}.csv'# filenaem

Use_for = l_case + u_case + num + sym # Create a string of all chars integers and symbols.


pwd = "".join(random.sample(Use_for, pwd_len)) # create a random password from given string

print(f'Your Generated Password is: {pwd}') # print password to console


dict = {'Service': service, 'Username': uname, 'Password': pwd} # dictionary of creds


df = pd.DataFrame(dict, index=[0]) # create dataframe from dictionary


df.to_csv(fname, mode='a', index=False, header=False) # save dataframe