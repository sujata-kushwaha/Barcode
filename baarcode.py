# from barcode import EAN13 # EAN13 is a type off bARCODE
# from barcode import Code39 # Code39 is take a char with digit
from barcode import Code128
# from barcode.writer import ImageWriter # pillow module is used to creat the barcode in the image formate
num = "67%6hdy3%%76*47$89#78#"
mybarcode = Code128(num)
# mybarcode=EAN13(num,writer=ImageWriter())
mybarcode.save("newcode1")
