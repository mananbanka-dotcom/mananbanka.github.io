import secrets,string,sys
print("Password generator")
try:
    n=int(input("Length (e.g. 16): ").strip())
except:
    print("Invalid length");sys.exit(1)

use_lower=input("Include lowercase? (y/n): ").strip().lower()=="y"
use_upper=input("Include uppercase? (y/n): ").strip().lower()=="y"
use_digits=input("Include digits? (y/n): ").strip().lower()=="y"
use_symbols=input("Include symbols? (y/n): ").strip().lower()=="y"

chars=""
if use_lower: chars+=string.ascii_lowercase
if use_upper: chars+=string.ascii_uppercase
if use_digits: chars+=string.digits
if use_symbols: chars+=string.punctuation

if not chars:
    print("No character sets selected");sys.exit(1)

pw="".join(secrets.choice(chars) for _ in range(n))
print("Generated password:",pw)
