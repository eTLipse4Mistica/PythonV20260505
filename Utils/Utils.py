import pandas as pd
import streamlit as st
# import time
from .ConstantsVariablesDictionaries import *


# Cabalistic Map Reverse
CabalisticMapReverse = {character: key for key, values in CabalisticMap.items() 
           for character in values if character}


### Dataframe Creation ###

# Create a sample DataFrame
@st.cache_data
def ReturnDf(path: str, separator: str = ',', encoder: str = 'utf-8') -> pd.DataFrame:
    return pd.read_csv(
        filepath_or_buffer = path,
        sep = separator,
        encoding = encoder,
        # index_col = 0
    )


### Calcule Numerical Pyramid ###

# Name as Numerical Sequence
def ConvertsNameToInts(text):
    """
        Converts a string into a list of integers according to the Kabbalistic Map
        Removes whitespace before conversion
    """
    textWithoutSpaces = text.replace(" ", "")
    
    return [CabalisticMapReverse.get(character.lower(), 0) for character in textWithoutSpaces]

# Reduce for One Digit
def Reduce4OneDigit(number):
    """ Reduce the Number for One Digit."""
    if number < 10:
        return number
    return Reduce4OneDigit(sum(int(d) for d in str(number)))

# Generate Pyramid
def GeneratePyramid(nameInString):
    """
    Generate Pyramid.
    
    Args:
        string_numeros: String with the digits.
    
    Returns:
        List of list with each number sequence of digits.
    """
    actualList = [int(c) for c in nameInString]
    pyramid = [actualList.copy()]  # Save the first value
    
    for _ in range(len(nameInString)):
        if len(actualList) == 1:
            break
        
        # Create new list
        actualList = [Reduce4OneDigit(actualList[i] + actualList[i+1]) 
                       for i in range(len(actualList)-1)]
        
        # Save each new sequence
        pyramid.append(actualList.copy())
    
    return pyramid