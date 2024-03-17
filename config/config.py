import xlrd


def get_excel_data(path):
    workbook = xlrd.open_workbook(path)
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


class TestData:
    BASE_URL = "https://www.linkedin.com/"
    BROWSER = "Chrome"
    filepath = "C:\\Users\\DELL\\TestData\\logincredstwo.xls"
