import pathlib

def separate_text(text, chunk_size=4096):
    """
    Separate text into chunks of given chunk size.
    """
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

filename = str(pathlib.Path(__file__).parent.resolve()) +'\\3.txt'

with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    chunks = separate_text(text)
    chunk_index = 0
    
    while chunk_index < len(chunks):
        input("Press Enter to copy the next chunk to the clipboard...")
        # pyperclip.copy(chunks[chunk_index]) # Uncomment this line if you want to copy the chunk to the clipboard, you will need to install pyperclip and export it
        print(chunks[chunk_index])
        chunk_index += 1
