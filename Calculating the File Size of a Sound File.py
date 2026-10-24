#Calculating the File Size of a Sound File
def file_size(frequency, bits, channels, duration):
    size = frequency * bits * channels * duration
    return size

def main():

    freq = int(input("Enter the frequency in Hz: "))
    bit_depth = int(input("Enter the bit depth: "))
    channel = int(input("Enter the number of channels: "))
    length = int(input("Enter the duartion of the sound file in seconds: "))

    size_out = file_size(freq, bit_depth, channel, length)
    size_kb = size_out / (8 * 1024)
    size_mb = size_kb / 1024
    print("The file size is", size_kb, "KB")
    print("The file size is", size_mb, "MB")

if __name__ == '__main__':
    main()
