FROM php:7.2-cli

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/

# Install pecl extensions
RUN pecl install mongodb \
    redis \
    && docker-php-ext-enable mongodb redis

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
