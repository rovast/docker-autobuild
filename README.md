# docker-autobuild

社区为我们提供了诸多开箱即用的镜像，但是部分的镜像由于其通用性而牺牲了定制性，这里我们基于官方的进行二次构建，进而满足更丰富的应用场景。

访问 https://hub.docker.com/r/rovast 查看更多镜像

| 状态 | 镜像               | 说明                            |
| ---- | ------------------ | ------------------------------- |
|  [![php7.2-cli](https://github.com/rovast/docker-autobuild/actions/workflows/php7.2-cli.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/php7.2-cli.yml)    | rovast/php:7.2-cli | 增加诸多拓展和开发常用软件 [^1] |
|  [![php7.2-fpm](https://github.com/rovast/docker-autobuild/actions/workflows/php7.2-fpm.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/php7.2-fpm.yml)   | rovast/php:7.2-fpm | 增加诸多拓展和开发常用软件 [^1] |
|  [![php7.4-cli](https://github.com/rovast/docker-autobuild/actions/workflows/php7.4-cli.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/php7.4-cli.yml)    | rovast/php:7.4-cli | 增加诸多拓展和开发常用软件 [^2] |
|  [![php7.4-fpm](https://github.com/rovast/docker-autobuild/actions/workflows/php7.4-fpm.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/php7.4-fpm.yml)   | rovast/php:7.4-fpm | 增加诸多拓展和开发常用软件 [^2] |
|  [![cadvisor:0.45](https://github.com/rovast/docker-autobuild/actions/workflows/cadvisor0.45.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/cadvisor0.45.yml)   | rovast/cadvisor:0.45 | gcr.io 镜像 |
|  [![kube-state-metrics:2.0](https://github.com/rovast/docker-autobuild/actions/workflows/kube-state-metrics2.0.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/kube-state-metrics2.0.yml)   | rovast/kube-state-metrics:2.0 | gcr.io 镜像 |
|  [![capistrano](https://github.com/rovast/docker-autobuild/actions/workflows/capistrano.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/capistrano.yml)   | rovast/capistrano | capistrano 镜像构建 |
| TODO | rovast/gcc:8 |  增加了 gdb，方便调试 |
| TODO | rovast/gdb-php-src:7.0.0 | PHP 源码学习使用 [^3] |



[^1]: 安装拓展：mongodb、redis、zip、intl、pdo、pdo_mysql、mysqli、pcntl、bcmath、imagick。安装软件：curl、composer、cron、zip、unzip、git
[^2]: 安装拓展：mongodb、redis、zip、intl、pdo、pdo_mysql、mysqli、pcntl、bcmath、gd、imagick。安装软件：curl、composer、cron、zip、unzip、git
[^3]: 使用gcc编译了php7.0.0的源码，开启了debug参数，用于调试学习PHP源码使用


## 相关项目 :link:

- [rovast/docker-examples](https://github.com/rovast/docker-examples) docker-compose example 集合
