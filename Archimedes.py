def gcd(m,n):
    if(n==0):
        return m;
    elif(m==0):
        return n;
    return gcd(n,m%n);

def main():
    print(gcd(60,24));

if __name__ == '__main__':
    main();


