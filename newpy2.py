# ###############################Q1
# def sum(numbers):
#     total = 0
#     for x in range(numbers):
#         total += x
#     return total
# print(sum((11)))
# # ###########################################Q2
# list1 = [8, 15, 32, 42, 60, 75, 122, 132, 150, 180, 190]
# for i in list1:
#     if i%4==0 and i<120 :
#         print(i)
# ##############################Q3
# num1 = [5, 15, 20, 25, 30]
# # num1.reverse()
# # print(num1)
# # num1=num1[::-1]
# # print(num1)
# for i in list(reversed(num1)):
#     print(i)

print('helloWorld'[0])
print('tinker'[1:4])
print(set('paellel'))
print([t[:-1] + (100,) for t in [(10, 20, 30), (40, 50, 90), (70, 80, 60)]])
result = ''
sample = {'1':['a','b'], '2':['c','d']}
list_1 = sample['1']
list_2 = sample['2']
for i in list_1:
    for j in list_2:
        result = i + j
        print(result)

