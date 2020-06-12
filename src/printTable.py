def printTable(header, data, align="center"):
    """
    Prints table with columns of header and data.

    Parameters
    ----------
    header : []
        list of header labels
        ex. header = ["one","two","three"]
    data : [[],[],...,[]]
        list of lists, each inner list is a data line
        data line must index with header appropriately
        ex. data = [[1, 2, 3],[1, 2, 3]]
    align : str in ["left", "center", "right"]
        desired alignment for data, default = "center"
        ex. align = "right"
    """

    # print headers
    col_widths=[]
    for i,label in enumerate(header):
        col_widths.append(len(label))
        if i == 0 :
            print("| ",end="")
        print(str(label).center(len(label)), end=" | ")
    print()

    # print separating line
    for i,width in enumerate(col_widths):
        if i == 0 :
            print("| ",end="")
        print("".center(width,"-"), end=" | ")
    print()

    # print data
    for i,line in enumerate(data):
        for i,value in enumerate(line):
            if i == 0 :
                print("| ",end="")
            if align == "left":
                print(str(value).ljust(col_widths[i]), end=" | ")
            elif align == "right":
                print(str(value).rjust(col_widths[i]), end=" | ")
            else: # align = center
                print(str(value).center(col_widths[i]), end=" | ")
        print()
