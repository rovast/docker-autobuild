FROM php:7.4-fpm

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    zip unzip libzip-dev \
    cron \
    git \
    libicu-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libmagickwand-dev \
    --no-install-recommends

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/

# Configure core extensions
RUN docker-php-ext-configure intl \
    && docker-php-ext-configure gd --with-freetype --with-jpeg

# Install extensions
RUN docker-php-ext-install -j$(nproc) intl zip pdo pdo_mysql mysqli pcntl bcmath gd \
    && pecl install mongodb redis imagick \
    && docker-php-ext-enable \
    intl zip pdo pdo_mysql mysqli pcntl bcmath gd imagick \
    mongodb redis imagick

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Set mirror for china users
RUN composer config -g repo.packagist composer https://packagist.phpcomposer.com
