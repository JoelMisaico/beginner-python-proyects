import qrcode ##import the library

data = input("Ingrese su link para generar el código QR")


img = qrcode.make(data) ##create the matrix of QR


img.save("code.png") # save the code