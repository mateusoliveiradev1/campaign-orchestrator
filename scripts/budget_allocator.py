import sys
def allocate(budget):
    b = float(budget)
    print(f"[BUDGET SPLIT] Meta/IG: ${b*0.5:.2f} | Search: ${b*0.3:.2f} | LinkedIn: ${b*0.2:.2f}")
if __name__ == "__main__":
    if len(sys.argv) > 1: allocate(sys.argv[1])
