############# Parameters for the user

extensions = ['.py', '.html', '.css']
#Example of extensions supported : `extensions = ['.txt', '.csv', '.py', '.json', '.xml', '.html', '.css', '.md', '.log', '.yaml', '.ini', '.cfg', '.bat', '.sh', '.sql', '.php', '.java', '.cpp', '.c', '.h', '.js', '.jsx', '.ts', '.tsx', '.rb', '.pl', '.r', '.go', '.swift', '.vb']`

folder_path = r'C:\Users\Utilisateur\Desktop\pdf_generator'
#Example (Windows) : folder_path = r'C:\Users\YourUsername\Documents\MyFiles'

output_path = r'C:\Users\Utilisateur\Desktop\dezsfrgt\pdf_generator.pdf'
#Example (Windows) : output_path = r'C:\Users\YourUsername\Desktop\MyPDF.pdf'

# Once the parameters set, execute this code (/!\ If the PDF already exists, be sure that the file is closed during the execution)

############# 

if __name__ == "__main__":
    from pdf_generator import generate_pdf_from_folder
    generate_pdf_from_folder(folder_path, output_path)