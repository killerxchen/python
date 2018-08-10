    communityNameflag = "resblockName"
    communityNamediv = soup.find(text=re.compile(communityNameflag))
    communityNameStartIndex = communityNamediv.find(communityNameflag) + len(communityNameflag)
    communityName = communityNamediv[communityNameStartIndex + 2 :]
    communityNameEndIndex = communityName.find(",")
    print(communityName[0:communityNameEndIndex - 1])

    communityIdflag = "resblockId"
    communityIddiv = soup.find(text=re.compile(communityIdflag))
    communityIdStartIndex = communityIddiv.find(communityIdflag) + len(communityIdflag)
    communityId = communityIddiv[communityIdStartIndex + 2 :]
    communityIdEndIndex = communityId.find(",")
    print(communityId[0:communityIdEndIndex - 1])
