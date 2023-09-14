import csv
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
nodes = []
edges = []
type = []
# 创建两个节点颜色数组，一个存储红色节点，一个存储蓝色节点
red_nodes = []
green_nodes = []
i = 1

def add(row, node):
    global i
    if row[0] == node:
        nodes.append(row[1])
        if row[2] == "导演" or row[2] == "出演":
            green_nodes.append(row[1])
            type.append(1)
            edges.append((node, row[1], {'weight': 1}))
        else:
            red_nodes.append(row[1])
            type.append(0)
            edges.append((node, row[1], {'weight': 2}))
        print("a", row[0], row[1], row[2], i)
        i += 1
    elif row[1] == node:
        nodes.append(row[0])
        if row[2] == "导演" or row[2] == "出演":
            green_nodes.append(row[0])
            type.append(1)
            edges.append((node, row[0], {'weight': 1}))
        else:
            red_nodes.append(row[0])
            type.append(0)
            edges.append((node, row[0], {'weight': 2}))
        print("b", row[0], row[1], row[2], i)
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
def secondFind():
    with open('D:\workspace\\top\\top250\python\\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过标题行
        data = list(csv_reader)  # 读取 CSV 数据到列表

    for i in range(len(type)):
        if type[i] == 1 and i != 1:
            print("aaaaa", nodes[i])
            for row in data:
                if row[2] == "出演" and row[1] == nodes[i]:
                    nodes.append(row[0])
                    edges.append((nodes[i], row[0], {'weight': 1111}))
                    red_nodes.append(row[0])

if __name__ == "__main__":
    # node=input("请输入要查询的导演信息信息：");
    node = "周星驰"
    type.append(0)
    red_nodes.append(node)
    nodes.append(node)
    find(node)
    secondFind()

    print(nodes)
    print("edges",edges)
    print("red",red_nodes)
    G = nx.DiGraph()

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 添加节点和边
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # 计算最短路径
    path = nx.single_source_dijkstra_path(G, node)
    length = nx.single_source_dijkstra_path_length(G, node)

    # print("最短路径:")
    # print(path)
    # print("最短路径长度:")
    # print(length)
    # 创建一个节点颜色字典，将节点名称映射到颜色
    node_colors = {node: 'red' if node in red_nodes else 'green' for node in nodes}

    # 绘制图形时使用节点颜色属性
    nx.draw_networkx(G, node_color=[node_colors[node] for node in G.nodes])
    plt.show()

print("结束")
