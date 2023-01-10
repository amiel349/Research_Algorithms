import gspread
import networkx as nx
from EX10.flask_example.algo import maximum_weight_fractional_matching


def read_and_write_gspread(url):
    account = gspread.service_account(r'C:\Users\amiel\PycharmProjects\Research_Algorithms\EX10\flask_example\credentials.json')
    try:
        spreadsheet = account.open_by_url(url)
    except Exception as e:
        raise Exception(f'Failed to open google sheet, please check url. {e}')

    input_sheet = spreadsheet.worksheet("Input")
    rows_val = input_sheet.row_values(1)
    col_val = input_sheet.col_values(1)
    rows_len = len(rows_val)
    col_len = len(col_val)
    G = nx.Graph()
    G.add_nodes_from(rows_val[1:-1])
    for i in range(2, rows_len+1):
        x = rows_val[i-1]
        for j in range(2, col_len+1):
            y = col_val[j-1]
            if x == y:
                continue
            if G.has_edge(x, y) or G.has_edge(y, x):
                continue
            celll_val = input_sheet.cell(i, j).value
            weight = celll_val if celll_val else 1
            G.add_edge(x, y, weight=weight)
    res = maximum_weight_fractional_matching(G)
    try:
        spreadsheet.del_worksheet(spreadsheet.worksheet("Output"))
    except Exception as e:
        print(f"worksheet doesnt exists as expected {e}")
    spreadsheet.add_worksheet("Output", input_sheet.row_count, input_sheet.col_count)
    output_sheet = spreadsheet.worksheet("Output")
    for index, value in enumerate(rows_val):
        output_sheet.update_cell(1, index+1, value)
    for index, value in enumerate(col_val):
        output_sheet.update_cell(index+1, 1, value)

    for i in range(2, rows_len+1):
        x = rows_val[i-1]
        for j in range(2, col_len+1):
            y = col_val[j-1]
            if x == y:
                continue
            if (x, y) in res:
                cell_val = res[x, y]
            else:
                cell_val = res[y, x]
            output_sheet.update_cell(i, j, cell_val)
    return len(G.nodes), len(G.edges), res


# if __name__ == '__main__':
#     read_and_write_gspread('https://docs.google.com/spreadsheets/d/13Sr8vQ5QJ3T7oa71SDBc2_SRtg-YXt8sl9wzfuNrIqo/edit#gid=0')

