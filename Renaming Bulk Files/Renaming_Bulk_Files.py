import os


def main():
    i = 0
    path = "C:/Users/Windows 7/Desktop/Baby names/"
    for file_name in os.listdir(path):
        my_dest = "text" + str(i) + ".txt"
        my_source = path + file_name
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == "__main__":
    main()
