# 14. Given a list of numbers, find and print all elements that are an even
# number. In this case use a for-loop that iterates over the list, and not over
# its indices! That is, don't use range(На английском языке, чтобы Вы научились )

this_is_list = [1,2,4,5,78,6,9,0,3]
for i in this_is_list:
    if i % 2 == 0:
        print(i)