# To take input of budget
while True:
    try:
        bg = float(input("Enter your budget: "))
        s = bg
    except ValueError:
        print("Print number as amount")
        continue
    else:
        break

'#Primary Dictionary'
a = {"name": [], "Quantity": [], 'Price': []}

# Values of a dictionary in list
b = list(a.values())

# indexed values of b list
na = b[0]
qu = b[1]
pr = b[2]

# Product Program
while True:
    '#The input of user that he/she want to add product or not'
    try:
        ch = int(input("1. Add\n2.Exit\nEnter your choice: "))
    except ValueError:
        print("\nERROR!Chose only digits from the given option")
        continue
    else:
        # If user want to add product
        if ch == 1:
            # Product Information input
            pn = input("Enter product name: ")
            q = int(input("Enter quantity: "))
            p = float(input("Enter price of the product: "))

            # Price calculation
            r = float(q) * p

            # Can user buy this product or not
            # noinspection PyUnboundLocalVariable
            if r > s:
                print("\nCan`t Buy this product")
                continue
            else:
                # If the Product name already exist in the dictionary
                if pn in na:
                    ind = na.index(pn)
                    qu.remove(qu[ind])
                    pr.remove(pr[ind])
                    qu.insert(ind, q)
                    pr.insert(ind, r)
                    # noinspection PyUnboundLocalVariable
                    s = bg - sum(pr)
                    print("\nAmount left", s)

                # If the Product name does not exist in the dictionary
                else:
                    na.append(pn)
                    qu.append(q)
                    pr.append(r)
                    s = bg - sum(pr)
                    print("\nAmount Left: ", s)

            # The statement of loop that is it go back to the loop or not
            if s <= 0:
                print("NO Budget")
                break
            else:
                continue

        # If user choose to exit
        elif ch == 2:
            break

        # If users giver wrong input
        else:
            print("Wrong input. Please give the correct input")
            continue

# Left amount printing
print("\nAmount left: Tk", s)

# Printing the final Grocery List
print("\n\nGrocery List")
for i in range(len(na)):
    print(na[i], qu[i], pr[i])