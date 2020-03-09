import tabula

f = '/home/joe/data/covid19/20200307.pdf'
#tabula.convert_into(f,"out.csv",output_format="csv",pages='all')
tables = tabula.read_pdf(f, pages = "all", multiple_tables = True)
nTables = len(tables)
n = 0
while n < nTables:
    print("n: ", n) 
    print(tables[n])
    n += 1





 