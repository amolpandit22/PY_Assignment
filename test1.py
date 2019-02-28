import re
import inflection


request = input("Please enter text : ")

def convertUsingRegularExpression(text):
    subString = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', text)   
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', subString).lower()

output1 = convertUsingRegularExpression(request)

def convertUsingInflection(text):
    subString = inflection.underscore(text)
    subString = subString.replace("_", " ")
    return subString.lower()

output2= convertUsingInflection(request)

print("Using Regular Expressions : " + output1)
print("Using inflection module : "  + output2)

