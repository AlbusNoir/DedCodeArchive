# defang ip
# input x.x.x.x output x[.]x[.]x[.]x

def defang(address):
    address = address.split(".")  # split at .
    output = "[.]".join(address)  # return [.] at any .
    print(output)


inp = input("Enter IP address to defang: ")

defang(inp)
