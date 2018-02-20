# # 10-1
# print("========== 10 - 1 ==========")
# filename = 'learning_python.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rstrip())
#
# # 10-2
# print("========== 10 - 2 ==========")
# for line in lines:
#     print(line.rstrip().replace('python', 'java'))
#
# # 10-3
# print("========== 10 - 3 ==========")
# filename3 = 'guest.txt'
#
# with open(filename3, 'w') as file_object:
#     name = input("what's your name: ")
#     file_object.write(name)
#
# # 10-4
# print("========== 10 - 4 ==========")
# filename4 = 'guest_book.txt'
#
# with open(filename4, 'a') as file_object:
#     while True:
#         name = input("Please enter your name: ('quit' to quit)")
#         if name == 'quit':
#             break
#         else:
#             print("Welcome, " + name + "!")
#             file_object.write(name + "\n")
#
# # 10-5
# print("========== 10 - 5 ==========")
# filename5 = 'programming_poll_result.txt'
#
# with open(filename5, 'a') as file_object:
#     while True:
#         name = input("Why do you like programming? type 'quit' to quit.")
#         if name == 'quit':
#             break
#         else:
#             file_object.write(name + "\n")

# # 10-6
# print("========== 10 - 6 ==========")
# print("Give me two numbers, and I'll add them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         first = int(first_number)
#         second = int(second_number)
#     except ValueError:
#         print("You need to input an integer.")
#     else:
#         print(first + second)

# # 10-7
# print("========== 10 - 7 ==========")
# print("Give me numbers, and I'll add them.")
# print("Enter 'q' to quit.")
# sum = 0
# while True:
#     first_number = input("\nnumber: ")
#     if first_number == 'q':
#         break
#     try:
#         first = int(first_number)
#     except ValueError:
#         pass
#     else:
#         sum += first
#         print(sum)

# # 10-8
# print("========== 10 - 8 ==========")
#
#
# def read_files(filename):
#     try:
#         with open(filename) as f_object:
#             contents = f_object.read()
#     except FileNotFoundError:
#         msg = "Sorry, the file " + filename + " is not found."
#         print(msg)
#     else:
#         print(contents)
#
#
# filenames = ['cats.txt', 'dogs.txt']
# for filename in filenames:
#     read_files(filename)

# # 10-9
# print("========== 10 - 9 ==========")
#
#
# def read_files(filename):
#     try:
#         with open(filename) as f_object:
#             contents = f_object.read()
#     except FileNotFoundError:
#         pass
#     else:
#         print(contents)
#
#
# filenames = ['cats.txt', 'dogs.txt']
# for filename in filenames:
#     read_files(filename)

# 10-10
print("========== 10 - 10 ==========")
with open('gutenberg.txt') as f_obj:
    contents = f_obj.read().lower()
    cnt = contents.count('the')
    print("word count for 'the' is " + str(cnt))
