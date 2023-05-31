import xlrd
import json

## 读取xls文件，生成json文件

# 读取xls文件
def read_xls(file_path):
    # 打开文件
    workbook = xlrd.open_workbook(file_path)
    # 获取所有sheet
    print(workbook.sheet_names()) # [u'sheet1', u'sheet2']

    sheet1_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
    # 读取一行数据
    print(sheet1.row_values(0)) # 获取第一行内容

    #遍历 sheet
    for i in range(workbook.sheet_names().__len__()):
        json_data = {}
        sheet = workbook.sheet_by_index(i)
        #json_data 是否有key
        sheet_name = workbook.sheet_names()[i]
        if not sheet_name in json_data.keys():
            json_data[sheet_name] = []

        print(sheet.name)
        print(sheet.nrows)
        print(sheet.ncols)
        for i in range(sheet.nrows):
            r = sheet.row_values(i) 
            json_data[sheet_name].append({'title':r[0],'desc':r[1],"imageUrl":""})
        save_json('{0}.json'.format(sheet_name),json_data[sheet_name])

# 生成json文件
def save_json(file_path, json_data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
if __name__ == '__main__':
    read_xls('booklist.xls')