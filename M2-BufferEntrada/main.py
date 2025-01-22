# Base code to start

def load_buffer(input_data, start, buffer_size):
    buffer = input_data[start:start + buffer_size]
    return buffer

def process_string(string, size):
    start = 0
    lexeme = ""

    while start < len(string):
        buffer = load_buffer(string, start, size)

        for symbol in buffer:
            print(f"buffer: {start} {symbol}")
            if symbol == " ":
                print(f"Lexeme processed: {lexeme}")
                lexeme = ""
            else: 
                lexeme += symbol
                
        start += size
    print(f"Lexeme processed: {lexeme}")


input_data = "This is an example"
start = 0
buffer_size = 10
process_string(input_data, buffer_size)
