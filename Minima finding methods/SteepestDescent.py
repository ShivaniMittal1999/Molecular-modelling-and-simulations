#Minima finding by steepest descent
while True:
    try:
        x1 = float(input("Enter the possible value of x: "))
        step = float(input("Enter the step size: "))
        break
    except ValueError:
        print ("Invalid type of input")
count = 0
while True:
    count += 1
    print ("Iteration:",count)
    S_x1 = 4 - (2*x1)
    if round(S_x1,5) != 0:
        x2 = x1 + (step*S_x1)
        print (f"x1 = {x1}\tstep = {step}\tNegative derivative = {S_x1}\tx2 = {x2}")
        x1 = x2
    else:
        print (f"{'-'*50}")
        print (x1,"is the point at which the value of function is minimum")
        print ("Number of iterations took to reach minima:",count)
        break
        

