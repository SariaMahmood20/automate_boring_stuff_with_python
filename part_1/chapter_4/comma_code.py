def commaFunction(spam):
    if not spam:
        return ""
    if len(spam) == 1:
        return spam[0]
    return ", ".join(spam[:-1])+" and "+spam[-1]

result = commaFunction(['apples', 'bananas', 'tofu', 'cats'])
print(result)
        
