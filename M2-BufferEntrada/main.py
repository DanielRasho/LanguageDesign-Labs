# Base code to start

# Returns a buffer of fixed size from a string
def load_buffer(input_data, start, buffer_size):
    buffer = input_data[start:start + buffer_size]
    return buffer

# Processes a string using buffers
def process_string(string, size):
    start = 0
    lexeme = ""
    buffer = load_buffer(string, start, size)

    while True:

        for symbol in buffer:
            print(f"buffer: {start} {symbol}")
            if symbol == " ":
                print(f"Lexeme processed: {lexeme}")
                lexeme = ""
            else: 
                lexeme += symbol

        if len(buffer) < size:
            print(f"Lexeme processed: {lexeme}")
            break

        buffer = load_buffer(string, start, size)

        start += size


input_data = "Esto es un ejemplo eof"
start = 0
buffer_size = 10
process_string(input_data, buffer_size)
