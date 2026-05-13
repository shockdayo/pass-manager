import pyotp

secret = pyotp.random_base32()

with open("otp_secret.txt", "w") as f:
    f.write(secret)

print("SECRET KEY:", secret)