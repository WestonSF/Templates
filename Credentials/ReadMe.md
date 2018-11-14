# Credentials Python Package

- Install python 2.7.x
- Run EncryptPassword.py
    - Enter in password
    - Copy encrypted password and username into Credentials.py file
    - Press enter to compile
- Copy Credentials.pyc and DecryptPassword.pyc files to your project and use the following code to get the password:
```python
import Credentials
import DecryptPassword
print DecryptPassword.decryptPassword(Credentials.password)
```