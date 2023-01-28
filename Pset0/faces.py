def convert(a):

    output = a.replace(':)','🙂')
    output1 = output.replace(':(','🙁')
    return output1

def main():
    example = input("")
    emoji = convert(example)
    print(emoji)


main()