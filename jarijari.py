print("\n=== PROGRAM KONVERSI SUHU ===")

# Input suhu dalam Celcius
celcius = float(input("Masukkan suhu dalam Celcius: "))

# Rumus konversi: F = (C × 9/5) + 32
fahrenheit = (celcius * 9/5) + 32

# Menampilkan hasil
print(f"\nSuhu dalam Celcius: {celcius}°C")
print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f}°F")