from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
import os
import textwrap

def generate_title_page(c, folder_path, extensions, page_width, page_height, margin):
    y_start = page_height - margin
    width = page_width - 2 * margin
    title_font_size = 44
    subtitle_font_size = 28
    extensions_font_size = 14
    extension_limit = (page_height - 2*margin) / (extensions_font_size * 1.5)

    # Calculate the total block height
    title_height = title_font_size * 1.5
    subtitle_height = subtitle_font_size * 1.5
    total_block_height = title_height + subtitle_height

    # Centered positions
    y_position = page_height / 2 + total_block_height / 2

    c.setFont("Helvetica-Bold", title_font_size)
    folder_name = os.path.basename(folder_path)
    title_lines = textwrap.wrap(folder_name, width=int(width / (title_font_size/2)))
    for title_line in title_lines:
        c.drawCentredString(page_width/2, y_position, title_line)
        y_position -= title_font_size * 1.5

    c.setFont("Helvetica", subtitle_font_size)
    subtitle = "Extension extracted" if len(extensions) == 1 else "Extensions extracted"
    c.drawCentredString(page_width/2, y_position, subtitle)
    y_position -= subtitle_font_size * 1.5

    c.setFont("Courier", extensions_font_size)

    for i, ext in enumerate(extensions):
        if y_position <= margin:
            c.showPage()  # Add a new page for the remaining extensions
            c.setFont("Courier", extensions_font_size)
            y_position = page_height - margin
        extension_line = ', '.join(textwrap.wrap(ext, width=int(width / (extensions_font_size/2))))
        c.drawCentredString(page_width/2, y_position, extension_line)
        y_position -= extensions_font_size * 1.5

    c.showPage()