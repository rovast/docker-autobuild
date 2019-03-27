FROM gcc:8

# Install dependencies
RUN apt-get update && apt-get install -y gdb

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/

# Set workdir
WORKDIR /home/Code
