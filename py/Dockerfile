# Use an official Python runtime as a parent image
FROM python:3.9.13

# 创建/app目录
RUN mkdir -p /app

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org Flask gunicorn torch transformers
# RUN pip install --trusted-host gunicorn
# RUN pip install --no-cache-dir -r requirements.txt
# 更新pip并安装Gunicorn
#RUN pip install --upgrade pip && \
#RUN pip install gunicorn
#RUN pip install --no-cache-dir -r requirements.txt
# Make port 8000 available to the world outside this container

RUN pip install --upgrade pip && \
    pip install gunicorn --no-cache-dir -r requirements.txt

EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
# timeout是为了在初次运行的时候，需要从huggingface中下载模型，需要花费时间。
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000","--timeout","3600","app2:app"]