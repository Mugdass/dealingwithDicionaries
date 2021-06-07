print("Give me three names! I forgot what they were")
a1=input()
a2=input()
a3=input()

print("That's right!I remember now.")

print("This is what I heard that...")
name=(a1,a2,a3)



family = [(a1, ["The Lord of The Rings", "Prison Break"]),
            (a2, ["Deep Blue Sea", "The Day after Tomorrow", "Harry Potter"]),
            (a3, ["Prison Break", "3 Idiots", "Shooter"])]
for (name, movies) in family:
    print(name, "likes watching these", len(movies),"\n", "movies:","\n",movies,"\n")
    
print("Maybe I'm right or maybe I'm wrong")
print()
print("Atleast that's what I heard...")
print()
print("Goodnight!")






          
          

