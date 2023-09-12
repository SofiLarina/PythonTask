# На вход подается строка, например: “ААААBBBCCF”
# напишите программу кодирующую эту строку по принципу: “4A3B2C1F”
string = "ААААBBBCCF"
result = ""

for i in set(string):
    number = string.count(string[0])
    result += str(number)
    result += string[0]
    string = [j for j in string if j != string[0]]

print(result)
