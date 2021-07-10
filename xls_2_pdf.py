from win32com import client
import os
import sys

def convert_xl_to_pdf(path, landscape = False):
    xlApp = client.Dispatch("Excel.Application")
    is_landscape = 1
    if landscape:
        is_landscape = 2
    for filename in os.listdir(path):
        if filename.endswith(".xls"):
            print(filename)
            books = xlApp.Workbooks.Open(path + '\\' + filename)
            ws = books.Worksheets[0]
            # change orientation to landscape
            ws.PageSetup.Orientation = is_landscape
            ws.PageSetup.Zoom = False
            ws.PageSetup.FitToPagesWide = 1
            ws.PageSetup.FitToPagesTall = 1
            ws.PageSetup.BottomMargin = 0
            ws.PageSetup.TopMargin = 0
            ws.PageSetup.RightMargin = 0
            ws.PageSetup.LeftMargin = 0
            ws.Visible = 1
            pdfname = filename.split(".")[0]
            ws.ExportAsFixedFormat(0, path + "\\" + pdfname + ".pdf")

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '--landscape':
        convert_xl_to_pdf(args[1], True)
    else:
        convert_xl_to_pdf(args[0])
    print("Done.")
    
