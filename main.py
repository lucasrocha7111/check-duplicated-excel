import sys
import xlrd

args_size = len(sys.argv)
temp_array_of_values = []

def check_is_duplicated(obj, temp_array_of_values):
    is_duplicated = False
    for i in temp_array_of_values:
        field_size = len(obj["rows"])
        duplicated_value_array = []
        for y in range(field_size):
            if obj["rows"][y] == i["rows"][y]:
                is_item_duplicated = True
            else:
                is_item_duplicated = False
            duplicated_value_array.append(is_item_duplicated)
        true_count = 0
        for z in duplicated_value_array:
            if z == True:
                true_count += 1
        if true_count == field_size:
            is_duplicated = True
    return is_duplicated

def showResults(temp_array_of_values):
    count = 0
    for i in temp_array_of_values:
        if i["duplicated"]:
            print("Duplicated")
            print(i)
            print("\n")
            count += 1
    print("Duplicated items: %s " % count)

if args_size > 0:
    file_dir = sys.argv[args_size - 1]
    print("File directory: %s \n" % (file_dir))

    wb = xlrd.open_workbook(file_dir)
    sheet = wb.sheet_by_index(0)

    sheet.cell_value(0, 0)

    for line in range(sheet.nrows):
        line_obj = {"line": line, "rows": []}
        for row in range(sheet.ncols):
            obj = sheet.cell(line, row)
            field = {"row": row, "value": obj.value}
            line_obj["rows"].append(field)
        is_duplicated = check_is_duplicated(line_obj, temp_array_of_values)
        line_obj["duplicated"] = is_duplicated
        temp_array_of_values.append(line_obj)

    showResults(temp_array_of_values)
else:
    print("Use a valid argument")
