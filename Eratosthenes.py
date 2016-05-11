import math


def cal(n):
    i = 0
    list = []
    while i <= n:
        list.append(i)
        i = i+1
    list[1] = 0

    j = 2 ;


    while j<=math.sqrt(n):
        k = j+1;
        while k<=n:
            if(list[k] !=0) and (list[k]%j == 0):
                list[k]=0
            k = k+1
        j = j+1

    for i in range(0,len(list)):
        if (list[i] != 0):
            print(list[i])

def main():
    cal(100000)


if __name__ == '__main__':
    main()


