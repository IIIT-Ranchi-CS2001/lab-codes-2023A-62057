print("Enter the coordinate of both point : ")
user_input = [int(input(f"{i+1}: "))for i in range(4)]
m=(user_input[0]-user_input[2])/(user_input[1]-user_input[3])

print(f"X- {user_input[0]} = {m}(Y-{user_input[1]})")