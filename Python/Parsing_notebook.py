import xml.etree.ElementTree as ET
import pandas as pd

data = []

# FILE 1
tree = ET.parse("response-budi.xml")
root = tree.getroot()

user = root.find("user")

data.append({
    "ID/NIM": user.find("id").text,
    "Nama": user.find("name").text,
    "Prodi": user.find("prodi").text,
    "Status": user.find("Status").text,
    "Angkatan": user.find("Angkatan").text
})

# FILE 2
tree = ET.parse("response-andi.xml")
root = tree.getroot()

mhs = root.find("Mahasiswa")

data.append({
    "ID/NIM": mhs.find("NIM").text,
    "Nama": mhs.find("Nama").text,
    "Prodi": mhs.find("Prodi").text,
    "Status": mhs.find("Status").text,
    "Angkatan": mhs.find("Angkatan").text
})

df = pd.DataFrame(data)

print(df)

df.to_csv("hasil_parsing.csv", index=False)