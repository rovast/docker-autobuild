FROM php:7.2-fpm

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    zip unzip libzip-dev \
    cron \
    git \
    libicu-dev

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/

RUN docker-php-ext-configure intl

# Install extensions
RUN docker-php-ext-install zip intl pdo pdo_mysql mysqli \
    && pecl install \
    mongodb \
    redis \
    && docker-php-ext-enable zip intl pdo pdo_mysql mysqli mongodb redis

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
