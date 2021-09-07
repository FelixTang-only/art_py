import pandas as pd

# 国际化导出
excel_index = 3 # 要替换的excel对应的列索引
excel_path = '/Users/apple/Work/art_py/Book1.xlsx' # 要替换的excel对应的列索引
miss_out_file_path = '/Users/apple/Work/art_py/miss_out.js'
# to_file_path = '/Users/apple/Work/art_py/en.js'
to_file_path = '/Users/apple/Work/art_py/zh-TW.js'
from_file_path = '/Users/apple/Work/art_py/zh-CN.js'



def translate():
    a = pd.read_excel(excel_path, header=0, names=None, keep_default_na=False)
    a_li = a.values.tolist()

    sp_str = "\'"
    # f_new = open('/Users/apple/Downloads/zh-TW.js', 'w+', encoding='utf-8')
    f_new = open(to_file_path, 'w+', encoding='utf-8')
    miss_out = open(miss_out_file_path, 'w+', encoding='utf-8')
    with open(from_file_path, 'r', encoding='utf8') as f:
        for inl, line in enumerate(f):
            if sp_str in line and "'" in line:
                temp = line
                tempTwo = line.split(sp_str)[1]
                
                for inx, x in enumerate(a_li):
                    if x[1] != '' and x[1] == tempTwo:
                        temp = temp.replace(x[1], x[excel_index])
                        print(temp)
                        f_new.write(temp)
                        break
                    if inx == len(a_li) - 1:
                        f_new.write(temp)
                        miss_out.write(temp)
                # f_new.write(tempOne + ': ' + (' ').join(tempTwo))
            else:
                f_new.write(line)


translate()
