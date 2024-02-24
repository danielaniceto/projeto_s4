import pymysql
print(pymysql.__version__)

mysql = pymysql.connect(host="localhost", port="3306", user="root", passwd="1234", database="produtoSB")

