# Provided data
data = """
prefix	name	family_name
Mr	Abbas	Fadlallah
Mr	Abbas	Chaady
Mr	Abdallah	Suleiman
Mr	Ahmad	Hmede
Mr	Ahmad	Tahir
Mr	Ali	Hammoud
Mr	Ali	Jammal
Mr	Ali	Zein
Mr	Ali	Akar
Mr	Ali	Said
Mr	Ali	Dangote
Mr	Ali	Khan
Mr	Ali	Taher
Miss	Amina	Ebonique
Mr	Anis	Makki
Mr	Aseel Saleh	Saleh
Miss	Athena	Keswani
Miss	Aya	Ghaddar
Mrs	Dalal	Zabat
Mrs	Fatima	Babagana
Mrs	Fatima	Gawuna
Mrs	Fatima	Kyaure
Miss	Fatima	Dandawaki
Mr	Foad	Hammoud
Mrs	Fozia	Mansury
Mr	Geryes	Bejjani
Mr	Ghazi	Mansour
Mrs	Ghida	Kassem
Miss	Grizelda	Jammal
Mr	Hadi	Fawaz
Mr	Hadi	Fadlallah
Mr	Haidar	Tahtah
Mr	Haidar	Atwi
Mr	Haidar	Fares
Mrs	Hamo	Fawaz
Miss	Hana 	Mustapha
Mrs	Hanan	Mansury
Mr	Hassan	Zein
Mr	Hassan	Jammal
Mr	Hassanein	Baydoun
Mr	Hussein	Tormos
Mr 	Hussein 	Jaffar
Mr	Ibrahim	Akar
Miss	Inaiya	Haq
Mr	Ismail	Mansury
Mr	Issa 	Fares
Mr	Jad	Haidar
Mrs	Jamila	Haq
Mr	Karim	Attar
Mr	Kassem	Saleh
Miss	Kawthar	Fadlallah
Mr	Khalifa	Dangote
Mr	Khudor	Elamin
Miss	Lara	Kassem
Mr	Mahdi	Fadlallah
Miss	Mariam	Dib
Miss	Mariam	Karram
Mrs	Maryam	Zabat
Miss	Mimz	Said
Mr	Mo	Saidi
Mr	Moe	Jaffar
Mr	Mohammad	Atwi
Mr	Mohammad	Tawbi
Mr	Mohammad	Saidi
Mr	Mohammed	Zein
Mr	Mohd Ali	Jebara
Mr	Mohd Ali	Jaffar
Mr 	Mustafa	Noureldeen
Mr	Musty	Akar
Miss	Nada	Kidami
Mr	Nadeem	Dandawaki
Miss	Nana	Kassem
Mr	Nehme 	Dayekh
Mrs	Noory	Khan
Miss	Nour	Fadlallah
Mrs	Rayan	Salma
Miss	Reema	Kamal
Mrs	Reena 	Kassem
Mr	Roda 	Berjawi
Mr	Roda 	Soufan
Mr	Saed	Zein
Mr	Safi	Zai
Mr	Said 	Dayekh
Mr	Saleh	Mansury
Mr	Samer	Mansour
Miss	Sara	Dib
Mrs	Shaheen	Sayed
Mr	Suleiman	Dayekh
Mrs	Taihida	Babagana
Mr	Yahya	Yahya
Miss	Yara	Yassin
Mr	Youssef	Shour
Mr	Yusef	Mansury
Miss	Zahra	Saidi
Mrs	Zainab	Khalil
Miss	Zainab	Attar
Miss	Zaza	Fayad

"""

# Split the data into lines
lines = data.strip().split('\n')

# Extract headers and remove extra spaces
headers = lines[0].split()
headers = [header.strip() for header in headers]

# Initialize the list to store couples data
couples_to_import = []

# Iterate over the remaining lines to create dictionaries for each couple
for line in lines[1:]:
    # Split each line into values and remove extra spaces
    values = line.split()
    values = [value.strip() for value in values]
    
    # Create a dictionary for the couple and add it to the list
    couple = {header: value for header, value in zip(headers, values)}
    couples_to_import.append(couple)

# Print the list of dictionaries
print(couples_to_import)
