FROM python
WORKDIR /home/myapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5055
CMD ["python3", "sample_app.py"]