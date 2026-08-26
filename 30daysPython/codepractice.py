# def solution(s):
#
#
#     mylist = []
#     if len(s) % 2 != 0:
#         s = s + '_'
#     for i in range(0, len(s), 2):
#         pair = s[i: i + 2]
#         mylist.append(pair)
#
#     return mylist
#
# solution("fgh")
rev_words = [ ]

def reverse_words(text):

    word = text.split(" ")
    for x in word:
        abc = x[::-1]
        rev_words.append(abc)
    # print(rev_words)
    result = ""
    for item in rev_words:
        result +=  item + " "
        # print(result)
    return  result.strip()
reverse_words( "hello my name is biraj")