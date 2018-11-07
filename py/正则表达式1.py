import re
text = "Hi, I am Shirley Hilton. I am his wife."
m = re.findall(r"hi", text)
if m:
    print(m)
else:
    print("mot match")

