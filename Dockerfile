FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file del progetto
COPY . .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Espone la porta Flask
EXPOSE 5000

# Comando di avvio
CMD ["python", "run.py"]
