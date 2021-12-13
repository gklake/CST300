cases = int(input())
while cases > 0:
    list1 = []
    list2 = []
    for i in range(cases):
        list1.append(int(input()))
        pass
    for i in range(cases):
        list2.append(int(input()))
        pass
    dictionary = dict(zip(sorted(list1),sorted(list2)))
    for items in list1:
        print(dictionary[items])
    print()
    cases = int(input())