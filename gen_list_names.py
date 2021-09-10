import pandas as pd

if __name__ == '__main__':
    save_to_csv = False
    my_range = 31
    my_old_str = "stims/sub"
    my_suffix = ".png"

    my_str_list = [my_old_str+str(i)+my_suffix for i in range(1, my_range)]

    df = pd.DataFrame(my_str_list)

    if save_to_csv:
        df.to_csv("new_strs.csv")