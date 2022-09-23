
def read_text(filename: str) -> str:
    """
        This function reads a file given a file path and converts contents into a string. 
    """
    with  open(filename,'r',encoding='utf-8',newline='\n') as file:
        
        file_string = file.read()

        return file_string







