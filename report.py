import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
data = pd.read_csv('tips (1).csv')

data.dropna(inplace=True)
data['total_bill'] = data['total_bill']* 100

with PdfPages('report.pdf') as pdf:
    plt.figure()
    plt.plot(data['total_bill'])
    plt.title('Total Bill report')
    plt.xlabel('Index')
    plt.ylabel('Total Bill')
    pdf.savefig()
    plt.show()
    plt.close()
