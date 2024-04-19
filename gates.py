# Parsing objects go here

def read(arg):
    return arg

KEYWORDS = {
    "REQUEST_INPUT": input,  # Mapping the keyword to the input function directly
    "READ": read,
}



class JSON_GATE:
    def __init__(self, command):
        self.command = command

    def parse_and_execute(self):
        if ": " in self.command:  # Ensure the command format is correct
            keyword, argument = self.command.split(": ", 1)
            func = KEYWORDS.get(keyword)
            if func:
                return func(argument)  # Execute the function associated with the keyword
        raise ValueError("NOT A VALID REQUEST")