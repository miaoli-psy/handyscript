import pandas as pd


def process_col(input_df: pd.DataFrame, col_name: str, func_name):
    if col_name in input_df.columns:
        input_df[col_name] = input_df[col_name].map(func_name)
    else:
        raise Exception(f"Warning: missing {col_name}")


def insert_new_col(input_df: pd.DataFrame, old_col: str, new_col: str, func_name):
    if old_col in input_df.columns:
        col_index = input_df.columns.get_loc(old_col)
        input_df.insert(col_index, new_col, input_df[old_col].map(func_name))
    else:
        raise Exception(f"Warning: missing {old_col}")
        

def insert_new_col_from_two_cols(input_df: pd.DataFrame, old_col1: str, old_col2: str, new_col: str, func_name):
    cols = input_df.columns
    if (old_col1 in cols) and (old_col2 in cols):
        input_df[new_col] = input_df.apply(lambda x: func_name(x[old_col1], x[old_col2]), axis = 1)
    else:
        raise Exception(f"Warning: missing {old_col1} or {old_col2}")


def x_coor_to_lst(input_x_coor: float) -> list:
    return list([input_x_coor, 0])


def transform_size(size_in_deg, to_pix_index):
    return [round(size_in_deg * to_pix_index, 2), round(size_in_deg * to_pix_index,2 )]


def get_letter_name(identity, size):
    return "stims/" + str(identity) + str(size) + ".png"

if __name__ == '__main__':
    save_to_excel = True
    filename = "files/condition.xlsx"
    df = pd.read_excel(filename)
    to_process = ["pos1", "pos2", "pos3", "pos4", "pos5", "pos6"]
    size = ["size"]
    # to_process = ["pos1", "pos2"]
    for pos in to_process:
        process_col(input_df = df, col_name = pos, func_name = x_coor_to_lst)
    
    letter_names = ["letter1", "letter2", "letter3", "letter4", "letter5", "letter6"]
    
    for letter_name in letter_names:
        insert_new_col_from_two_cols(df, "identity", "size_w", letter_name, get_letter_name)
        
    insert_new_col_from_two_cols(df, old_col1 = "size_w", old_col2 = "to_pix_index", new_col = "size_in_pix", func_name = transform_size)

    if save_to_excel:
        df.to_excel("processed_condition.xlsx", index = False)
    
        


