

def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1 

def knuth_morris_pratt(pat, str):
    m = len(pat)
    n = len(str)
    lps = [0] * m
    j = 0
    compute_lps(pat, m, lps)
    i = 0
    while i < n:
        if pat[j] == str[i]:
            i += 1
            j += 1
        if j == m:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]
        elif i < n and pat[j] != str[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
def compute_lps(pat, m, lps):
    len = 0
    lps[0]
    i = 1
    while i < m:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    lcs = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    return lcs[m][n]

def bellman_ford(graph, src):
    dist = [float("Inf")] * len(graph)
    dist[src] = 0
    for _ in range(len(graph) - 1):
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return
    print(dist)
    