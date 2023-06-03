from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
import os
import textwrap
from PyPDF2 import PdfWriter, PdfReader
from title_page import generate_title_page
from pdf_utils import draw_footer, draw_header
from table_of_contents import generate_table_of_contents
from config_and_launch import extensions, folder_path, output_path

def generate_pdf_from_folder(folder_path, output_path):
    page_width, page_height = A4
    margin = 2 * 28.3465  # Margin in points (2cm)
    y_start = page_height - margin - 70  # Adjust the starting position as needed
    y_threshold = margin + 70  # Adjust the threshold as needed
    width = page_width - 2 * margin  # Width of the text

    file_pages = []  # List for storing the page numbers of each file

    # Temporary output paths for the three passes
    temp_output_path_title = output_path.replace('.pdf', '_temp_title.pdf')
    title_canvas = canvas.Canvas(temp_output_path_title, pagesize=A4)
    temp_output_path_code = output_path.replace('.pdf', '_temp_code.pdf')

    # First pass to generate the code pages and record the page numbers
    c = canvas.Canvas(temp_output_path_code, pagesize=A4)
    total_page_num = 1

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                full_path = os.path.join(os.path.basename(folder_path), relative_path)

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                file_page_start = total_page_num
                file_page_num = 1

                # Header
                draw_header(c, margin, page_width, page_height, folder_path, full_path, file_page_num)
                c.setFont("Courier", 10)

                # Draw file content
                lines = content.split('\n')
                y = y_start
                for line in lines:
                    # Wrap the line
                    wrapper = textwrap.TextWrapper(width=int(width / 6))  # 6 approximates average character width in points
                    wrapped_lines = wrapper.wrap(line)
                    for wrapped_line in wrapped_lines:
                        if y <= y_threshold:
                            # Footer
                            draw_footer(c, margin, page_width, total_page_num)

                            # Create new page and add header
                            c.showPage()
                            file_page_num += 1
                            total_page_num += 1
                            draw_header(c, margin, page_width, page_height, folder_path, full_path, file_page_num)
                            c.setFont("Courier", 10)
                            y = y_start

                        c.drawString(margin, y, wrapped_line)
                        y -= 14  # Adjust the line spacing as needed

                # Footer
                draw_footer(c, margin, page_width, total_page_num)
                c.showPage()

                file_pages.append((full_path, (file_page_start, total_page_num)))

                total_page_num += 1
    c.save()

    # Generate the title page
    generate_title_page(title_canvas, folder_path, extensions, page_width, page_height, margin)
    title_canvas.save()

    # Generate the table of contents
    toc_file = generate_table_of_contents(folder_path, page_width, page_height, margin, file_pages)

    # Create a PdfWriter object
    writer = PdfWriter()

    # Add the title page at the beginning
    reader = PdfReader(temp_output_path_title)
    for i in range(len(reader.pages)):
        writer.add_page(reader.pages[i])

    # Add the ToC pages
    reader = PdfReader(toc_file)
    for i in range(len(reader.pages)):
        writer.add_page(reader.pages[i])

    # Add the previously generated code pages
    reader = PdfReader(temp_output_path_code)
    for i in range(len(reader.pages)):
        writer.add_page(reader.pages[i])

    # Write the final output PDF file
    with open(output_path, 'wb') as f:
        writer.write(f)

    # Delete the temporary files
    os.remove(temp_output_path_title)
    os.remove(temp_output_path_code)
    os.remove(toc_file)