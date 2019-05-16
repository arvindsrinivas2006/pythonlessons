class TacoCalculator:
    taco_quantity=0
    burrito_quantity=0
    # ask manager: obtain price of taco
    veggie_taco_price=input("Manager, how much is a taco today?")
    veggie_taco_price=eval(veggie_taco_price)
    
    bean_burrito=input("Manager, how much is a bean burrito today?")
    bean_burrito=eval(bean_burrito)

    # ask customer: how many tacos
    customer_order=input("Would you like to purchase: 1) veggie taco and/or 2) bean burrito?")
    if "1" in customer_order:
        taco_quantity=input("How many tacos would you like?")
        taco_quantity=eval(taco_quantity)

    if "2" in customer_order:
        burrito_quantity=input("How many burritos would you like?")
        burrito_quantity=eval(burrito_quantity)

    # calculate order before tax
    taco_order=taco_quantity*veggie_taco_price
    burrito_order=burrito_quantity*bean_burrito

    total_order=taco_order+burrito_order

    print("customer, your order comes to $", total_order)

    # calculate sales tax
    sales_tax_rate=0.05
    sales_tax_amount=sales_tax_rate*total_order

    # calculate grand total
    grand_total=sales_tax_amount+total_order

    print("customer, your grand total comes to $", grand_total)
