from tabulate import tabulate

def tableView(headers: list, data: list):
    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)