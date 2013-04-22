def save_txt(filename, string):
    text_file = open(filename, "w")
    text_file.write(string)
    text_file.close()
    return "Done!"