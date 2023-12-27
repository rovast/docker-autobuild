FROM php:8-fpm-alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk update \
    && apk add --no-cache \
        --virtual=.build-dependencies \
        build-base \
        autoconf \
    && apk add --no-cache \
        openssh-client \
        freetype \
        freetype-dev \
        libjpeg-turbo \
        libjpeg-turbo-dev \
        libpng \
        libpng-dev \
        libmcrypt \
        libmcrypt-dev \
        libmemcached \
        libmemcached-dev \
        libzip-dev \
    && docker-php-ext-install -j$(nproc) pdo_mysql mysqli opcache zip \
    && docker-php-ext-configure gd --enable-gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install -j$(nproc) bcmath \
    && pecl install igbinary \
    && pecl install redis \
    && pecl install memcached \
    && pecl install mcrypt \
    && pecl clear-cache \
    && docker-php-ext-enable pdo_mysql mysqli opcache zip gd bcmath igbinary redis memcached mcrypt \
    && curl --silent --show-error https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && apk del .build-dependencies \
    && rm -rf /tmp/*

# demo
RUN sed -i 's/http:\/\/deb.debian.org/https:\/\/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list && \
    apt-get update && apt-get install -y git && apt-get install -y supervisor

COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/bin/

RUN install-php-extensions opcache pcntl
