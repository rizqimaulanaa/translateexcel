import pandas as pd
from deep_translator import GoogleTranslator
file_path = "1.xlsx"  # Ganti dengan path file Excel
sheet_name = "Sheet1"  # Ganti dengan nama sheet
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Kolom yang akan diterjemahkan
columns_to_translate = ['Description', 'Solution']

# Buat kolom baru untuk hasil translate
for col in columns_to_translate:
    data[f"{col}_Translated"] = data[col].apply(
        lambda text: GoogleTranslator(source='auto', target='id').translate(text) if isinstance(text, str) else text
    )

# Simpan hasil ke file baru
output_file = "translated_output.xlsx"
data.to_excel(output_file, index=False)
print(f"Hasil diterjemahkan disimpan ke: {output_file}")
