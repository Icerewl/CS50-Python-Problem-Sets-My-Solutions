def main():
    example = input('Type the mass that you want to convert to joules: \n')
    output = equation(example)
    print(output)
def equation(mass):
    massint = int(mass)
    joules = massint * 300000000 * 300000000 
    return joules

main()
