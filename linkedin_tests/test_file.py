import openpyxl
import pytest
import xlrd

#using list
def get_data():
    return [
        ["test", "test123"],
        ["test2", "test1234"],
        ["test3", "test12345"]
    ]

#using excel files - xlrd library
def get_excel_data():
    workbook = xlrd.open_workbook("C:\\Users\\DELL\\TestData\\logincredstwo.xls")
    sheet = workbook.sheet_by_name('logincreds2')
    data = []
    headers = []
    for col in range(sheet.ncols):
        header_value = sheet.cell_value(0, col)
        headers.append(header_value)
    print("Headers : ", headers)

    for row in range(1, sheet.nrows):
        row_data = {}
        for col in range(sheet.ncols):
            row_data[headers[col]] = sheet.cell_value(row, col)
        data.append(row_data)

    return data


@pytest.mark.parametrize("data", get_excel_data())
def test_datadriven_two(data):
    username = data['username']
    password = data['password']
    print(username, password)

#using csv library
import csv

def get_data_csv():
    file=open("C:\\Users\\DELL\\TestData\\logincreds.csv")
    data=csv.reader(file)
    return list(data)

def test_csv():
    print(get_data_csv())


