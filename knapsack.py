def kanpsack(cap,weight,profit,n,items):
    if cap==0 or n ==0:
        return 0
    
    if weight[n-1]>cap:
        return kanpsack(cap,weight,profit,n-1,items)

    else:
        profit_with_item = profit[n-1]+kanpsack(cap-weight[n-1],weight,profit,n-1,items)
        profit_without_item = kanpsack(cap,weight,profit,n-1,items)

        if profit_with_item> profit_without_item:
            items.add(n-1)
        
        return max(profit_with_item,profit_without_item)
    
items =set()

print("Enter profit of each item")
profit = list(map(int,input().split(' ')))

print("Enter weight of each item")
weight = list(map(int,input().split(' ')))

cap = int(input("Enter max capacity"))
n = len(profit)
max_profit = kanpsack(cap,weight,profit,n,items)

print("Max profit is ",max_profit)
print("Selected items are ",items)
