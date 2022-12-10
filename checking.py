with open("styles.css") as initial_text:
    css_text = initial_text.readlines()
print(len(css_text))
for i in range(1, 33):
    css_text.pop(0)
print(css_text)
