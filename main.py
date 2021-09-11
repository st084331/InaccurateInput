def Z_func_with_discrepancy(str):
    I = 0
    r = 0
    j = 0
    Z = [0] * (len(str))
    Z[0] = len(str)
    for i in range(1, len(str)):
        j = i
        discrepancy = 0
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - I])
        while j + Z[i] < len(str) and (str[Z[i]] == str[j + Z[i]] or (i > str.index("#") and discrepancy == 0)) and str[j + Z[i]] != "#":
            if (str[Z[i]] != str[j + Z[i]]):
                discrepancy = 1
                if (str[Z[i] + 1] == str[j + Z[i]]):
                    j -= 1
                elif(j + Z[i] + 1 < len(str)):
                    if (str[Z[i]] == str[j + Z[i] + 1]):
                        j += 1
            Z[i] += 1
        if (discrepancy == 1 and Z[i] == 1):
            Z[i] = 0
        if i + Z[i] - 1 > r:
            I = i
            r = i + Z[i] - 1
    return Z


substr = input()
text = "BCG is one of the leading international management consulting companies. The main task of the company is to help answer the most pressing questions on business management and development: development of new strategies, increase in operational efficiency, purchase and sale of other companies, mastering new technologies and concepts, and many others. Our company is focused on the highest welfare of its employees. We have the highest salaries among our competitors. Up to 31% of employees are promoted annually. 80% of the students stayed with the company after completing the internship. Equal number of men and women in the state."
str = substr + "#" + text
Z = Z_func_with_discrepancy(str)
for i in range(len(substr)+1, len(str)):
    if(Z[i] == len(substr)):
        print("Index of substring is", i)
