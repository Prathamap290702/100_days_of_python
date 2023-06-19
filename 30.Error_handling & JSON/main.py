# #file not found
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     # print("There was an error")
#     file =  open("a_file.txt",  "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"{error_message} does not exist.")
# else: #if everything succeeds then this keyword is exceuted
#     content = file.read()
#     print(content)
# finally:#it will excecute no matter what happens
    # file.close()
    # print("file was closed.")
    # raise TypeError("this is the error that i created")
 # we can raise our own exceptions by using raise keyword

 #example in bmi calculator height of a human cannot be more than 3 meters
 # so we can raise an error that the height should be less than 3 meters
 # raise ValueError("Human height cannot exceed 3 meters")