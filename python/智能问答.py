import networkx as nx
import csv
import re
# 构建电影关系图
G = nx.Graph()
nodes = set()  # 使用集合来跟踪已添加的节点
edges = set()  # 使用集合来跟踪已添加的边
def get_weight(relation_type):
    # 根据关系类型返回相应的权重
    if relation_type == '属于':
        return 1
    elif relation_type == '出演':
        return 2
    elif relation_type == '导演':
        return 3
    elif relation_type == '合作':
        return 4
def get_type(relation_weight):
    # 将关系权重字符串转换为整数
    relation_weight = int(relation_weight)
    # 根据关系权重返回相应的类型
    if relation_weight == 1:
        return '属于'
    elif relation_weight == 2:
        return '出演'
    elif relation_weight == 3:
        return '导演'
    elif relation_weight == 4:
        return '合作'

def creat_graph():
    with open('D:\workspace\\top\\top250\python\\movie_relation.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            node1 = row[0]
            node2 = row[1]
            relation_type = row[2]
            # 检查并添加节点
            nodes.add(node1)
            nodes.add(node2)
            # 构建边的唯一标识
            edge_identifier = (node1, node2, relation_type)
            # 检查并添加边
            if edge_identifier not in edges:
                G.add_edge(node1, node2, weight=get_weight(relation_type))  # 添加边到图中
                edges.add(edge_identifier)  # 将边标识添加到已添加边的集合中


def answer_question(question):
    # 使用正则表达式提取问题中的电影名称和问题类型
    match = re.search(r'(.+)的(.+)是谁', question)
    match_relation = re.search(r'(.+)和(.+)是什么关系', question)
    if match:
        movie_name = match.group(1)
        question_type = match.group(2)
        if G.has_node(movie_name):
            # 使用 NetworkX 查找与电影相关的导演节点
            directors = [node for node in G.neighbors(movie_name) if G.edges[movie_name, node]['weight'] == 3]

            if directors:
                if question_type == '导演':
                    return f"{movie_name}的{question_type}是{', '.join(directors)}"
                else:
                    return f"抱歉，我不知道{movie_name}的{question_type}是什么。"
            else:
                return f"抱歉，我不知道{movie_name}的导演是谁。"
        else:
            return f"抱歉，我不知道{movie_name}这部电影。"
    elif match_relation:
        entity1 = match_relation.group(1)
        entity2 = match_relation.group(2)
        # 使用 NetworkX 检查两个实体之间的关系
        if G.has_edge(entity1, entity2):
            relation_weight = str(G[entity1][entity2]['weight'])
            return f"{entity1}和{entity2}是{get_type(relation_weight)}关系"
        elif G.has_edge(entity2, entity1):
            relation_weight = str(G[entity2][entity1]['weight'])
            return f"{entity2}和{entity1}是{get_type(relation_weight)}关系"
        else:
            return f"抱歉，我不知道{entity1}和{entity2}之间的关系。"
    else:
        return "抱歉，我无法理解你的问题。"

if __name__ == "__main__":
    #创建图
    creat_graph()
    # # 输出已添加的节点和边
    # print("Nodes:", nodes)
    # print("Edges:", edges)
    # 与用户交互
    while True:
        user_input = input("你的问题（输入退出结束对话）: ")
        if user_input.lower() == '退出':
            print("智能问答系统已退出。")
            break
        answer = answer_question(user_input)
        print("智能问答系统:", answer)
