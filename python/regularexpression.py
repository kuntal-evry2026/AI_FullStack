import re ;

text = "Driver’s License Number: 123-456";
digit = re.findall(r"\d+",text);
print(digit)



updated_text = re.sub(r"\d","x",text);
print(updated_text)


def clean_text(text):
    text = re.sub(r"[^\w\s]","",text)
    text = "".join(text.split())
    return text

