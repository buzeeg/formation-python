# with "toto" as s:
#     print(s)

# Old school method, but ressource not cleaned up if an exception is raised
f = open("toto.txt", "w")
print("Hello", file=f)
f.close()

# The good answer, possible when __enter__ and __exit__ methods are implemented
with open("toto.txt", "a") as fl:
    print("Hello with", file=fl)
