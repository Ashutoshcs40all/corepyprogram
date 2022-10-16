# The FORMAT() method formats the specified values(s) and insert them inside the string's placeholder.
#The palceholder is defined using curly brackets:{}.
#^ centre
#> right
#< left
w="Welcome To {} {} Lucknow".format("ASHUTOSH", "In");
print(w)

w1="Welcome To {1} {0} Lucknow".format("ASHUTOSH", "In");
print(w1)

w2="Welcome To {a:^15} {b} Lucknow".format(a="ASHUTOSH", b="In");
print(w2)
