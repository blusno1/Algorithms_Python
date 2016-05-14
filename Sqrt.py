#牛顿迭代法
import math

import inf as inf


def NewtonSqrt(x):
    if(x<0):
        print("不能对负数开平方！")
        return -1
    if(x==0):
        return 0

    _avg=x
    last_avg = float(inf)
    _jingdu = 1e-6

    while(math.fabs(_avg-last_avg)>_jingdu):
        last_avg=_avg
        _avg=(_avg + x / _avg) / 2;
    return _avg


def main():
    print(NewtonSqrt(3.1))


if __name__ == '__main__':
    main()

