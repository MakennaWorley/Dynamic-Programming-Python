def change_making(d,n):
    amount = [0] * (n + 1)
    for i in range(1, n + 1):
        proposal_amount = []
        for j in range(len(d)):
            if i >= d[j]:
                proposal_amount.append(amount[i - d[j]] + 1)
        amount[i] = min(proposal_amount)
    return amount[-1]


if __name__ == "__main__":
    d=[1,3,4,5,6]
    n=10
    print(change_making(d,n))
    
    d=[1,2,4,6,8,10,22,23]
    n=40
    print(change_making(d,n))

    d=[1,2,10,11,12,15,19,30]
    n=1900
    print(change_making(d,n))

