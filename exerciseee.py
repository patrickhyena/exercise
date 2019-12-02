prices = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3

}
stocks = {
 "banana": 5,
 "apple": 0,
 "orange": 9,
 "pear": 6
}
for keys in prices:
    print("\n" + keys)
    print("prices: " + str(prices[keys]))
    print("stock: " + str(stocks[keys]))

total = 0
for i in prices:
    total += prices[i] * stocks[i]

print("\nTotal = " + str(total))

