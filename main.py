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

Use_for = l_case + u_case + num + sym


pwd = "".join(random.sample(Use_for, pwd_len))

print(f'Your Generated Password is: {pwd}')

#dictionary of creds
dict = {'Service': service, 'Username': uname, 'Password': pwd}

df = pd.DataFrame(dict, index=[0])

#save dataframe
df.to_csv('database.csv', mode='a', index=False, header=False)