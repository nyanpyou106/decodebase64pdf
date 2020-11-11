import base64
 
with open("pdf.txt", "r") as f:
    bytes_data = f.read()
data = base64.b64decode(bytes_data.encode())
print(type(data))
with open("test.pdf", "wb") as f:
    f.write(data)