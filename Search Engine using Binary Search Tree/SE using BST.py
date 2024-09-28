import os
import pickle
import time


class Node:
    def __init__(self, query, urls):
        self.key = query
        self.urls = urls
        self.left = None
        self.right = None


class binarySearchTree:
    def __init__(self):
        self.root = None

    def searchInBst(self, query):
        return self.search(self.root, query)

    def search(self, node, query):
        if node is None:
            return None
        if node.key == query:
            return node
        elif node.key > query:
            return self.search(node.left, query)
        else:
            return self.search(node.right, query)

    def buildTree(self, list_of_tuples):
        self.root = self.build(list_of_tuples, 0, (len(list_of_tuples) - 1))

    def build(self, list_of_tuples, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = Node(list_of_tuples[mid][0], list_of_tuples[mid][1])
        node.left = self.build(list_of_tuples, start, mid - 1)
        node.right = self.build(list_of_tuples, mid + 1, end)
        return node


def top10000(filename):
    with open(filename, 'r') as f:
        dic = {}
        line = f.readline().strip()
        while line:
            if line in dic:
                dic[line] += 1
            else:
                dic[line] = 1
            line = f.readline().strip()
        return dic


def top10000_urls(filename, dic_of_10000):
    with open(filename, 'r') as f:
        line = f.readline().strip()
        while line:
            words = line.split(':')
            if words[0] in dic_of_10000:
                dic_of_10000[words[0]] = words[1]
            elif not os.path.isfile(f'Files/{words[0]}.txt'):
                with open(f'Files/{words[0]}.txt', 'w') as file:
                    file.write(words[1])
            line = f.readline().strip()
        return dic_of_10000


def calculateLength(filename):
    with open(filename, 'r') as f:
        length = len(f.readlines())
    return length


def probabilityOfTop50Queries(t50, len):
    c = 1
    for (query, frequency) in t50:
        prob = round(frequency / len, 6)
        percent_prob = round(prob * 100, 6)
        print(f'{c}). The search probability of query {query} is {prob} ({percent_prob}%)')
        c += 1


def timeForQueries(arr1, arr2, bt):
    print('\t\t\t\t\t-----Queries From Memory------')
    c = 1
    for query in arr1:
        initTime = time.perf_counter_ns()
        ans = bt.searchInBst(query)
        endTime = time.perf_counter_ns()
        print(c, '). Query:', query)
        print('Output:', ans.urls.lstrip())
        print('URLs Read From: Memory')
        print(f'Time taken to serve the query is: {(endTime - initTime) / 10 ** 9} seconds')
        c += 1
    print('\t\t\t\t\t-----Queries From File------')
    c = 1
    for query in arr2:
        initTime = time.perf_counter_ns()
        with open(f'Files/{query}.txt', 'r') as f:
            ans = f.readline().strip()
        endTime = time.perf_counter_ns()
        print(c, '). Query:', query)
        print('Output:', ans)
        print('URLs Read From: File')
        print(f'Time taken to serve the query is: {(endTime - initTime) / 10 ** 9} seconds')
        c += 1


def saveInBF(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def readFrequencyFromBF(filename):
    if not os.path.isfile(filename):
        data = top10000('search-history.txt')
        saveInBF(filename, data)
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            return data
    else:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            return data


def readUrlsFromBF(filename, dic):
    if not os.path.isfile(filename):
        data = top10000_urls('search-results.txt', dic)
        saveInBF(filename, data)
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            return data
    else:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            return data


def main():
    dic = readFrequencyFromBF('frequency.bin')  # return dictionary of on basis of frequencies
    sorted_dic_10000 = sorted(dic.items(), key=lambda item: item[1], reverse=True)[:10000]  # sorted on basis of
    # frequencies and give list of Tuples
    dic_of_10000 = dict(sorted_dic_10000)  # dictionary  of top 10000 on basis of frequencies
    top_50 = sorted_dic_10000[:50]  # give top 50 most search queries
    dic_of_10000 = readUrlsFromBF('Urls.bin', dic_of_10000)  # return top 10000 queries with their urls
    top_10000 = sorted(dic_of_10000.items(), key=lambda item: item[0])  # sort data on basis of queries
    length = calculateLength('search-results.txt')

    print('----------------------------------Report 1---------------------------------------------')
    probabilityOfTop50Queries(top_50, length)

    bst = binarySearchTree()
    bst.buildTree(top_10000)

    print('----------------------------------Report 2---------------------------------------------')
    queriesFromMemory = ['fagot', 'zoopery', 'gewgaw', 'Zionism', 'Alma', 'Bobby', 'Acer', 'Alya', 'Batan', 'Baidya']
    queriesFromFiles = ['bakery', 'premake', 'mire', 'rechain', 'waver', 'Aaru', 'electro', 'inshoot', 'nife', 'volume']

    timeForQueries(queriesFromMemory, queriesFromFiles, bst)

    print('----------------------------------Main Program---------------------------------------------')

    while True:
        query = input('Please Enter the Search Query(or to stop enter -1): ')
        if query == '-1':
            break
        node = bst.searchInBst(query)
        if node:
            print('Output: ', node.urls.lstrip())
            print('URLs Read From: Memory')
        else:
            if os.path.isfile(f'Files/{query}.txt'):
                file = open(f'Files/{query}.txt', 'r')
                print('Output: ', file.readline().strip())
                print('URls Read From: File')
            else:
                print('Query Not Found')


main()
