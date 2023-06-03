from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def draw_footer(c, margin, page_width, total_page_num, is_toc=False):
    c.setFont("Helvetica", 12)
    if not is_toc:  # Don't draw the page number if it's the Table of Contents
        c.drawRightString(page_width - margin, margin, f"Doc Page: {total_page_num}")
    c.line(margin, margin + 30, page_width - margin, margin + 30)

def draw_header(c, margin, page_width, page_height, folder_path, file_path, file_page_num, is_toc=False):
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, page_height - margin, f"Project: {os.path.basename(folder_path)}")
    c.setFont("Helvetica", 14)
    if is_toc:  # If it's the Table of Contents
        c.drawString(margin, page_height - margin - 20, 'Table of Contents')
        c.setFont("Helvetica", 12)
        c.drawRightString(page_width - margin, page_height - margin - 20, f"ToC Page: {file_page_num}")
    else:  # If it's a code page
        c.drawString(margin, page_height - margin - 20, f"Path: {file_path}")
        c.setFont("Helvetica", 12)
        c.drawRightString(page_width - margin, page_height - margin - 20, f"File Page: {file_page_num}")
    c.line(margin, page_height - margin - 30, page_width - margin, page_height - margin - 30)