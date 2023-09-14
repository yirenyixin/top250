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
def add(row, node):
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
def getType(name):
    global type
    flag=1
    with open('D:\workspace\\top\\top250\python\\node.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            if row[1]==name and (row[2]=="演员" or row[2]=="导演"):
                type.append(1)
                flag=0
    if not flag==1:
         type.append(0)
def remove_duplicates(lst):
    seen = set()
    result = []
    for edge in lst:
        # 提取边的信息并转换为元组
        edge_info = (edge[0], edge[1], edge[2]['weight'])
        if edge_info not in seen:
            seen.add(edge_info)
            result.append(edge)
    return result


def show(name1,name2):
    global nodes,edges,red_nodes,green_nodes,type
    getType(name1)
    # type.append(0)
    red_nodes.append(name1)
    nodes.append(name1)
    find(name1)
    getType(name2)
    # type.append(0)
    red_nodes.append(name2)
    nodes.append(name2)
    find(name2)
    nodes=list(set(nodes))
    # 不可哈希元素的列表进行去重
    edges = remove_duplicates(edges)

    # 创建一个字典，用于根据节点去重
    unique_nodes_dict = {}
    # 用于存储新的去重后的类型列表
    unique_types = []
    for node, node_type in zip(nodes, type):
        if node not in unique_nodes_dict:
            unique_nodes_dict[node] = True  # 使用字典来记录节点
            unique_types.append(node_type)  # 将相应位置的类型添加到新的列表中
    # 转换为列表形式
    unique_nodes = list(unique_nodes_dict.keys())
    nodes=unique_nodes
    type=unique_types
    secondFind()
    # print(len(node),len(type))
    # print(nodes)
    # print("edges",edges)
    # print("red",red_nodes)
    G = nx.DiGraph()

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 添加节点和边
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # 创建一个节点颜色字典，将节点名称映射到颜色
    node_colors = {node: 'red' if node in red_nodes else 'green' for node in nodes}

    # 绘制图形时使用节点颜色属性
    nx.draw_networkx(G, node_color=[node_colors[node] for node in G.nodes])
    plt.show()
    print(nodes)
    print(edges)
    # # 计算从name1到name2的最短路径
    # shortest_path = nx.shortest_path(G, source=name1, target=name2)
    # print("最短路径:", shortest_path)
    #
    # # 创建一个新的图形，仅包含最短路径上的节点和边
    # shortest_path_graph = G.subgraph(shortest_path)
    #
    # # 绘制最短路径
    # pos = nx.spring_layout(shortest_path_graph)  # 指定节点的布局
    #
    # # 显示节点的索引作为标签
    # labels = {node: str(node) for node in shortest_path_graph.nodes}
    #
    # node_colors = [node_colors[node] for node in shortest_path_graph.nodes]
    # nx.draw_networkx_nodes(shortest_path_graph, pos, node_color=node_colors)
    # nx.draw_networkx_edges(shortest_path_graph, pos, edgelist=shortest_path_graph.edges, edge_color="blue", width=2)
    # nx.draw_networkx_labels(shortest_path_graph, pos, labels, font_size=10, font_color="black")
    #
    # # 显示最短路径图形在新的画布上
    # plt.show()
def check(name1,name2):
    # 读取 CSV 文件
    # with open('E:\workspace\\top250\python\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
    with open('D:\workspace\\top\\top250\python\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            if (row[0] == name1 and row[1] == name2) or (row[0] == name2 and row[1] == name1):
                return row[2];
if __name__ == "__main__":
    # name1=input("请输入要查询的第一个信息：");
    # name2=input("请输入要查询的第二个信息：");
    name1="李力持"
    name2="周星驰"
    flag=check(name1,name2)
    if flag=="属于" or flag=="合作" or flag=="出演":
        print("有关系",flag)
        show(name1,name2)
    else:
        print("没关系")