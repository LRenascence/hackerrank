import re

# get the input
N = int(input())
urlList = []
for i in range(N):
    urlList.append(input())

domainList = set()
# extract the domain
for i in urlList:
    domain = re.findall(r'https?:\/\/((?:ww[w2]\.)?(?:[\-a-zA-Z0-9]+\.)+[a-zA-Z0-9]+)', i)
    if domain:
        for j in domain:
            j = j.replace('www.', '')
            j = j.replace('ww2.', '')
            domainList.add(j)

# sort the domainList
domainList = list(domainList)
domainList.sort()

# format the output
print(';'.join(domainList))
