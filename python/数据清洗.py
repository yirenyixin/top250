import openpyxl
import split
import csv

# 打开 Excel 文件
wb = openpyxl.load_workbook('E:\workspace\\top250\python\\file\TOP250.xlsx')
sheet = wb.active


# 输出 A 列的值
# for row in sheet.iter_rows(min_col=1, max_col=1):
#     for cell in row:
#         print(cell.value)

# 定义要写入的数据
data = [
    ["ID","名称","标签"],
]
i=0
# 指定要创建的 CSV 文件的路径
csv_file_path = "example.csv"

# 使用 "w" 模式打开 CSV 文件，创建文件并写入数据
with open(csv_file_path, "w", newline="",encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in sheet.iter_rows(min_col=1, max_col=1):
        for cell in row:
            data.append([i,cell.value,"电影名称"])
            i+=1
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in data:
        csv_writer.writerow(row)

print(f"CSV 文件 {csv_file_path} 创建成功并写入数据。")