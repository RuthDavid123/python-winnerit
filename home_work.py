# mystring = input("press string: ")
# print(mystring[-1] + mystring[:-1])
# print(mystring[1::2])
### תרגיל מספר
# word = input("enter minimum 6: ")
# print(word[0:3].upper() + word[3:-3].lower() + word[-3:].upper())
# num = float(input("press number: "))
# print("" + str(num*2) + "\n" + str(num/2))
# #
# rochav = float(input("prees rochav: "))
# orech = float(input("prees orech: "))
# print(f"shetach: {rochav*orech}")
# print(f"hikef: {(rochav*2)+(orech*2)}")
# #
# height = float(input())
# width = float(input())
# #
# print((height * width), (2 * (width + height)))
# c = float(input())
# print((c-32)*5/9)
# #
# num = float(input())
# num *= 1.5
# print(num)
# #
# num = float(input())
# print(num % 2 == 0)
# #
# num = float(input())
# print((num > 5) and (num < 19))
# #
# n1 = float(input())
# n2 = float(input())
# print(abs(n1)+abs(n2))
# #
# n1 = int(input())
# print(n1//1000)
# #
# n1, n2 = map(int,input().split())
# print(n1)
# #
# n1 = int(input())
# print(n1 % 10)
# #
# string = input()
# print(string[:3])
# print(string[-1] + string[:-1])
# print(string[0::2])
# #
# string = input()
# if len(string) >= 6:
#     print(string[:3].upper() + string[3:-3].lower() + string[-3:].upper())
# #
# list = input()
# print(list[0])
# print(list[-1])
# m = len(list) // 2
# print(list[m])
# print(list[1::2])
# print(list[::2])
# print(list[::-1])
# #
list1 = input()
print(list1.lower())
print(list1.upper())
print(list1.capitalize())
print(list1.title())
words = list1.strip()
print(words)

