songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[-1])
print(songs[1:])

songs[-1] = "Work work work"

songs.extend(["The Art of Zen", "Antigravity", "Neptune"])

del songs[2]

animals = ["Penguin", "Turtle", "Dog"]
animals.append("Cat")
print(animals[2])
del animals[0]

for animal in animals:
  print(animal)