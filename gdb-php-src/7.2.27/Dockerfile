FROM gcc:8

# Install dependencies
RUN apt-get update && apt-get install -y gdb vim

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/

RUN cd /home/  \
    && wget https://www.php.net/distributions/php-7.2.27.tar.gz \ 
    && tar -zxf php-7.2.27.tar.gz \
    && rm php-7.2.27.tar.gz

RUN cd /home/php-7.2.27 \
    && ./configure --enable-phpdbg-debug --enable-debug \
    && make \
    && find -type f -name '*.a' -delete \
    && make install

RUN echo "gdb-php-src started ..." > /home/start.md

# Set workdir
WORKDIR /home/

CMD ["tail", "-f", "/home/start.md"]
