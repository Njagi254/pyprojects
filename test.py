s = int(input('Enter speed: '))
if 70<s<75:
    d=0
    d+=(s-70)/5 + 1
    print('Overspeeding by: ', s-70)
    print('Demerit points:', d)
elif s>70 and ((s-70)%5) == 0:
    d=0
    d+=int((s-70)/5 + 1)
    print('Overspeeding by: ', s-70)
    print('Demerit points:', d)

    if d>12:
        print('Demerit points:', d)
        print('License suspended!')
else:
    print('Within speed limit ')
