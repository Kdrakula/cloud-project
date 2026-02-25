# 1. Wybieramy oficjalny, lekki obraz Pythona
FROM python:3.9-slim

# 2. Tworzymy folder roboczy wewnątrz kontenera
WORKDIR /app

# 3. Kopiujemy listę zależności i instalujemy je
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopiujemy resztę naszego kodu (app.py)
COPY . .

# 5. Informujemy, że aplikacja używa portu 8080
EXPOSE 8080

# 6. Komenda, która uruchamia aplikację
CMD ["python", "app.py"]
