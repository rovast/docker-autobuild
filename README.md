<h1 align="center"> docker-autobuild </h1>

<p align="center">基于各种官方 image 侯建的 Dockerfile 集合</p>

## 背景

:baby: [docker hub](https://hub.docker.com/) 为我们提供了好多便捷的环境。
官方提供的基础 image 一般都是比较精简的，我们需要在此基础上进行部分拓展，形成
自己的 Dockerfile。

本项目以此为基础，结合 [cloud docker](https://cloud.docker.com) 的 autobuild 功能，
打包了一些镜像。

> :bulb: 使用 docker 的 autobuild 自动构建的速度很快（毕竟是国外）。并且设置好了之后，
> 对应的 github 仓库的 Dockerfile 变更后，可以立即自动 build

---

## 一览

| Dockerfile 路径                                              | 官方镜像                                      | 本项目镜像                                                               | 说明      |
| ----------                                                   | -------------------------------------        | -------------------------------------                                   | ------------------------------------- |
| [gcc/8/Dockerfile](gcc/8/Dockerfile)                         | [gcc:8](https://hub.docker.com/_/gcc)        | [rovast/gcc:8](https://hub.docker.com/r/rovast/gcc)                     | 增加了 gdb，方便调试 |
| [gdb-php-src/7.0.0/Dockerfile](gdb-php-src/7.0.0/Dockerfile) | [gcc:8](https://hub.docker.com/_/gcc)        | [rovast/gdb-php-src:7.0.0](https://hub.docker.com/r/rovast/gdb-php-src) | 使用 gcc 编译了 php7.0.0 的源码，开启了 debug 参数，用于调试学习 PHP 源码使用|
| [php/7.2/cli/Dockerfile](php/7.2/cli/Dockerfile)             | [php:7.2-cli](https://hub.docker.com/_/php)  | [rovast/php:7.2-cli](https://hub.docker.com/r/rovast/php)               | 基于官方的 php7.2-cli，增加了以下拓展：mongodb、redis、zip，安装了以下软件：curl、composer、cron、zip、unzip、git|
| [php/7.2/fpm/Dockerfile](php/7.2/fpm/Dockerfile)             | [php:7.2-fpm](https://hub.docker.com/_/php)  | [rovast/php:7.2-fpm](https://hub.docker.com/r/rovast/php)               | 基于官方的 php7.2-cli，增加了以下拓展：mongodb、redis、zip，安装了以下软件：curl、composer、cron、zip、unzip、git|

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
