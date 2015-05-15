import csv

with open('data/000101027265_0415_20150514164017.csv', newline='') as csvfile:
  with open('data/metrozoho.csv', 'w+') as csvout:
    writer = csv.writer(csvout, lineterminator='\n')
    cs = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(cs, None)  # skip the first row from the reader, the old header
    writer.writerow(['Date-dd/MM/YY', 'Withdrawals', 'Deposits', 'Payee', 'Description', 'Reference Number']) # write new header
    for line in cs:
        writer.writerow((line[4],line[8],line[9],'',line[5],line[6]))
