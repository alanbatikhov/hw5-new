# list = [ 1, 2, 3, 4, 5]
# maximum = max(list)
# minimum = min(list)
# print(minimum, maximum)

"""task1"""
def minimum(list):
    min_val = None
    for val in list:
        if min_val == None or min_val > val:
            min_val = val
    return min_val
def maximum(list):
    max_val = None
    for val in list:
        if max_val == None or max_val<val:
            max_val = val
    return max_val
def main():
    list = [1,2,3,4,5,6,7]
    print("Наименьшее значение это ", minimum(list))
    print("Наибольшее значение это ", maximum(list))
main()


"""task2"""
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        most_words_found: int = 0
        for sentence in sentences:
            list_of_words: list[str] = sentence.split(" ")
            num_of_words: int = len(list_of_words)
            most_words_found = max(most_words_found, num_of_words)
        return most_words_found

s = Solution()
rs = s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
print(rs)



# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# sent_len = []
# for s in sentences:
#     li_len = len(s.split(' '))
#     sent_len.append(li_len)
# sent_len
