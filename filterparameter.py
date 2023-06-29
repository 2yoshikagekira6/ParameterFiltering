import re

def filter_data(data, parameters, from_front=True):
    filtered_data = []
    patterns = [r'\b{}\w*\b'.format(re.escape(parameter.lower())) for parameter in parameters]

    for item in data:
        matches = [re.findall(pattern, item.lower()) for pattern in patterns]

        if from_front and all(matches) and all(matches[i][0] == parameters[i].lower() for i in range(len(parameters))):
            item = re.sub(r'({})'.format('|'.join([re.escape(parameter) for parameter in parameters])), r'\033[91m\1\033[0m', item)
            filtered_data.append(item)

    return filtered_data

def save_to_txt(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(item + "\n")
        print("Data berhasil disimpan dalam file {}.".format(filename))
    except:
        print("Terjadi kesalahan saat menyimpan data.")

def main():
    filename = input("Masukkan nama file: ")

    try:
        with open(filename, 'r') as file:
            data = file.read().splitlines()
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    parameters = input("Masukkan kata-kata yang ingin dicari (pisahkan dengan koma): ").split(",")

    filtered_data = filter_data(data, parameters, from_front=True)

    if len(filtered_data) == 0:
        print("Tidak ada data yang sesuai dengan parameter.")
    else:
        print("Data yang sesuai dengan parameter:")
        for item in filtered_data:
            print(item)

    save_option = input("Apakah Anda ingin menyimpan hasil filter ke dalam file? (y/n): ")
    if save_option.lower() == "y":
        save_filename = input("Masukkan nama file untuk menyimpan hasil filter: ")
        save_to_txt(save_filename, filtered_data)

if __name__ == "__main__":
    main()
