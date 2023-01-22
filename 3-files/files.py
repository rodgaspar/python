# Handling files
file = open("estados.txt")

# .read - read file
file_data = file.read()
print(file_data)
print("-----------")
file.close

# .readline - read one record file
file = open("estados.txt")
record = file.readline()
print(record)
print("-----------")
file.close

# .readlines - read all record file
file = open("estados.txt")
file_w = open("estados_gravados.txt", "w" )
records = file.readlines()
for record in records:
    file_w.write(record)
    print(record)
print("-----------")
file.close
file_w.close
