FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# wtw.sh script executable
RUN chmod +x /app/wtw.sh

# Create an alias for 'wtw'
RUN echo "alias wtw='/app/wtw.sh'" >> /root/.bashrc

# Start an interactive shell by default
CMD ["bash"]
