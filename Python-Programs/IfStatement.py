ismale = False
istall = False
if ismale and istall:
    print("You are a tall male")
elif ismale and not(istall):
    print("You are a short male")
elif not(ismale) and istall:
    print("You are Not a Male But You are tall")
else:
    print("You Are not male and not tall")
