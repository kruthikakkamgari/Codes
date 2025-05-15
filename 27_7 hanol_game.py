def tower_of_hanol(n, source,auxilary,destination):
    if n==1:
        print(f"Move disk one from{source} to {destination} ")
        return
    tower_of_hanol(n-1,source,destination,auxilary)
    print("Move disk {n} from {source}to {destination}")
    tower_of_hanol(n-1,auxilary,source,destination)
n=int(input())
tower_of_hanol(n,'A','B','C')