# -*- coding: UTF-8 -*-
from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_odd_even(odd, even, outfn):
    pdf_output = PdfFileWriter()
    odd_input = PdfFileReader(open(odd, 'rb'))
    even_input = PdfFileReader(open(even, 'rb'))
    odd_page = odd_input.getNumPages()
    even_page = even_input.getNumPages()
    if odd_page == even_page:
        print('The number of pages is {}'.format(odd_page*2))
        for i in range(odd_page):
            pdf_output.addPage(odd_input.getPage(i))
            pdf_output.addPage(even_input.getPage(i))
        pdf_output.write(open(outfn, 'wb'))
    else:
        print('Check page number')


if __name__ == '__main__':
    odd = 'odd.pdf'
    even = 'even.pdf'
    filename = input('Input file name:')
    outfn = filename + '.pdf'
    merge_odd_even(odd, even, outfn)
