# WORD SOUP! AHAHAHAEHAAAEHA
import pandas as pd
import random 


def txt_read(txt):
    df = pd.read_csv(txt, sep=" ")
    df = df.dropna()
    str_out = str(df.astype(str)).split()
    return str_out


def wordsoup(txt):
    str_out = txt_read(txt)
    random.shuffle(str_out)
    return " ".join(str_out)


