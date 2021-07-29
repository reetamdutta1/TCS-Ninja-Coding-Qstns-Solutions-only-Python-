def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    adult=no_of_adults*37550
    child=no_of_children*(37550/3)
    sum=adult+child
    after_tax=sum+(7*sum)/100
    total_ticket_cost=after_tax-(10*after_tax)/100
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)