import openpyxl as xl

# Create a new workbook
workbook = xl.Workbook()

# Select the active sheet
sheet = workbook.active

# Give the sheet a name (optional)
sheet.title = "MySheet"

# Add data to the sheet (example data)
sheet['A1'] = "Name"
sheet['B1'] = "Age"
sheet['A2'] = "John"
sheet['B2'] = 25
sheet['A3'] = "Jane"
sheet['B3'] = 30

# Save the workbook to a file
workbook.save("my_spreadsheet.xlsx")

print("Spreadsheet created successfully!")
