    flag = "resblockName"
    xiaoqu = soup.find(text=re.compile(flag))
    xiaoquStartIndex = xiaoqu.find(flag) + len(flag)

    xiaoqu = xiaoqu[xiaoquStartIndex+ 2 :]
    xiaoquEndIndex = xiaoqu.find(",")
    print(xiaoqu[0:xiaoquEndIndex - 1])
