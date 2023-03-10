friends = ["Biswa", "Kuni", "Papuna", "jim", "Papuna"]
friends[1] = "Pupu"
print(friends[1])
num = [2, 8, 9, 80, 87, 99]
#friends.extend(num)
print(friends)
friends.append("Kuni")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Kelly")
print(friends)
print(friends.index("Pupu"))
print(friends.count("Papuna"))
friends.sort()
friends.reverse()
print(friends)
friends2 = friends.copy()
print(friends2)