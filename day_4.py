from utils.utils import read_input, read_input_raw
import pandas as pd 

data = read_input("day_4_data.txt")
# data = read_input("day_4_example.txt")

df = pd.DataFrame([list(s) for s in data])
num_columns = len(df.columns) - 1
num_rows = len(df) - 1

x_indices = [(row_index, col_index) for row_index, row in df.iterrows() 
           for col_index, value in row.items() if value == 'X']

def check_surrounding(indicies, character):
    row_index = indicies[0]
    col_index = indicies[1]
    
    directions = {
        "north": (row_index - 1, col_index),
        "north_east": (row_index - 1, col_index + 1),
        "east": (row_index, col_index + 1),
        "south_east": (row_index + 1, col_index + 1),
        "south": (row_index + 1, col_index),
        "south_west": (row_index + 1, col_index - 1),
        "west": (row_index, col_index - 1),
        "north_west": (row_index - 1, col_index - 1)
    }

    valid_matches = []
    for direction, (r, c) in directions.items():
        if 0 <= r <= num_rows and 0 <= c <= num_columns:
            if df.iloc[r, c] == character:
                valid_matches.append({"direction": direction, "index": (r, c)})

    return valid_matches
    

m_indexs = []
a_indexs = []
s_indexs = []
index_lst = []

xmas_count = 0

for x_index in x_indices:
    m_matches = check_surrounding(x_index, "M")
    for m_match in m_matches:
        m_direction = m_match["direction"]
        m_index = m_match["index"]
        
        # Check for 'A' in the same direction
        a_matches = check_surrounding(m_index, "A")
        for a_match in a_matches:
            if a_match["direction"] == m_direction:
                a_index = a_match["index"]
                
                # Check for 'S' in the same direction
                s_matches = check_surrounding(a_index, "S")
                for s_match in s_matches:
                    if s_match["direction"] == m_direction:
                        xmas_count += 1
                        xmas = {"x": x_index, "m": m_index, "a": "a_index", "s": s_match["index"]}
                        index_lst.append(xmas)

print(f"Total occurrences of 'XMAS': {xmas_count}")
