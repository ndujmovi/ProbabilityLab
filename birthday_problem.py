import random


def has_shared_birthday(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] == x[j]:
                return True
    return False


def exact_probability(n):
    a=1

    for i in range(365,365-n, -1):
        a*=i
    a/=365**n
    return 1-a


def monte_carlo_probability(n,simulations):
    matches=0


    for _ in range(simulations):
        birthdays = []
        
        for _ in range(n):
            birthday=random.randint(1,365)
            birthdays.append(birthday)

        if has_shared_birthday(birthdays):
            matches+=1


    return matches/simulations


simulations=100000
n=23

exact=exact_probability(n);

estimated=monte_carlo_probability(n,simulations)





print("People: ", n)
print("Simulations: ", simulations,end="\n\n")

print("Estimated probability: ", estimated)
print("Exact probability: ", exact)
print("Error: ", abs(estimated-exact))






