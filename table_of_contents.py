from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
import os
import textwrap
from pdf_utils import draw_footer, draw_header

def generate_table_of_contents(folder_path, page_width, page_height, margin, file_pages):
    toc_canvas = canvas.Canvas("toc.pdf", pagesize=A4)
    toc_page_num = 1

    # Header
    draw_header(toc_canvas, margin, page_width, page_height, folder_path, 'Table of Contents', 1, is_toc=True)  # use toc_canvas instead of c
    draw_footer(toc_canvas, margin, page_width, toc_page_num, is_toc=True)
    toc_canvas.setFont("Helvetica", 12)

    # Draw the ToC
    y_start = page_height - margin - 70
    y_threshold = margin + 70
    y = y_start

    for directory in sorted(set(os.path.dirname(full_path) for full_path, _ in file_pages)):
        if y <= y_threshold:
            # Create new page and add header/footer
            toc_canvas.showPage()
            toc_page_num += 1
            draw_header(toc_canvas, margin, page_width, page_height, folder_path, 'Table of Contents', toc_page_num, is_toc=True)
            draw_footer(toc_canvas, margin, page_width, toc_page_num, is_toc=True)
            toc_canvas.setFont("Helvetica", 12)
            y = y_start

        toc_canvas.setFont("Helvetica-Bold", 12)
        folder_text = toc_canvas.beginText(margin, y)
        folder_text.textLine(directory)
        toc_canvas.drawText(folder_text)
        toc_canvas.line(margin, y - 1, margin + stringWidth(directory, "Helvetica-Bold", 12), y - 1)
        y -= 14  # Adjust the line spacing as needed
        toc_canvas.setFont("Helvetica", 12)

        for full_path, page_range in file_pages:
            if os.path.dirname(full_path) == directory:
                if y <= y_threshold:
                    # Create new page and add header/footer
                    toc_canvas.showPage()
                    toc_page_num += 1
                    draw_header(toc_canvas, margin, page_width, page_height, folder_path, 'Table of Contents', toc_page_num, is_toc=True)
                    draw_footer(toc_canvas, margin, page_width, toc_page_num, is_toc=True)
                    toc_canvas.setFont("Helvetica", 12)
                    y = y_start

                if page_range[0] == page_range[1]:
                    page_info = f'{page_range[0]}'
                else:
                    page_info = f'{page_range[0]} - {page_range[1]}'

                # The indent, filename and dots
                toc_canvas.drawString(margin + 20, y, full_path)
                page_info_width = stringWidth(page_info, "Helvetica", 12)
                dots_width = page_width - margin - (margin + 20 + stringWidth(full_path, "Helvetica", 12) + page_info_width)
                toc_canvas.drawString(margin + 20 + stringWidth(full_path, "Helvetica", 12), y, '.' * int(dots_width / stringWidth('.', "Helvetica", 12)))
                toc_canvas.drawRightString(page_width - margin, y, page_info)
                y -= 14  # Adjust the line spacing as needed

    toc_canvas.save()
    return "toc.pdf"