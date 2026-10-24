#Converting Hexadecimal to Denary
def hex_to_denary(hex_in):
    #only convert values A to F
    hex_A_to_F = [["A", "10"], ["B", "11"], ["C", "12"], ["D", "13"],
                  ["E", "14"], ["F", "15"]]

    convert = False
    for count in range(len(hex_A_to_F)):
        if hex_in == hex_A_to_F[count][0]:
            convert = True
            return int(hex_A_to_F[count][1])

        #if values are not A to F i.e. 1 to 9, return these as integers

    if convert == False:
        return int(hex_in)

def main():

    hexi = input("Enter a hex digit to convert: ")
    hex_out = hex_to_denary(hexi)
    print("The denary equivalent is", hex_out)
