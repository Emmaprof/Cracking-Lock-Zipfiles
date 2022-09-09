import zipfile
from tqdm import tqdm

#Let's specify our target zip file along with the word list path:
# the password list path you want to use, must be available in the current directory
wordlist = "C:/Users/hp/Desktop/zip.txt"
# the zip file you want to crack its password
zip_file = "C:/Users/hp/Desktop/Take Home Test ele317.zip"

# To read the zip file in Python, we use the zipfile.ZipFile class that has methods to open, read, write, close, 
# list and extract zip files (we will only use extractall() method here):

# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            print(word.strip())
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
