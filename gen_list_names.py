import pandas as pd

if __name__ == '__main__':
    save_to_csv = True
    start_range = 10
    end_range = 18
    my_old_str = "stims/whitesub"
    my_suffix = ".png"

    my_str_list = [my_old_str+str(i)+my_suffix for i in range(start_range, end_range + 1)]

    df = pd.DataFrame(my_str_list)

    if save_to_csv:
        df.to_csv("new_strs.csv")