from salary_generator import generate_csv_data, write_csv, read_csv

if __name__ == '__main__':
    filename = 'salaries_100.csv'

    #write data
    data = generate_csv_data(100)

    write_csv(filename, data)

    # read data
    data2 = read_csv(filename)
    print(data2)
