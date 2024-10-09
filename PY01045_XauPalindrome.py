# s = input()
# f = [[0] * len(s) for _ in range(len(s))]

# for i in range(len(s)):
#     f[i][i] = 1
# for i in range(len(s)):
#     for j in range(len(s)):
#         print(f[i][j], end = " ")
#     print()
# for j in range(2, len(s) + 1):
#     for i in range(len(s) - 1):
#         if(j == 2):
#             if(s[i] == s[i + 1]):
#                 f[i][i + 1] = 1
#         else:
#             if(i <= len(s) - j and s[i] == s[j + i - 1] and f[i + 1][j - 1] == 1):
#                 f[i][j] = 1
# cnt = 0
# for i in range(len(s)):
#     for j in range(len(s)):
#         print(f[i][j], end = " ")
#         if f[i][j] == 1:
#             cnt+= 1
#     print()
# print(cnt)
s = input()
print(len(s) - 1)