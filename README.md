# Cloud Native Web App ☁️

Prosta aplikacja w Pythonie (Flask) zliczająca odwiedziny, podłączona do bazy Redis. Projekt przygotowywany pod wdrożenie w Kubernetes.

## 🛠 Wymagania
- macOS (M-series / Apple Silicon)
- OrbStack (lub Docker Desktop)
- Python 3

## 🚀 Jak uruchomić projekt lokalnie (Model Hybrydowy)

### Krok 1: Aktywacja środowiska Python
Zawsze zaczynaj od wejścia do folderu i aktywacji izolowanego środowiska:
\`\`\`bash
cd ~/cloud-project
source venv/bin/activate
\`\`\`

### Krok 2: Uruchomienie bazy danych (Redis) w Dockerze
Jeśli kontener jeszcze nie istnieje, stwórz go i uruchom:
\`\`\`bash
docker run -d -p 6379:6379 --name moj-redis redis
\`\`\`
*(Jeśli kontener już istnieje, ale jest wyłączony, użyj: `docker start moj-redis`)*

### Krok 3: Uruchomienie aplikacji
Gdy baza danych działa, uruchom serwer Pythona:
\`\`\`bash
python app.py
\`\`\`

### Krok 4: Testowanie
Otwórz przeglądarkę i wejdź pod adres:
[http://localhost:5000](http://localhost:5000)

---
## 🧹 Przydatne komendy
- `docker ps` - sprawdza, czy Redis faktycznie działa w tle.
- `docker stop moj-redis` - zatrzymuje bazę danych.
- `Ctrl+C` (w terminalu z Pythonem) - zatrzymuje aplikację.
