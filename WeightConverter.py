weight = float(input("Weight: "));
metric = input("K(g) or (L)bs: ");
relation = float(2.20462262);

if metric.lower() == "k":
    print("Result: " + str(weight * relation) + " lbs");
elif metric.lower() == "l":
    print("Result: " + str(weight / relation) + " kg");
else:
    print("Not possible to convert!");