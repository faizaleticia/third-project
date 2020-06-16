import os.path
from fpdf import FPDF


def get_data_from_prettytable(data):
    """
    Get a list of list from pretty_data table
    Arguments:
        :param data: data table to process
        :type data: PrettyTable
    """

    def remove_space(row_list):
        """
        Remove space for each word in a list
        Arguments:
            :param row_list: list of strings
        """
        list_without_space = []
        for mot in row_list:  # For each word in list
            word_without_space = mot.replace(' ', '')  # word without space
            list_without_space.append(word_without_space)  # list of word without space
        return list_without_space

    # Get each row of the table
    string_x = str(data).split('\n')  # Get a list of row
    header = string_x[1].split('|')[1: -1]  # Columns names
    rows = string_x[3:len(string_x) - 1]  # List of rows

    list_word_per_row = []
    for row in rows:  # For each word in a row
        row_resize = row.split('|')[1:-1]  # Remove first and last arguments
        row_resize = remove_space(row_resize)
        if row_resize[0] != '':
            list_word_per_row.append(row_resize)  # Remove spaces

    return header, list_word_per_row


def export_to_pdf(header, data, title):
    """
    Create a a table in PDF file from a list of row
        :param title: name of file and title of PDF
        :param header: columns name
        :param data: List of row (a row = a list of cells)
        :param spacing=1:
    """
    pdf = FPDF()  # New  pdf object

    pdf.set_font("Arial", size=12)  # Font style
    epw = pdf.w - 2 * pdf.l_margin  # Width of document
    col_width = pdf.w / 4.5  # Column width in table
    row_height = pdf.font_size * 1.5  # Row height in table
    spacing = 1.3  # Space in each cell

    pdf.add_page()  # add new page

    pdf.cell(epw, 0.0, 'Fornecedor ' + title, align='C')  # create title cell
    pdf.ln(row_height * spacing)  # Define title line style

    # Add header
    for item in header:  # for each column
        pdf.cell(col_width, row_height * spacing, txt=item, border=1)  # Add a new cell

    pdf.ln(row_height * spacing)  # New line after header

    for row in data:  # For each row of the table
        for item in row: # For each cell in row
            pdf.cell(col_width, row_height * spacing, txt=item, border=1)  # Add cell
        pdf.ln(row_height * spacing)  # New line after row

    my_path = os.path.abspath(os.path.dirname(__file__))
    pdf.output(os.path.join(my_path, '../assets/table/' + title + '.pdf'))  # Create pdf file
    pdf.close()
