class Operations_with_css():
    def __init__(self, lat_gusev, long_gusev, lat_harlamov, long_harlamov, lat_bluetrans, long_bluetrans, lat_petrov, long_petrov, lat_ragulin, long_ragulin, css_lines):
        super().__init__()
        self.lat_gusev = lat_gusev
        self.long_gusev = long_gusev
        self.lat_harlamov = lat_harlamov
        self.long_harlamov = long_harlamov
        self.lat_bluetrans = lat_bluetrans
        self.long_bluetrans = long_bluetrans
        self.lat_petrov = lat_petrov
        self.long_petrov = long_petrov
        self.lat_ragulin = lat_ragulin
        self.long_ragulin = long_ragulin
        self.css_lines = css_lines





    def updating_css_file_with_new_coordinates(self):
        text= ['.Гусев {\n', 'color: red;\n', '  position:absolute;\n', f'  top: {self.lat_gusev}px; /*[wherever you want it]*/\n', f'  left:{self.long_gusev}px; /*[wherever you want it]*/\n', '}\n', '\n', '.Харламов {\n', 'color: red;\n', '  position:absolute;\n', f'  top: {self.lat_harlamov}px; /*[wherever you want it]*/\n', f'  left:{self.long_harlamov}px; /*[wherever you want it]*/\n', '}\n', '.Петров {\n', 'color: red;\n', '  position:absolute;\n', f'  top: {self.lat_petrov}px; /*[wherever you want it]*/\n', f'  left:{self.long_petrov}px; /*[wherever you want it]*/\n', '}\n', '.Рагулин {\n', 'color: red;\n', '  position:absolute;\n', f'  top: {self.lat_ragulin}px; /*[wherever you want it]*/\n', f'  left:{self.long_ragulin}px; /*[wherever you want it]*/\n', '}\n', '.Блютранс {\n', 'color: red;\n', '  position:absolute;\n', f'  top: {self.lat_bluetrans}px; /*[wherever you want it]*/\n', f'  left:{self.long_bluetrans}px; /*[wherever you want it]*/', '\n}\n']
        with open("styles.css") as initial_text:
            css_text = initial_text.readlines()
        for i in range(1, 32):
            css_text.pop(0)
        new_text = "".join(text + css_text)

        with open("styles.css", "w") as file:
            file.write(new_text)




