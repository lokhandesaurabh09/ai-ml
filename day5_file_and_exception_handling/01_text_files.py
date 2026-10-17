with open("notes.txt", "w") as f:
    f.write("Python is fun\n")
    f.write("Files store data\n")
    f.write("Logging helps debugging\n")

with open("notes.txt" , "r") as f:
    print(f.read())

#----------------------------------------------

with open("notes.txt" , "r") as f:
    text = f.read()

lines = len(text.splitlines())
words = len(text.split())
chars = len(text)
print(f"Lines: {lines}, Words: {words}, Characters: {chars}")