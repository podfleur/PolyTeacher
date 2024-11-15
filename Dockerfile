# Choose your OS system
FROM python:3.8.10

# Log level
ENV PYTHONUNBUFFERED 1

#API
ENV API_KEY AIzaSyCmYrzD3f23p7p_QUvWk06G67-5i4O27UY

# Make working directory
RUN mkdir /polyteacher

# Change the current working directory
WORKDIR /polyteacher

# Copy and link
ADD . /polyteacher

# Install the libraries
RUN pip install -r requirements.txt