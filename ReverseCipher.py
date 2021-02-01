def enReverseCipher(txt):

  encrypted = ''
  i = len(txt) - 1
  while i >= 0:
   encrypted = encrypted + txt[i]
   i = i - 1
  print(encrypted)


enReverseCipher("Huitzi")

def deReverseCipher(txt):
  
  decrypted = ""
  i = len(txt) - 1
  while i >= 0:
    decrypted = decrypted + txt[i]
    i = i - 1
  print(decrypted)

deReverseCipher("iztiuh")
