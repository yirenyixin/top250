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
        if row[2] == "导演" or row[2] == "出演":
            nodes.append(row[1])
            green_nodes.append(row[1])
            type.append(1)
            edges.append((row[1], node, {'weight': 1}))
    elif row[1] == node:
        if row[2] == "导演" or row[2] == "出演":
            nodes.append(row[0])
            green_nodes.append(row[0])
            type.append(1)
            edges.append((row[0], node, {'weight': 1}))

def find(node):
    # 读取 CSV 文件
    # with open('E:\workspace\\top250\python\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
    with open('D:\workspace\\top\\top250\python\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            if row[0] == node or row[1] == node:
                add(row, node)
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
def getNameType(name):
    global type
    flag=1
    with open('D:\workspace\\top\\top250\python\\node.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            if row[1]==name:
                return row[2]
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


def show(name1, name2, nodes, edges, red_nodes, green_nodes, type):
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
def check(name1,name2):
    # 读取 CSV 文件
    # with open('E:\workspace\\top250\python\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
    with open('D:\workspace\\top\\top250\python\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过标题行
        name1_type=getNameType(name1)#输入第一个字符的类型
        name2_type=getNameType(name2)
        if name1_type=="电影名称" and name2_type=="电影名称":
            name1_list=[]#输入第一个字符的导演列表
            name2_list=[]
            for row in csv_reader:
                if row[1]==name1:
                    name1_list.append(row[0])
                elif row[1]==name2:
                    name2_list.append(row[0])
            print(name1_list)
            print(name2_list)
            if len(list(set(name2_list).intersection(set(name2_list))))>0:
                return "有相同导演"
            else:
                return "没关系"
        else:
            for row in csv_reader:
                if (row[0] == name1 and row[1] == name2) or (row[0] == name2 and row[1] == name1):
                    return row[2];
if __name__ == "__main__":
    # name1=input("请输入要查询的第一个信息：");
    # name2=input("请输入要查询的第二个信息：");
    name1="李力持"
    name2="周星驰"
    # name1="天书奇谭"
    # name2="哪吒闹海"
    flag=check(name1,name2)
    if flag=="属于" or flag=="合作" or flag=="出演" or flag=="导演" or flag=="有相同导演":
        print("有关系",flag)
        G = nx.DiGraph()
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        # 传递相应的参数, 将这些变量作为参数传递给函数，并避免在函数内部重新初始化
        show(name1, name2, nodes, edges, red_nodes, green_nodes, type)
        # 添加节点和边
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        # 创建一个节点颜色字典，将节点名称映射到颜色
        node_colors = {node: 'red' if node in red_nodes else 'green' for node in nodes}
        # 绘制图形时使用节点颜色属性
        nx.draw_networkx(G, node_color=[node_colors[node] for node in G.nodes])
        plt.show()
    else:
        print("没关系")