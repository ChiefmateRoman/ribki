
class Getting_css_text:
    def __init__(self):
        super().__init__()

    def getting_lines(self):
        with open("styles.css") as file_css:
            text = file_css.readlines()
        return(text)