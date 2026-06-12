print("Wassup Buddy!! v10")
import os

print("PWD:", os.getcwd())
print("FILES:")
for f in os.listdir("."):
    print(f)
