# docker-autobuild

社区为我们提供了诸多开箱即用的镜像，但是部分的镜像由于其通用性而牺牲了定制性，这里我们基于官方的进行二次构建，进而满足更丰富的应用场景。

访问 https://hub.docker.com/r/rovast 查看更多镜像

| 状态 | 镜像               | 说明                            |
| ---- | ------------------ | ------------------------------- |
|  [![php7.2-cli](https://github.com/rovast/docker-autobuild/actions/workflows/php7.2-cli.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/php7.2-cli.yml)    | rovast/php:7.2-cli | 增加诸多拓展和开发常用软件 [^1] |
|  [![php7.2-fpm](https://github.com/rovast/docker-autobuild/actions/workflows/php7.2-fpm.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/php7.2-fpm.yml)   | rovast/php:7.2-fpm | 增加诸多拓展和开发常用软件 [^1] |
|  [![php7.4-cli](https://github.com/rovast/docker-autobuild/actions/workflows/php7.4-cli.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/php7.4-cli.yml)    | rovast/php:7.4-cli | 增加诸多拓展和开发常用软件 [^2] |
|  [![php7.4-fpm](https://github.com/rovast/docker-autobuild/actions/workflows/php7.4-fpm.yml/badge.svg)](https://github.com/rovast/docker-autobuild/actions/workflows/php7.4-fpm.yml)   | rovast/php:7.4-fpm | 增加诸多拓展和开发常用软件 [^2] |


[^1]: 安装拓展：mongodb、redis、zip、intl、pdo、pdo_mysql、mysqli、pcntl、bcmath。安装软件：curl、composer、cron、zip、unzip、git
[^2]: 安装拓展：mongodb、redis、zip、intl、pdo、pdo_mysql、mysqli、pcntl、bcmath、gd。安装软件：curl、composer、cron、zip、unzip、git


---

文档整理中，下面是原文档


| Dockerfile 路径                                              | 官方镜像                                    | 本项目镜像                                                              | 说明                                                                                                                                                           |
| ------------------------------------------------------------ | ------------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [gcc/8/Dockerfile](gcc/8/Dockerfile)                         | [gcc:8](https://hub.docker.com/_/gcc)       | [rovast/gcc:8](https://hub.docker.com/r/rovast/gcc)                     | 增加了 gdb，方便调试                                                                                                                                           |
| [gdb-php-src/7.0.0/Dockerfile](gdb-php-src/7.0.0/Dockerfile) | [gcc:8](https://hub.docker.com/_/gcc)       | [rovast/gdb-php-src:7.0.0](https://hub.docker.com/r/rovast/gdb-php-src) | 使用 gcc 编译了 php7.0.0 的源码，开启了 debug 参数，用于调试学习 PHP 源码使用                                                                                  |
| [php/7.2/cli/Dockerfile](php/7.2/cli/Dockerfile)             | [php:7.2-cli](https://hub.docker.com/_/php) | [rovast/php:7.2-cli](https://hub.docker.com/r/rovast/php)               | 基于官方的 php7.2-cli，增加了以下拓展：mongodb、redis、zip、intl、pdo、pdo_mysql、mysqli、pcntl，安装了以下软件：curl、composer、cron、zip、unzip、git         |
| [php/7.2/fpm/Dockerfile](php/7.2/fpm/Dockerfile)             | [php:7.2-fpm](https://hub.docker.com/_/php) | [rovast/php:7.2-fpm](https://hub.docker.com/r/rovast/php)               | 基于官方的 php7.2-fpm，增加了以下拓展：mongodb、redis、zip、intl、pdo、pdo_mysql、mysqli、pcntl、bcmath，安装了以下软件：curl、composer、cron、zip、unzip、git |

## 注意事项 :warning:

:one: gdb 在 docker 里使用，需要注意一些启动参数，以下给出 docker-compose 的范例。

注意 **security_opt** 和 **cap_add** 配置

```yaml
version: '2'

services:
  gcc:
    image: rovast/gcc:8
    container_name: my-gcc
    security_opt:
      - seccomp:unconfined
    cap_add:
      - SYS_PTRACE
    volumes:
      - /home/rovast/Code:/home/Code
      - ./README.md:/home/README.md
    command: tail -f /home/README.md
```

正确挂载自己的代码目录到 /home/Code 即可

```bash
docker-compose up -d
docker exec -it my-gcc bash
```

## 相关项目 :link:

- [rovast/docker-examples](https://github.com/rovast/docker-examples) docker-compose example 集合
