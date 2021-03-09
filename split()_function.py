#split() function is used for split the string with a certain character
#First let's define a string variable

website  = 'www.elifakkaya.com'

#if we want to separate www, elifakkaya and com, we can use split() function
#as it's seen, between all of these, there are . characters
#so, we split the string according to that . character

print(website.split('.'))

# we can use this function for any other character even with space

information = 'Elif Akkaya Python'
print(information.split(' '))