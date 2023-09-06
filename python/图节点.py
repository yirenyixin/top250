import csv
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 创建一个有向图
G = nx.DiGraph()

i = 1

def add(row, node):
    global i
    if row[0] == node:
        G.add_node(row[1])
        G.add_edge(node, row[1])
        print("a",i)
        i += 1
    elif row[1] == node:
        G.add_node(row[0])
        G.add_edge(node, row[0])
        print("b",i)
        i += 1

def find(node):
    # 读取 CSV 文件
    # with open('E:\workspace\\top250\python\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
    with open('D:\workspace\\top\\top250\python\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            if row[0] == node or row[1] == node:
                add(row, node)

if __name__ == "__main__":
    node = "周星驰"
    G.add_node(node)
    find(node)

# 设置全局字体参数
font_path = fm.findSystemFonts()  # 获取系统中可用字体文件路径
font_name = fm.FontProperties(fname=font_path[0]).get_name()  # 获取第一个可用字体的名称
plt.rcParams["font.family"] = font_name  # 设置全局字体为系统中第一个可用字体

# 可视化有向图
pos = nx.spring_layout(G)  # 定义节点的布局

# 可视化有向边，并使用中文字符
nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue",
        font_size=12, font_color="black", font_weight="bold",
        connectionstyle="arc3, rad=0.2", labels={node: node})

plt.show()
print("结束")
