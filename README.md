# docker-autobuild

在官方的 docker images 中增加一些必要的软件、拓展、工具，来便于自己的开发

> 所有的镜像都基于 Dockerfile 自动构建，请放心查阅使用

## Tags

### rovast/php

|            | rovast/php:7.2-fpm                    | rovast/php:7.2-cli                    |
| ---------- | ------------------------------------- | ------------------------------------- |
| php-extensions | mongodb、redis、zip                   | mongodb、redis、zip                   |
| software   | curl、composer、cron、zip、unzip、git | curl、composer、cron、zip、unzip、git |

### rovast/gcc

|            | rovast/gcc:8                    |
| ---------- | ------------------------------- |
| software   | gdb |

结合 docker-compose 使用，方便 gdb 调试

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


### rovast/gdb-php-src

GDB 调试 PHP 源码使用，基于 gcc 官方镜像构建

|            | rovast/gdb-php-src:7.0.0                    |
| ---------- | ------------------------------- |
| software   | gdb |
