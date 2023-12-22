n=int(input())        #输入数据总行数
for i in range(n):       #遍历每一行
    s=input().split()  #输入一行数据
    s1,s2=s[0],s[1]   #s1主串，s2待查找子串
    i=0            #初始化s2在s1中的起始位置？？
    if s1.find(s2)==-1:   #在主串s1中未查找到子串s2（情况一）
        print('no')     #输出no
        continue      #回到循环开始处处理下一行数据（停止本次循环，进行下一次循环
    if s1.count(s2)==1:   #若s2在s1中只出现1次，输出其位置，回到循环开始处（情况二）
        print(s1.find(s2))
        continue        
    while True:               #如果非上述两种情况，则进行如下处理（情况三）
        d=s1.find(s2)          #查找s2在s1中的位置，记为d  （返回的是起始位置）
        if len(s1)<=len(s2):      #当s1的长度小于s2，即结束查找
            break
        if d==0:              #若d为0，则s2的起始位置从0开始
            print(i,end=' ')     #输出子串s2出现的位置
            d=d+len(s2)       #修改之后查找的起始位置
            s1=s1[d:]         #修改s1
            i=i+d             #修改i，i即s2在原s1中的位置
        else:                 #若d不为0            
            i=i+d      #从当前位置向后？？？
            print(i,end=' ')    #输出子串s2出现的位置？？？
            s1=s1[d+len(s2):]   #修改s1
    print()
