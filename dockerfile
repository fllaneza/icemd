# Python3 Image ---------------------------------------------
FROM python:3

# Installs --------------------------------------------------
COPY requirements.txt /usr/local/project/requirements.txt
RUN pip install -r /usr/local/project/requirements.txt

# Add scripts -----------------------------------------------
COPY /ec2/model.pkl /usr/local/project/model.pkl
COPY /ec2/app_rl.py /usr/local/project/app_rl.py
WORKDIR /usr/local/project

# Expose port -----------------------------------------------
EXPOSE 9999

# Run -------------------------------------------------------
CMD ["python", "app_rl.py"]
