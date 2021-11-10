print("This program is to know more about the person")

person = {"first_name": "WeiQuan", "last_name": "Liow", "age": 33, "country_of_birth": "Singapore", "Phone": 93029029}

info = input("What do you want to know about the person? ").lower()


result = person.get(info, "We do not have this information")

print(result)
