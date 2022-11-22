
import json


def split_address(address):
    
    # define an empty dictionary for output
    converted_address = {}


    ## delete comma and create tokens from address
    address_tokens = address.replace(",","").split()


    ##find the indexes of tokens containing numbers and put them in a list named indexes
    indexes = []
    for token in address_tokens:
        if any(char.isdigit() for char in token):
            indexes.append(address_tokens.index(token))

            
    ## if the first token is a number, we can think of it as a housenumber and the rest of it as the street name
    if indexes[0] == 0 :
        converted_address["street"] = (" ".join(address_tokens[1:]))
        converted_address["housenumber"] = address_tokens[0]


    ##if the first token is not a number, and all address contains only 1 token with the number >>
    # we can extract after the number as a house number, the rest of it as the street name
    elif indexes[0] != 0  and len(indexes) == 1:
        converted_address["street"] =   (" ".join(address_tokens[0:indexes[0]]))   
        converted_address["housenumber"] = (" ".join(address_tokens[indexes[0]:]))


    ## if address contains more than 1 token with number, we can extract street name until the token which contains first number, rest of it as housenumber
    ## and if contains "no" or "No" wording we can easily use it to extract 
    contains_no_wording = False

    for token in address_tokens:
        if any("no" in char.lower() for char in token):
            contains_no_wording = True
            index_no = address_tokens.index(token)
    if len(indexes) > 1:
        if contains_no_wording :
            print("contains no")
            converted_address["street"] =   (" ".join(address_tokens[index_no:index_no+2]))   
            converted_address["housenumber"] = (" ".join(address_tokens[index_no+1:]))
        else:
            converted_address["street"] = (" ".join(address_tokens[0:indexes[0]+1]))
            converted_address["housenumber"] = (" ".join(address_tokens[indexes[0]+1:]))
      
    
    return json.dumps(converted_address,ensure_ascii=False)


## Let's use test cases and try them with the function defined above
print(split_address("Winterallee 3"))
print(split_address("Musterstrasse 45"))
print(split_address("Blaufeldweg 123B"))
print("----------------------------------------------------------")
print(split_address("Am Bächle 23"))
print(split_address("Auf der Vogelwiese 23 b"))
print("----------------------------------------------------------")
print(split_address("4, rue de la revolution"))
print(split_address("200 Broadway Av"))
print(split_address("Calle Aduana, 29"))
print(split_address("Calle 39 No 1540"))
