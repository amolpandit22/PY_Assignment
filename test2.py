import re
import inflection


testStrings = ['isValidNumber','isFMNOCurrent','newRecordID']


def convertUsingRegularExpression(text):
    subString = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', text)   
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', subString).lower()

def convertUsingInflection(text):
    subString = inflection.underscore(text)
    subString = subString.replace("_", " ")
    return subString.lower()


for test_string in testStrings:
    print("Using Regular Expressions : " + convertUsingRegularExpression(test_string))

for test_string in testStrings:
    print("Using inflection module : "  + convertUsingInflection(test_string))